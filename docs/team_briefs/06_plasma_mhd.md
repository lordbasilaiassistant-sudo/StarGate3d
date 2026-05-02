# Brief 06 — Plasma, MHD, and the Honest Map of "Plasma-as-Portal"

**Author:** Dr. Saavik Roy (plasma physics — MHD, magnetic confinement, plasma toroids)
**Audience:** StarGate3d sim team + benchtop build team
**Status:** Working brief. Numbers are device-class typicals; verify against the cited papers before quoting in publication.

---

## 0. Why this brief exists

The Stargate "puddle" is the iconic image of the property: a vertical, glowing,
toroidal-edged disk you can step through. Two of those features map onto real
plasma physics — toroidal magnetic confinement *does* produce stable luminous
plasma rings, and reconnection *does* change magnetic field-line connectivity.
Neither makes a wormhole. The job of this brief is to keep the sim visually
grounded in real plasma geometries (Iris's metamaterial brief covers the static-B
side; mine covers the *glowing, time-dependent* side), to flag which
"plasma-as-portal" claims are mainstream-falsified, and to hand the build team
three apartment-buildable demos and the GPU team three implementable scenes.

Hana's GR brief (`01_*.md`) covers wormhole geometry; Iris's materials brief
(`03_*.md`) covers the static magnetic wormhole and metamaterial cloaks. I do
not re-derive their content. Where I touch metamaterials it is plasma-as-medium
(reconnection sheet ↔ thin-shell wormhole analogy, etc.), not the Prat-Camps
device.

---

## 1. What real plasma toroids look like

Three classes are relevant. All are *self-organized* magnetic plasma equilibria
— the plasma carries the currents that produce the fields that confine it.

**Tokamak.** Toroidal vessel, external toroidal field coils, plasma current
driven by a central solenoid. *Not* compact — the field lines wrap a hole the
machine sits around. Visually: a luminous donut whose ergosurface (poloidal
flux surfaces) is actually plotted via Thomson scattering, not by eye. Typical
parameters in research devices: T_e ~ 1–20 keV, n_e ~ 10¹⁹–10²⁰ m⁻³, pulse
length ~seconds (ITER design: 400 s burn). *Not the Stargate image.* The
Stargate puddle is closed in front, no central pillar — that's an FRC or
spheromak shape, not a tokamak.

**Spheromak.** Compact toroid, *no* central column. Self-organized Taylor state
(minimum magnetic energy at fixed helicity). SSPX (Sustained Spheromak Physics
Experiment, LLNL, 1999–2008): major radius R ≈ 0.33 m, minor radius a ≈ 0.23 m,
T_e up to 0.5 keV (later runs ~350 eV typical), B_tor ≈ 0.6 T,
β_e ≈ 5%, *plasma duration 1.5–3.5 ms* sustained by coaxial helicity injection
(CHI). SSX (Swarthmore Spheromak Experiment, Brown lab): two magnetized plasma
guns into a 0.5 m copper flux conserver — used heavily for *reconnection*
studies (see §2). Sustained spheromak lifetimes scale with helicity-injection
power; floating spheromaks (no drive) decay in tens of µs. — Hooper et al.,
*Nucl. Fusion* 39, 863 (1999); Geddes et al., *Phys. Plasmas* 5, 1027 (1998).

**Field-Reversed Configuration (FRC).** Compact toroid with *zero* toroidal
field — the plasma is held by purely poloidal closed field lines, the elongated
"smoke ring" geometry. Closest visual analog to the Stargate disk: an FRC seen
end-on is a glowing ring around a darker interior. TAE Technologies' C-2W
("Norman", 2017–) is the modern record holder: *T_e > 0.75 keV*, total plasma
energy ~13 kJ, *sustained 30–40 ms* via neutral-beam injection — and as of
2025 they demonstrated FRC formation by NBI alone (300–350 kA fast-ion ring
current at 8 MW effective beam power), without theta-pinch formation. — Gota
et al., *Nucl. Fusion* 59, 112009 (2019); Binderbauer et al., *Nat. Commun.*
16, 2025, doi:10.1038/s41467-025-58849-5; Galea et al., *J. Fusion Energy*
review 2023, https://w3.pppl.gov/ppst/docs/galea2023jfe.pdf.

