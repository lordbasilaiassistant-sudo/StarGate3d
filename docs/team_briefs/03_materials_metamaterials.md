# Brief 03 — Materials & Metamaterials for the Wormhole Analogue

**Author:** Dr. Iris Vance (materials / metamaterials / magnetic shielding)
**Audience:** StarGate3d sim team + benchtop build team
**Status:** Working brief — verify vendor prices at quote time; pricing drifts.

---

## 1. Prat-Camps / Navau / Sánchez 2015 — Full Breakdown

**Reference:** Prat-Camps J., Navau C., Sánchez A. *A Magnetic Wormhole.* Sci. Rep. 5, 12488 (2015). DOI: 10.1038/srep12488.

**What it is.** A device that takes the magnetic field at point A and makes it reappear at point B as if pulled through an extra-dimensional tunnel. Crucially it does this *while the tunnel itself is magnetically invisible* — a compass swept past the device sees nothing where the hose runs, but the field "teleports" from one mouth to the other and emerges looking like an isolated magnetic monopole.

**Geometry — three nested layers** (described in the SI of srep12488):

1. **Inner ferromagnetic hose / core.** A spiral-wound mu-metal foil rolled into a tube. Acts as a high-permeability waveguide for B-field lines — analogous to an optical fiber for static magnetic flux. The hose runs the full length of the device and pokes out the two "mouths."
2. **Intermediate superconducting shell (Type II, YBCO).** The hose is wrapped around its midsection by a spherical shell tessellated from flat YBCO tape segments glued to a plastic former. Cooled to 77 K (LN₂). Function: expel external field via the Meissner effect (μ_r → 0). This is what makes the hose invisible — the SC shell forces external flux to detour around it as though the hose were not there.
3. **Outer ferromagnetic metasurface.** Discrete mu-metal plates arranged on a second, larger spherical former (radius R₃ > R₂). Function: cancel the magnetic distortion that the SC shell *would* otherwise produce (a perfect SC sphere acts like a magnetic anti-monopole and is itself visible). The outer μ → ∞ shell exactly compensates the SC's μ → 0 anomaly. Net result on external field: zero distortion. The wormhole reads as empty space from outside.

**Why this works — transformation optics for magnetostatics.** Maxwell's equations in source-free regions are form-invariant under coordinate transformations if you let ε and μ absorb the metric. Greenleaf, Kurylev, Lassas & Uhlmann (SIAM Rev. 2009, doi:10.1137/080716827) showed that a topology-changing transformation — punching a handle into 3-space — corresponds to an annular shell with prescribed anisotropic μ(r). Prat-Camps simplified this dramatically: in the *magnetostatic* limit (∇×H = 0, ∇·B = 0) you don't need full anisotropic μ; you need (a) a high-μ channel, (b) an isotropic μ→0 cloak, (c) an isotropic μ→∞ outer compensator. Off-the-shelf materials suffice.

**What they achieved.** Transmission of a dipole field from one mouth to the other with the output appearing monopolar (the dipole partner is "hidden" at the far mouth). Source dipole strengths in the ~few mT range at the mouth (NdFeB hand magnet class). External field undetectable to within the noise of their fluxgate (~µT). Device diameter ≈ 8 cm (R₃ ≈ 4 cm), hose length ~14 cm. **DC only.** Effect demonstrated for static fields; the SC shell limits the bandwidth — eddy losses kill it at audio frequencies and up.