**What produces the visible glow.** Recombination + line emission. At fusion
temperatures the bulk plasma is too hot to radiate visibly (fully stripped, only
bremsstrahlung and synchrotron, mostly UV/X-ray). The *visible* glow people
photograph is from the cooler edge plasma: hydrogen Balmer-α (656 nm, the pink
line you see in every tokamak photo), impurity line radiation (carbon, oxygen),
and plasma-wall interaction. For sim purposes: a luminous toroid is *physically*
plausible at edge T_e ≈ 1–10 eV and n ≈ 10¹⁸–10²⁰ m⁻³, well inside any of these
device classes' edge regions.

**Lifetime is the catch.** None of these plasmas live more than seconds; the
"open Stargate, walk through, stays open until shut" timescale is *seven orders
of magnitude* off any real magnetic confinement. The longest-lived stable
magnetic plasma toroid on Earth as of 2026 is a sustained tokamak (EAST,
Hefei, 2023: ~1000 s at 70 MK with non-fusion-relevant density). Don't oversell.

---

## 2. Magnetic reconnection — and is it "topological"?

**The physics.** In ideal MHD, magnetic field lines are frozen into the plasma:
two fluid elements that share a field line at t=0 share one forever. When
resistivity, electron inertia, or turbulence break the frozen-in condition in
a thin current sheet, field lines from one topological domain *re-pair* with
field lines from another. The classical 2D picture is the X-point Sweet-Parker
sheet (1957–58) and the Petschek slow-shock geometry (1964); 3D reconnection
proceeds at *quasi-separatrix layers* (QSLs — Priest & Démoulin 1995) and
null-points where field-line connectivity changes drastically without a true
mathematical separatrix. Standard text: **Priest & Forbes,** *Magnetic
Reconnection: MHD Theory and Applications*, Cambridge UP 2000 — still the
canonical reference. Modern review with collisionless physics: Ji, Daughton,
Yamada et al., *Outstanding questions on magnetic reconnection*, Space Sci.
Rev. 2025, doi:10.1007/s11214-025-01143-z (arXiv:2407.09670).

**Is reconnection "topology change" in the wormhole sense?** No, but the
linguistic overlap is real and it's where pop-physics gets confused. The
distinction is sharpened in Jafari, *Does Magnetic Reconnection Change
Topology?*, arXiv:2408.13732 (revised April 2025): in 2D, reconnection *is*
topology-change of the field-line pattern — separatrices reconnect, X-points
move. In 3D laminar flow, topology change happens by dissipation at a rate
proportional to resistivity. In 3D turbulence, "spontaneous stochasticity"
makes topology change fast and resistivity-independent. **None of this is
spacetime topology change.** The topology that changes is the connectivity
graph of field lines in a fixed Euclidean 3-space; the spacetime manifold is
unaffected. Reconnection ≠ wormhole. Selling it as one would be exactly the
kind of thing this team should not do.

**What it *does* give the sim.** A scientifically real "throat-like"
phenomenon: a thin current sheet where field lines cross-connect, plasma
inflows from two sides and outflows from two more, all visible in 3D vector
fields. Reconnection sheets are *visually striking* (filaments, plasmoids,
flux ropes) and the math is clean. Nature's biggest reconnection events —
solar flares, magnetar giant flares, MMS-mission magnetopause crossings — are
genuine physics worth the user's attention. We can build a "topology-change
demo" that is honest plasma topology change and explicitly *not* spacetime
topology change.

---

## 3. DIY plasma toroids — what an apartment can build under $500

**Tier 0 — toy plasma globe ($25).** Buy off the shelf. ~5 kV, 25 kHz Tesla
oscillator into a partially-evacuated noble-gas globe. Filaments, no toroid.
Good for the LN₂-magnetic-quench demo (§6).

**Tier 1 — xenon plasma toroid, "Tokamak in your home" ($100–250).**
Strattman/BagelGen/Zerg Labs xenon-filled spherical bulb (~13 cm dia, ~15 torr
xenon: e.g., BagelGen "BagelFlask"), driven by a 12 MHz two-turn PCB inductor
wrapped around the equator. The bulb sits inside the coil; xenon ionizes into
a *toroidal* plasma loop that acts as the secondary winding of an air-core
transformer. **This is the closest cheap visual to a Stargate puddle that
exists.** ~$65 for a kit on AliExpress; ~$200 if you want the open-source
Hackaday "sky-guided PCB edition" with proper RF shielding. Refs:
Strattman / BagelGen at https://bagelgen.com/ and the Hackaday project pages
(`hackaday.io/project/198021` and `194683`). Safety: 12 MHz at >50 W gets RF
burn territory; do not touch the drive coil under power.

**Tier 2 — low-pressure RF inductive discharge in a glass tube ($300–500).**
Sealed Pyrex tube (~10 cm dia × 30 cm) filled with Ar at 0.1–1 torr,
single-loop external induction coil at 13.56 MHz (the ISM band — *legal*
unlicensed). At a few hundred W RF you get a stable bright "ring" inductive
mode (E-mode → H-mode transition). Build risk: requires a vacuum pump
(~$200 for a used two-stage rotary vane on eBay), ISM-band RF generator
(~$150 for a 100 W kit), tuning network (~$50 in components), and a glass
shop or pre-made discharge tube. Total ~$400–500 if scrounged; $1500+ retail.
This is the lab-grade demo.

**What you cannot do under $500.** A real demountable Penning trap (~$10k+,
needs UHV and a 1+ T magnet), a real tokamak (Inductrence/PrincetonOpenSource
projects start at >$100k), a sustained spheromak (multi-MJ capacitor banks,
~$1M). The *visual* Stargate puddle from Tier 1 is good enough that the sim
team should treat it as the reference image and not chase scale.

---

## 4. Plasma-as-portal — honest assessment of fringe claims

The team will get asked about these. We need a defensible position.

**Heim theory (B. Heim, 1950s–80s; Dröscher–Häuser "Heim Quantum Theory" 2005).**
Claims to derive particle masses and to predict an FTL "gravitophoton" drive
through an extra-dimensional space accessed by rotating superconductors in a
strong B-field. Status: *firmly fringe*. The DARPA "Advanced Aerospace Threat
Identification Program" (AATIP) DIRD report on warp drives (2010, FOIA-released
2018) discussed it. Mainstream: Geoffrey Landis's "Rise and Fall of Heim
Theory" (geoffreylandis.com/Heim_theory.html) catalogs the predictive failures
— excited-particle states predicted that don't exist, mass formulas later
shown to have hand-tuned fitting parameters (independent analysis 2006). The
theory's notation is non-standard, derivations are partly unpublished, and
nothing has reproduced the mass-prediction success under blind tests. Position
to take: *not crackpot, but not science yet* — interesting historical artifact,
no operational predictions the sim should respect.

**Tajmar gravitomagnetic London moment (Tajmar & de Matos, ESA-funded, 2006).**
Claim: a rotating Nb superconductor at 6500 rpm produces an anomalous
gravitomagnetic field of order 10⁻⁴ g near the rotor, ~20 orders of magnitude
larger than GR's frame-dragging prediction. Original paper:
arXiv:gr-qc/0603033. Status: *no successful independent replication in 20
years.* Graham et al. 2008 (Canterbury) and a Stanford repeat at higher
sensitivity both saw nothing above noise. Tajmar's own later EmDrive
replication work (see below) showed his lab is *capable of finding their own
errors* — which is to his credit and also undermines the original claim.
**Mainstream consensus: artifact (likely thermal or mechanical coupling of
the accelerometers to the rotor).** Don't put it in the sim.