**Limits acknowledged by authors.**
- Not perfect near the mouths (finite openings break the spherical symmetry).
- DC / quasi-static only. Not an EM wormhole — fields above the SC's penetration depth time-scale leak.
- Field magnitude conserved along the hose (it's a *channel*, not an amplifier). Output ≈ input minus losses.
- This is **not** a spacetime wormhole. No mass or energy passes through; nothing exotic happens. It is a transformation-optics illusion in B-field space.

---

## 2. Replication BOM — Hobbyist / Tabletop Scale (~5–10 cm device)

Target: a device the user can wave a fluxgate around and *measure* the topology change vs. a control (bare magnet, then bare hose, then full nested device).

| Item | Spec | Vendor | 2025–26 USD | Notes |
|------|------|--------|-------------|-------|
| Mu-metal foil, adhesive | 4" × 0.004" thick, by the inch | Magnetic Shield Corp. (MUT004-4) via EDMO / Aircraft Spruce | ~$12–$18 / ft length (~$3.5–5/in) | ≈$45–60/ft² effective. Need ~2–3 ft². |
| Mu-metal sheet, larger | 12"×12" × 0.014" (Co-NETIC AA / MuMETAL stress-annealed) | Magnetic Shield Corp. (quote) / Less EMF retail | $120–$200/sheet | For outer shell plates. |
| NdFeB magnets | N52, 1/2"–1" cube or cylinder | K&J Magnetics | $5–$25 | Field source. |
| Hall probe / fluxgate | DRV5055 analog Hall (1mT–80mT) or AlphaLab Milligauss meter | DigiKey / AlphaLab | $5 (chip) / $250 (meter) | Chip + Arduino works for first pass. |
| Gauss meter (better) | Bartington Mag-03 fluxgate (research grade) | Bartington / used eBay | $400–$1500 used | Needed for cloak verification (µT-level residual). |
| Plastic spherical former | 3D-printed PETG or PLA, R₂ ≈ 3 cm, R₃ ≈ 4 cm | self / Shapeways | $0–$30 | Print as hemispheres, glue. |
| Ferromagnetic powder (optional inner core fill) | Mn-Zn ferrite or carbonyl iron | Amazon / Magnetic Component Engineering | $20–$40/kg | For experiments with bulk vs. foil core. |
| **Superconductor (the expensive step)** | YBCO bulk disk 28–56 mm | CAN Superconductors (CZ) or Quantum Levitation (IL) | $300 (28 mm) – **$1119 (56 mm)** | One disk is *not enough*; need a tessellation. |
| YBCO tape (better for tessellation) | 2G HTS tape, 4 mm × 1 m | SuperPower / Shanghai Superconductor / surplus | $50–$200/m | Closer to what Prat-Camps used. |
| LN₂ dewar + LN₂ | 4 L cryo-flask + ~5 L LN₂ | US Cryogenics / local welding gas supplier | $150 dewar + $1–3/L LN₂ | ~$10–20 per experiment session. |

**Realistic all-in:**
- **Phase 1 (no SC, "magnetic hose" only):** ~$300–$500. Foil + magnets + Hall sensor + 3D-printed former. Demonstrates field guiding through hose. **Not a wormhole** — the hose is visible from outside. But it is a real, publishable measurement and a sanity check on permeability modeling.
- **Phase 2 (with SC, full Prat-Camps replica):** ~$2000–$3500 incl. one LN₂ refill cycle. Tape-based SC tessellation is cheaper than bulk disks and matches the original geometry better.

**Honest answer on skipping YBCO for v1:** Yes, skip it for v1. The hose alone gives you a measurable, instructive system: you can verify B-field channeling, compute the demagnetization tensor, and validate the FE solver. Without the SC layer the device is *not invisible*, but it *is* a magnetic-field guide — and that's the half of the physics the simulator needs to nail first. Add the SC shell in Phase 2 once the solver agrees with the hose-only data within ~10%.

---

## 3. Scale-Up Paths — 5 cm → 1 m

**What stops it at small scale.** Three things, in order of severity.

1. **Saturation of mu-metal.** Mu-metal saturates at B_sat ≈ 0.7–0.8 T. A strong NdFeB source will saturate the hose walls and B-field will leak everywhere. At 5 cm with a 0.5 T magnet this is already a real concern. At 1 m you can use a far stronger source, but the wall thickness must scale to keep B_wall < 0.7 T — meaning multi-mm laminated mu-metal stacks (annealed *after* forming, or shielding effectiveness collapses). A 1 m device wants a ~1 cm-equivalent total mu-metal wall, in laminated layers with insulator between to suppress eddy currents.
2. **Superconductor critical field and critical current.** YBCO bulk H_c2 is huge (>100 T at 4 K) but at 77 K it's effectively limited by J_c, the depinning current. A bigger device sees more flux and demands more screening current per unit length of tape. Above some threshold the SC goes resistive and the cloak fails. Mitigation: cool below 77 K (drop to ~30 K with a Gifford–McMahon cryocooler — kills hobbyist budget) or use thicker / multi-layer tape stacks.
3. **Geometric fidelity of the outer metasurface.** The discrete mu-metal plates that compensate the SC need to tessellate the sphere with sub-wavelength-equivalent pitch. At larger scale, "sub-wavelength" for static fields means "small compared to R₃," which is easy — but plate-to-plate gaps become flux leaks that scale with perimeter. You need progressively finer tessellation, not just bigger plates.

**Pushing past magnetostatic.** This is where it gets interesting and where the team should aim.

- **Quasi-static AC (DC – 1 kHz).** SC shell still works (penetration depth is geometry-set, not frequency-set, until you hit the gap edge). Mu-metal still works but eddy losses grow as f². Need laminations. Buys you the ability to *modulate* the throughput — a signaling channel through the wormhole. This is real and underexplored.
- **RF / microwave.** SC shell becomes lossy; mu-metal becomes useless. Need to switch to transformation-optics metamaterials (split-ring resonators, etc.) — Greenleaf et al.'s original 2007 proposal. No experimental demonstration of an EM wormhole as of 2026 to my knowledge — closest are 2D cloaks. **High-value target:** be the first lab to demonstrate one at S-band (~3 GHz) using printed-circuit metasurfaces. ~$5–15k of materials, doable in a garage.
- **Coupling field types.** Acoustic + magnetic, or thermal + magnetic, share the same Laplace-equation transformation-optics math (∇·(σ∇T)=0 ↔ ∇·(μ∇φ_m)=0). A device that is simultaneously a thermal cloak and a magnetic wormhole is buildable and would be *novel*. This is a real publishable angle for us.

**New failure modes at 1 m scale.** Mu-metal sheet warping during anneal (mu-metal must be annealed *after* forming; strain destroys permeability). Cryostat size and LN₂ consumption (1 m sphere ≈ 0.5 m³ ≈ ~$400/refill in LN₂). Mechanical force on the SC from the source magnet (Meissner repulsion at 1 m diameter and 0.5 T can be hundreds of newtons — secure mounting required). Earth field becomes a non-negligible bias (50 µT, but over 1 m geometry the gradient matters).

---

## 4. Other Metamaterial Portal Analogues — Real-or-Hyped Audit

| Analogue | Status | Wavelength / regime | Cost to replicate | Note |
|----------|--------|---------------------|-------------------|------|
| **Optical / EM wormhole** (Greenleaf, Kurylev, Lassas, Uhlmann 2007/2009) | Theory only — no experimental wormhole as of 2026. 2D cloaks demonstrated at microwave (Schurig et al. 2006, Science 314:977) and near-IR (Valentino et al. Nature Mater. 2009). | µwave through near-IR | $5–50k for microwave | **Real opportunity.** No one has built the wormhole version. |
| **Photonic "wormhole" (nonlocal metasurfaces)** Nature Comms 2025 doi:10.1038/s41467-025-63981-3 | Recent — uses nonlocal photonic structures to mimic parallel-space topology. Real demo, optical band. | Visible / NIR | $20k+ (lithography) | Verify status; flagged [unverified scope]. |
| **Acoustic black-hole / wormhole analogues** (Visser gr-qc/9712010; Unruh 1981; Nottingham water-tank 2019) | Real demos for *black holes* in flowing-fluid setups. Wormhole-specific acoustic demos are rare; theoretical (Simpson–Visser metric, arXiv 2412.02727 explores BEC acoustic wormholes). | Audio in water / sound in BEC | $5–30k tank, $250k+ BEC | Black-hole side mature; wormhole side embryonic. |
| **BEC analogue black hole** (Steinhauer Nature 569:688, 2019, doi:10.1038/s41586-019-1241-0) | **Real.** Sonic horizon in ⁸⁷Rb BEC, thermal Hawking spectrum measured. **No** wormhole-specific BEC demo as of 2026. (User-cited arXiv 1809.00913 is Steinhauer-adjacent; 1910.09363 is the canonical follow-up. Verify exact ID.) | Sonic / cold-atom | $250k–$1M apparatus | Out of hobbyist reach. |
| **Thermal cloaks / concentrators** (Schittny, Kadic, Guenneau, Wegener, Phys. Rev. Lett. 110, 195901, 2013, doi:10.1103/PhysRevLett.110.195901) | **Real.** Heat-flux cloak in copper/PDMS plate. Same Laplace math as magnetostatic cloak. | DC heat | $200–$1000 | Cheapest demo; perfect "warm-up" project. |

**Take:** The Prat-Camps magnetic wormhole is the only experimentally realized portal-topology analogue. Thermal cloaks share the math and are the cheapest sandbox. EM wormholes are the open prize. BEC and acoustic horizons are interesting but off-strategy for a renter's apartment.

---

## 5. Simulator Features — What the "Build Mode" Must Do

The sim must let the user place real materials and see the resulting field. Five concrete features:

1. **Magnetostatic FE solver — vector potential formulation.** Solve ∇×(μ⁻¹∇×**A**) = **J** + ∇×**M** with **B** = ∇×**A** on a tetrahedral mesh. Use first-order Nédélec edge elements (vector A is naturally edge-based; avoids spurious modes). Backend: Python + scikit-fem or compiled C++ (MFEM / FEniCS bindings). Real-time on small meshes (~50k tets); precompute for large.
2. **Material library with nonlinear B-H.** Mu-metal, soft iron, ferrite, NdFeB (with hard remanence M_r and coercivity H_c), Type-II SC (London-equation regime: μ_r → 0 above H_c1, with penetration depth λ_L). Saturation matters — mu-metal *cannot* be modeled as μ_r = 50000 constant. Use a piecewise B(H) curve and Newton iteration. Math: H = B/μ₀ − M(B), with M from a tanh fit to vendor data sheets (Magnetic Shield Corp. publishes B-H for MuMETAL — pull and digitize).
3. **Cloak / wormhole topology visualizer.** Streamline integration of B-field through a transparent volume render. Color by |B|; opacity by ∇·B residual (numerical sanity check). Add a "Prat-Camps mode" that toggles the SC shell on/off and shows the field-line topology change as an animation. This is the pedagogical money shot.
4. **Transformation-optics layer designer.** User specifies a desired coordinate transform (e.g., punch a hole between point A and point B). Solver computes the required μ_r tensor field via the Jacobian: μ' = J·μ·J^T / det(J). Display where this exceeds physical bounds (μ_r > 100k impossible at room T; μ_r < 0.001 needs SC). Highlights what's buildable vs. what's transformation-optics fantasy.
5. **Eddy-current / quasi-static AC mode.** Solve ∇×(σ⁻¹∇×**H**) + jω**B** = 0 in conductors. Lets the user sweep frequency and watch the SC cloak fail above its corner frequency. Math: complex-valued FE on the same mesh, σ from material library. This is what tells the build team whether their AC modulation idea will work before they buy any tape.

**Stretch features:** thermal solver on the same mesh (∇·(κ∇T) = 0) for thermal-cloak co-design; CSG construction tree (place "mu-metal sphere R=4 cm thickness 0.5 mm minus YBCO sphere R=3 cm" as Boolean ops); export to STL for 3D-printing the formers.

---

## 6. What an Apartment-Renter in NY Can Build Safely

**Static magnetic field — ICNIRP 2009 limits** (still current 2026): general public 400 mT (4000 G) any body part; occupational 2 T head/trunk, 8 T limbs. **Threshold for transient vertigo / nausea: 2–3 T.** Source: ICNIRP guidelines, https://www.icnirp.org/en/frequencies/static-magnetic-fields-0-hz/

**Practical: with a 6-year-old in the house.**
- **Safe.** NdFeB magnets up to a few cm, used carefully (pinch hazard is a *bigger* risk than field — these things will take fingertips off if they snap together; the field at 10 cm is already <10 mT). Hall probes, Arduino electronics, mu-metal sheets, ferrite cores — all inert. Working B-field at the device exterior in the Prat-Camps replica is well under 10 mT at any accessible point. Limit child access to the bench, magnets in a locked drawer.
- **Iffy.** YBCO + LN₂. LN₂ itself is a real hazard — cold burns, asphyxiation in unventilated rooms (1 L LN₂ → 700 L gaseous N₂; small NY apartment kitchen volume ~30 m³, single dewar boil-off can drop O₂ noticeably with door closed). Rules: open window + door, child out of room, no carpet (LN₂ spills shatter brittle floors and freeze fingers), face shield, leather (not insulated synthetic) gloves, dewar on a stable surface at floor level. Quantity ≤ 4 L at a time. Renter consideration: nothing here damages the apartment, but a spilled LN₂ on a finished hardwood floor will leave a thermal-shock mark. Use a tray.
- **No.** Do not build pulsed-power coils (capacitor bank → coil) that exceed ~100 V or store >10 J. That is the regime of "things that arc, set fires, and hit the kid." Do not run mains-powered electromagnets above ~30 V DC at the bench. Do not attempt RF wormhole demos above 10 W (FCC license territory; also RF burns). No high-vacuum (turbo-pumps + glass = implosion). No exotic chemicals (the YBCO disk arrives finished — don't try to synthesize it).

**Bottom line for v1 (Phase 1, no SC):** entirely safe with normal magnet hygiene. **Phase 2 with LN₂:** safe *with explicit ventilation discipline and child not in room*. Phase 3 (RF / pulsed) requires renting time at a university lab, not doing it at the kitchen table.

---

## 7. Citations

- Prat-Camps J., Navau C., Sánchez A. *A Magnetic Wormhole.* Sci. Rep. 5, 12488 (2015). DOI: **10.1038/srep12488**. https://www.nature.com/articles/srep12488 ; PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC4542659/
- Greenleaf A., Kurylev Y., Lassas M., Uhlmann G. *Cloaking Devices, Electromagnetic Wormholes, and Transformation Optics.* SIAM Review 51:3 (2009). DOI: **10.1137/080716827**. https://epubs.siam.org/doi/10.1137/080716827
- Schurig D. et al. *Metamaterial Electromagnetic Cloak at Microwave Frequencies.* Science 314:977 (2006). DOI: **10.1126/science.1133628**.
- Valentine J., Li J., Zentgraf T., Bartal G., Zhang X. *An optical cloak made of dielectrics.* Nature Materials 8, 568 (2009). DOI: **10.1038/nmat2461**. https://www.nature.com/articles/nmat2461
- Schittny R., Kadic M., Guenneau S., Wegener M. *Experiments on transformation thermodynamics: molding the flow of heat.* Phys. Rev. Lett. 110, 195901 (2013). DOI: **10.1103/PhysRevLett.110.195901**.
- Steinhauer J. *Observation of quantum Hawking radiation and its entanglement in an analogue black hole.* Nature Phys. 12, 959 (2016). arXiv:**1510.00621**.
- Muñoz de Nova J.R., Golubkov K., Kolobov V.I., Steinhauer J. *Observation of thermal Hawking radiation and its temperature in an analogue black hole.* Nature 569, 688 (2019). DOI: **10.1038/s41586-019-1241-0**. [user cited arXiv:1809.00913 — verify; canonical follow-up is **arXiv:1910.09363**, "Observation of stationary spontaneous Hawking radiation"] **[unverified arXiv ID]**
- Visser M. *Acoustic black holes: horizons, ergospheres and Hawking radiation.* Class. Quantum Grav. 15:6 (1998). arXiv:**gr-qc/9712010**.
- *Nonlocality-enabled photonic analogies of parallel spaces, wormholes and multiple realities.* Nature Comms (2025) doi:**10.1038/s41467-025-63981-3**. https://www.nature.com/articles/s41467-025-63981-3 **[unverified scope — confirm wormhole claim]**
- ICNIRP. *Guidelines on Limits of Exposure to Static Magnetic Fields.* Health Phys. 96(4):504 (2009). https://www.icnirp.org/en/frequencies/static-magnetic-fields-0-hz/
- **Vendors.** Magnetic Shield Corporation: https://www.magnetic-shield.com/ (MuMETAL sheet & foil, quote-based). EDMO / Aircraft Spruce: https://www.aircraftspruce.com/catalog/elpages/edmomumetal.php (foil retail). K&J Magnetics: https://www.kjmagnetics.com/ (NdFeB). CAN Superconductors (CZ): https://shop.can-superconductors.com/ (YBCO bulks, e.g., CSYL-28SE). Quantum Levitation (IL): https://quantumlevitation.com/ (YBCO 56 mm disk, **$1,119**, 400 N levitation force, 2–3 wk lead time). AlphaLab: https://www.alphalabinc.com/ (Milligauss meter). Bartington: https://www.bartington.com/ (research fluxgates). DigiKey (Hall ICs, e.g., TI DRV5055).

---

**Recommended next moves for the team.** (a) Build Phase-1 hose-only replica this month (~$400) and validate against the magnetostatic FE solver before any SC purchase. (b) In parallel, implement features 1, 2, and 3 from §5 — those alone make the sim useful for the build team. (c) Treat the EM-wormhole-at-microwave as the medium-term aspirational target; treat the Prat-Camps replica as the near-term credibility build.