**EmDrive (Shawyer 2001; NASA Eagleworks 2016).** Claimed thrust from a
closed RF cavity. *Definitively falsified* by Tajmar's own group at TU Dresden
(Space Propulsion Conference 2020+1, March 2021): with a null-balance setup
and active thermal stabilization, *zero thrust above 0.1 µN noise floor at up
to 100 W input power*. Tajmar's quote: "Our measurements refute all EmDrive
claims by at least three orders of magnitude." The original positive results
were thermally-induced false zero on the scale. — Kößling, Monette, Weikert,
Tajmar, *CEAS Space J.* 14, 255 (2022),
doi:10.1007/s12567-021-00385-1. **Closed file. Do not platform.**

**Position for the project.** Where these come up in user questions, we link
the falsification papers and move on. The sim does not contain a "Heim drive"
mode. We *do* let users explore the actual published math of warp / wormhole
metrics (which violate energy conditions and are honest about it) — that's
science fiction grounded in GR, not pseudoscience grounded in misread
data.

---

## 5. Three concrete simulator features

**(F1) Toroidal MHD scene driven by ideal MHD on the GPU.** Solve the ideal
MHD equations
```
∂ρ/∂t + ∇·(ρv) = 0
∂(ρv)/∂t + ∇·(ρvv + p* I − BB/μ₀) = 0          (p* = p + B²/2μ₀)
∂B/∂t − ∇×(v×B) = 0                             (with ∇·B = 0 maintained)
∂E/∂t + ∇·[(E + p*)v − B(v·B)/μ₀] = 0
```
on a 3D Cartesian grid in WebGPU compute shaders. Use a Godunov-type HLLD
Riemann solver (Miyoshi & Kusano, *J. Comput. Phys.* 208, 315 (2005)) — same
solver Athena uses (Stone et al., *ApJS* 178, 137 (2008); Athena++:
Stone et al., *ApJS* 249, 4 (2020), iopscience.iop.org/article/10.3847/1538-4365/ab929b).
Maintain ∇·B with constrained transport on staggered B-fields. For real-time
WebGPU, target a 128³ grid → ~30 fps on a mid-range GPU; reference port:
the 2D CUDA Athena port (Wasiljew & Murawski 2014). Initial condition:
analytic FRC equilibrium (Rigid-rotor or Hill's vortex profile) with a
visible Balmer-α emissivity proxy (∝ n_e n_H × T_e^{-1/2} for recombination,
or just `n²` for a pretty proxy). **Cost:** ~5k lines of WGSL + ~2 weeks
engineering. GPU memory at 128³×8 fields×fp32 ≈ 64 MB, fine.

**(F2) Reconnection demo — Sweet–Parker / Harris-sheet IC.** Initialize a
2D Harris current sheet `B_x(y) = B_0 tanh(y/L)`, perturb, and let the GPU
MHD solver (F1, dropped to 2D) form an X-point. Render the field-line
connectivity in two colors (left-domain vs right-domain field lines); on
reconnection, lines change color along the user's pointer. Side-panel
explainer: "this is *field-line* topology change, not *spacetime* topology
change — see GR brief §1." Tracks against published Yamada/MRX (Magnetic
Reconnection Experiment, Princeton) figures; ref Yamada, Kulsrud, Ji,
*Rev. Mod. Phys.* 82, 603 (2010), DOI:10.1103/RevModPhys.82.603. **Cost:**
trivial extension of F1 — same solver, different IC, plus a connectivity
tracer. ~3 days.

**(F3) Cosmetic plasma-sheath shader on the wormhole throat.** Optional —
toggleable, off by default — a screen-space shader that renders a
plasma-sheath glow on Hana's wormhole throat *only when the user explicitly
turns on "Stargate aesthetic"*. Uses a Langmuir-Child-style space-charge
limited current proxy for opacity: `j ∝ V^{3/2}/d²` evaluated radially from
the throat. **Hana flagged "no entrance shimmer" in her brief §5; this
respects that** by being explicit-opt-in and labeled "non-physical aesthetic
overlay" in the HUD. Do not enable in the validation harness. ~1 day.

---

## 6. Three lab experiments under $5k

**(E1) Plasma globe in a strong-magnet field ($120 + child supervision).**
Plug-in plasma globe ($25), N52 cube magnet 1" ($25), Hall probe + Arduino
($30), iPhone for video. Bring the magnet near the globe. Filaments curve along
B-field lines (E×B drift); strong magnet *pinches* filaments into Larmor-radius
loops. **Demonstrates:** charged particle gyration, magnetic field
visualization. **Does not demonstrate** confined toroid — globe geometry is
wrong. Useful pedagogy, two-hour experiment, child-safe with normal magnet
hygiene (per Iris's safety note).

**(E2) 13.56 MHz RF inductive toroid ($1500–3500).** From §3 Tier 2, scaled.
Used Edwards rotary-vane vacuum pump (~$300 eBay), borosilicate discharge
chamber (~$400 custom or $200 surplus), 13.56 MHz 250 W RF generator + manual
matching network ($1200 for a hobbyist kit, $3000+ retail), Ar/Xe gas regulator
($150 + $50/cylinder). With proper matching, transition E-mode (capacitive,
filamentary) → H-mode (inductive, ring-shaped) at ~150 W input. **Demonstrates:**
real toroidal plasma in a glass vessel, controllable density and pressure,
visible Balmer-α / argon-line spectrum. Closest hobbyist build to a real
plasma toroid. Refs: Lieberman & Lichtenberg, *Principles of Plasma
Discharges and Materials Processing*, 2nd ed., Wiley 2005 — the standard
text on industrial RF discharges, not optional.

**(E3) Benchtop magnetic mirror ($600–2500).** Two opposing N52 ring magnets
(or coil pairs) mounted on a non-magnetic optical rail with a sealed
low-pressure (~10⁻² torr) Ar-filled glass bulb between them; drive a DC glow
discharge at 500–1000 V across the bulb axis. Charged particles with
v_perp/v ratio above the loss-cone bounce between the mirrors; you see a
*standing-wave-like density pattern* between the magnets. With permanent
magnets you get B ≈ 0.3–0.8 T at the throats. **Demonstrates:** magnetic
mirror confinement, loss-cone particle physics, μ-invariance (magnetic
moment as adiabatic invariant). Refs: Post, *Nucl. Fusion* 27, 1579 (1987);
modern miniature realization — Choi et al., *Sensors* 23, 1040 (2023),
mdpi.com/1424-8220/23/2/1040, used N52 magnets at 1230 mT residual flux for
a Penning-mirror miniature ion pump. **Does *not* demonstrate** a wormhole,
fusion, or anything FTL — just adiabatic invariance, which is the foundation
of all magnetic confinement.

---

## 7. What this brief commits to (and explicitly does not)

**Yes:** real toroidal-plasma visuals in the sim (F1), an honest reconnection
demo with the correct disclaimer (F2), three buildable apartment-scale
demos (E1–E3), and a written rebuttal page for Heim/Tajmar/EmDrive when
users ask.

**No:** plasma-driven warp drives, "ionizing the vacuum to make exotic
matter," EmDrive-mode toggle, Tajmar gravitomagnetic effects in the GR module.
A user toggling our sim should be able to see — clearly labeled — what is
real plasma physics, what is real GR, and where the unresolved frontier is.
The frontier does *not* run through any of the three falsified or unfalsifiable
fringe claims in §4.

---

## 8. Citations

- Priest E. R. & Forbes T. G. *Magnetic Reconnection: MHD Theory and
  Applications.* Cambridge UP, 2000. ISBN 0-521-48179-1.
- Ji H. et al. *Outstanding Questions and Future Research on Magnetic
  Reconnection.* Space Sci. Rev. (2025), DOI:10.1007/s11214-025-01143-z.
  arXiv:**2407.09670**.
- Jafari A. *Does Magnetic Reconnection Change Topology?* arXiv:**2408.13732**
  (v3, Apr 2025).
- Yamada M., Kulsrud R., Ji H. *Magnetic reconnection.* Rev. Mod. Phys. 82,
  603 (2010). DOI:**10.1103/RevModPhys.82.603**.
- Stone J. M. et al. *Athena: A New Code for Astrophysical MHD.* ApJS 178,
  137 (2008).
- Stone J. M. et al. *The Athena++ Adaptive Mesh Refinement Framework.*
  ApJS 249, 4 (2020). DOI:**10.3847/1538-4365/ab929b**.
- Miyoshi T. & Kusano K. *A multi-state HLL approximate Riemann solver for
  ideal MHD.* J. Comput. Phys. 208, 315 (2005).
- Hooper E. B. et al. *The Sustained Spheromak Physics Experiment (SSPX):
  design and physics results.* Plasma Phys. Control. Fusion 54, 113001
  (2012). [primary parameters]
- Geddes C. G. R. et al. *Scaling studies of spheromak formation and
  equilibrium.* Phys. Plasmas 5, 1027 (1998). [SSX]
- Gota H. et al. *Achievement of stable advanced beam-driven FRC plasmas.*
  Nucl. Fusion 59, 112009 (2019). [TAE C-2W parameters]
- Binderbauer M. et al. *Generation of field-reversed configurations via
  neutral beam injection.* Nat. Commun. 16 (2025).
  DOI:**10.1038/s41467-025-58849-5**.
- Galea C. et al. *The Princeton Field-Reversed Configuration for Compact
  Nuclear Fusion.* J. Fusion Energy review 2023.
  https://w3.pppl.gov/ppst/docs/galea2023jfe.pdf
- Lieberman M. A. & Lichtenberg A. J. *Principles of Plasma Discharges and
  Materials Processing*, 2nd ed., Wiley (2005). [RF inductive discharge
  reference]
- Post R. F. *The magnetic mirror approach to fusion.* Nucl. Fusion 27,
  1579 (1987).
- Tajmar M., de Matos C. *Experimental Detection of the Gravitomagnetic
  London Moment.* arXiv:**gr-qc/0603033** (2006). [the original claim]
- Kößling M., Monette M., Weikert M., Tajmar M. *High-accuracy thrust
  measurements of the EMDrive and elimination of false-positive effects.*
  CEAS Space J. 14, 255 (2022). DOI:**10.1007/s12567-021-00385-1**.
  [the falsification]
- Landis G. A. *Rise and Fall of the Heim Theory.*
  geoffreylandis.com/Heim_theory.html [unverified — informal author page,
  but the standard mainstream commentary; no peer-reviewed Heim review
  exists].
- *Hackaday* "Tokamak in Your Home: A Xenon Plasma Toroid," project
  198021, https://hackaday.io/project/198021 ; "Plasma Toroid (sky-guided
  PCB edition)," project 194683.
- Strattman/BagelGen xenon globes: https://bagelgen.com/.
- Choi Y. et al. *High-Efficiency Plasma Source Using a Magnetic Mirror
  Trap for Miniature-Ion Pumps.* Sensors 23, 1040 (2023).
  DOI:**10.3390/s23021040**. https://www.mdpi.com/1424-8220/23/2/1040

---

**Recommended next moves.** (a) F1 (toroidal MHD scene) is the highest-value
single deliverable from plasma — it's the visual the property is named after
and we can ship a real ideal-MHD solver in WebGPU in two weeks. (b) E1 is
free if the team already owns a plasma globe; do it this week as a content
shot. (c) Coordinate with Hana (GR brief) before F2 ships so the
"topology" disclaimer language is consistent across briefs — the user must
not walk away thinking reconnection ≈ wormhole.

— Saavik
