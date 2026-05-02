# Materials Ledger — what we buy, source, and refuse to buy

Synthesis of every concrete BOM item, vendor, price, and apartment-feasibility
note across briefs 01–11. Citations as `[B##]`. Renter in Vestal NY,
six-year-old daughter present, Capt. Torres's safety brief (B11) is binding.

**Core operating rule.** No money to spend until a build is validated. Phase-1
is the only thing that gets ordered before something works. Every Phase-2 and
Phase-3 line item is gated on Phase-1 producing a measurement that agrees
with the FE solver `[B03 §6 recommended next moves; B09 §3 expt B kill
criterion]`.

Prices are 2025–26 USD; verify at quote time. Items flagged `[unverified]`
are flagged in the source brief itself — do not silently launder.

---

## 1. Phase-1 build kit (target $300–500)

The mu-metal hose magnetic-wormhole replica + Hall probe + bench
instrument. **This is the one thing that gets bought.**

| Item | Spec | Vendor | 2025–26 USD | Lead time | Source brief |
|---|---|---|---|---|---|
| Mu-metal foil, adhesive | 4" × 0.004" thick, by the inch (MUT004-4) | Magnetic Shield Corp. via EDMO / Aircraft Spruce | ~$12–18/ft (~$3.5–5/in); ~$45–60/ft² eff. Need ~2–3 ft² | a few days (retail) | B03 §2 |
| NdFeB N52 magnet | ½–1" cube or cylinder | K&J Magnetics | $5–25 | days | B03 §2, B05 §6 |
| Hall IC (DRV5055A1) | analog, ±20–80 mT, ~30 µT rms in 1 Hz BW | DigiKey / TI | $5 chip / $50 board | days | B03 §2, B09 §1 |
| ADS1115 24-bit ADC | I²C, 4-channel | DigiKey / Adafruit | $10 | days | B09 §8 expt A |
| Arduino (Uno or Nano) | – | DigiKey / Amazon | $25 | days | B09 §8 |
| 3D-printed XYZ stage | linear rails + stepper drivers; PETG | self / scrounge | $100 incl. rails | days | B09 §8 expt A |
| 3D-printed spherical former | PETG/PLA hemispheres, R₂≈3 cm, R₃≈4 cm; glue | self / Shapeways | $0–30 | days | B03 §2 |
| Connectors / wire / dupont leads | – | DigiKey | $25 | days | B09 §8 |
| O₂ meter (portable) | <19.5% audible alarm; e.g. Macurco OX-6 or Forensics Detectors O2-300 | Macurco / Amazon | ~$150–200 used / new | days | B08 §2, B11 §1 |
| Class C dry-chem fire extinguisher | 2A:10B:C residential | Home Depot | ~$30 | same day | B11 §1 |
| Sheet-pan tray + silicone mat | floor protection under any cryo work | Amazon / kitchen supply | $25 | same day | B08 §2, B11 §3 |
| Cut-resistant gloves (A4 min) | mu-metal handling | Amazon | $15 | days | B11 §1 |
| Locked toolbox / drawer | NdFeB + magnet storage | hardware store | $20 | same day | B11 §2 |
| Plug-in circuit-tracer | map apartment branches before anything draws >5 A | Klein / Amazon | $30 | days | B11 §3 |
| CO + smoke combo alarm (lab room) | independent of building system | Amazon | $25 | same day | B11 §3 |
| USB fume extractor (soldering) | activated-carbon, ~15 cm from joint | Amazon | $40 | days | B11 §1 |
| In-line fuses + insulated 4 mm banana leads | DC supply work | DigiKey | ~$20 | days | B11 §1, §4 |

**Phase-1 total: ~$575 buys the entire benchtop including safety
infrastructure. Pure science BOM (without safety/storage items): ~$300.**

**What Phase-1 proves:** Phase-1 magnetic-hose-only replica `[B03 §2]`. The
hose alone is a real, publishable measurement — verifies B-field
channeling, lets us compute the demagnetization tensor, and validates the
FE solver before any SC purchase. Without the SC layer the device is
**not invisible** but **is** a magnetic-field guide. **Kill criterion
(B09 §8 expt A):** if field at hose mouth B is not ≥10× background within
a 2 cm radius, FE solver in B03 §5 is wrong and we stop coding the wormhole
sim until we understand why.

**What Phase-1 does NOT prove:** true magnetic invisibility of the
connecting tube. That requires the superconductor (Phase 2). It also is
not, and never will be, a spacetime wormhole.

**Apartment feasibility:** entirely safe with normal magnet hygiene. No
cryogens, no high voltage, no RF, no vacuum. Daughter-safe with locked
magnet storage and tweezers/wood pusher for placement `[B03 §6, B11 §1]`.
Bench can be set up on the dining table during school hours and broken
down at end of session `[B11 §5]`.

---

## 2. Phase-2 expansion (~$3–5 k)

YBCO sample, LN₂ dewar, used fluxgate, GPSDO, Michelson optics.
**Gated on Phase-1 producing a measurement that agrees with the FE solver
to ≤30% (Mager 1968 cylindrical-shielding analytic check, B09 §8 expt B).**

| Item | Spec | Vendor | 2025–26 USD | Lead time | Source brief |
|---|---|---|---|---|---|
| YBCO bulk disk | 28–56 mm | CAN Superconductors (CZ) | $300 (28 mm) – **$1,119 (56 mm)** | weeks | B03 §2 |
| YBCO 2G HTS tape | 4 mm × 1 m, closer to Prat-Camps original geometry, cheaper than bulk | SuperPower / Shanghai Superconductor / surplus | $50–200/m | weeks | B03 §2 |
| LN₂ dewar | 4 L cryo-flask (Cryofab CL-10 or used) | Cryofab / eBay | $400–600 new / $150–300 used | days | B03 §2, B08 §3 |
| LN₂ refill | per session | local welding-gas supplier (Airgas, Praxair/Linde) | $0.50–1.78/L bulk delivery; $2–5/L in 10–50 L dewars; $50–150 minimum-order fee. ~$10–20 per experiment session for a 4 L pour. | hours | B03 §2, B08 §3 |
| Cryo gloves | Tempshield Cryo-Gloves, leather (NOT insulated synthetic) | Tempshield / lab supply | $50–80 | days | B08 §2, B11 §1 |
| Face shield | full-face, not just safety glasses | lab supply | $30 | days | B08 §2, B11 §1 |
| Bartington Mag-03 fluxgate | 6 pT/√Hz at 1 Hz, ±70 µT–1 mT | Bartington / used eBay | $400–1500 used / new $3k+ | weeks | B03 §2, B09 §1 |
| Mu-metal sheet (larger) | 12"×12" × 0.014" Co-NETIC AA / MuMETAL stress-annealed | Magnetic Shield Corp. / Less EMF retail | $120–200/sheet | days | B03 §2 |
| Mn-Zn ferrite or carbonyl iron powder (optional core fill) | bulk | Amazon / Magnetic Component Engineering | $20–40/kg | days | B03 §2 |
| 3-layer mu-metal can (gradiometer shield, DIY from coffee cans + foil) | 12 oz cans + MagShield foil | DIY from Phase-1 stock | $80 each in materials | – | B09 §8 expt B |
| Used scroll pump | Edwards XDS-5 / Agilent IDP-3, oil-free | eBay / LabX | ~$1,500 used | weeks | B08 §1, §3 |
| Used small turbomolecular pump | Pfeiffer TPU 062, Edwards EXT 70, ~70 L/s, working with controller | eBay / LabX | $400–500 used; +$300–800 if controller separate (always confirm bundled) | weeks | B08 §3 |
| Pirani / capacitance gauge (used) | – | LabX / Capovani | $200–500 | weeks | B08 §4 |
| Helmholtz-coil pair | residual-field cancellation (Earth's 50 µT), trivial copper-wire build | self | ~$50 | days | B08 §4 |
| Honeywell HMC5883L breakout (gradiometer pair) | ~100 nT floor; cheap second probe | Adafruit / DigiKey | $10 each | days | B09 §8 expt B |
| Thorlabs EDU-MINT2/M Michelson kit | working interferometer on a breadboard | Thorlabs | ~$1.2–1.8k `[unverified 2026 price — B09]` | days | B09 §3, §8 expt C |
| Stabilized HeNe (Thorlabs HRS015B) | sub-MHz drift, λ/100 ≈ 6 nm path-length sensitivity | Thorlabs | ~$3 k | days | B09 §3 |
| Sorbothane breadboard pad | passive vibration isolation | Thorlabs MB1224 or used Newport | $150–300 | days | B09 §3, §8 expt C |
| Si photodiode (FDS100, FGA015) | NEP ~10⁻¹⁴ W/√Hz | Thorlabs | $20–200 | days | B09 §2 |
| Leo Bodnar Mini-Precision GPSDO | Allan dev. 1 s ~10⁻¹⁰–10⁻¹¹, day <10⁻¹² | leobodnar.com `[verify still listed 2026 — B09]` | $300 | days | B09 §6 |
| Surplus Rb (FE-5680A, LPRO-101) | Allan dev. ~10⁻¹¹ | eBay | $100–400 | weeks | B09 §6 |
| OCXO (Bliley NV45 used) | – | eBay | $50–300 | weeks | B09 §6 |
| Stanford SR830 lock-in (used) | – | ValueTronics / AccuSource | $3.5–4.5k | weeks | B09 §9 |
| Rigol DSA815 / used HP 4395A spectrum analyzer | for shot-noise calibration | eBay / instrument resellers | $1–3 k | weeks | B09 §2 |
| Femto HCA-S TIA / DIY OPA847 PCB (difference amp) | balanced photodetection | Femto / DIY | $50–1500 | weeks | B09 §2 |
| 50/50 beamsplitter, polarization optics, mode-matching telescope | – | Thorlabs | ~$500 | days | B09 §2 |

**Phase-2 total: ~$3.5–5 k for the baseline kit (one YBCO disk, dewar +
LN₂ logistics, used Mag-03, used scroll + small turbo, Helmholtz, Michelson
kit). Treasurer note from B08 §8: "$400 LN₂ dewar + $200 O₂ monitor + $1.5k
used scroll pump + $1.5k used small turbo. Total ~$3.5k buys us 77 K + HV
— enough for the magnetic-wormhole replica AND a Casimir bench at 10⁻⁶ Torr.
Anything below 77 K is a partner-lab conversation."**

**What Phase-2 unlocks:** Phase-2 full Prat-Camps replica (~$2–3.5k, B03 §2),
which is the actual 5–10 cm magnetic-wormhole device with the SC shell and
outer compensator. Plus 77 K + HV bench = static Casimir at µm range, OPO
squeezed-vacuum bench (with additional spend, B02), and the FE-solver
validation chamber (B09 §8 expt B).

**Apartment feasibility (B11 §5 risk assessment):** **CONDITIONAL GO**
subject to: O₂ meter purchased and tested; bedroom window operable; 4 L LN₂
max on premises; child not in apartment OR supervised by a second adult
outside the lab room with door closed; first three LN₂ runs done with a
recorded video safety-check by Anders or a remote witness on phone. **Do
not do first-ever LN₂ pour without a witness on the phone.** `[B11 §8 — hard
block #2]`

**Cost-of-ownership note (B08 §6c):** at $0.16/kWh NY 2025 residential and
a 7 kW compressor, closed-cycle cryocooler runs $1.12/hr ≈ $27/day
continuous. Typical break-even on a $40k cryocooler vs. LHe is 3–5 years
for a continuous-running bench `[B08 §6c]`. We do not run continuous;
LN₂ refills at ~$10–20/session is the right model at this tier.

---

## 3. Phase-3 stretch (~$10–30 k)

Used cryocooler, OPO bench attempt, tier-2 plasma demos. **None of this
gets ordered until Phase-2 has produced a peer-reviewable measurement.**

| Item | Spec | Vendor | 2025–26 USD | Source brief |
|---|---|---|---|---|
| Sumitomo SRDK-408 cold head | 4 K, 1 W @ 4.2 K | eBay | ~$4 k + $350 ship | B08 §3 |
| Sumitomo RDK-415D cold head, refurbished | – | eBay | ~$7.5 k | B08 §3 |
| Cryomech CP-970 compressor | CP-900 series, water-cooled, 4 kW (needs matching head + chiller; do not buy first) | eBay | $800–1000 used | B08 §3 |
| Complete working 2-stage GM cryocooler (head + compressor + flex lines + chiller) | – | Cryomech / SHI used market | $8–15 k used / $30–80 k new | B08 §3 |
| Pulse-tube cryocooler (preferred over GM — no moving displacer, less vibration) | – | American Instrument (Cryomech PT410), SHI | quote-only / rare used | B08 §3 |
| Mid turbomolecular pump | Pfeiffer HiPace 300, Agilent TwisTorr 84, 250–300 L/s | eBay / LabX | $1.5–3 k used + $300–800 controller | B08 §3 |
| Working Gamma / Varian 60 L/s ion pump | – | Capovani / BMI Surplus | $1.5–4 k used | B08 §3 |
| Full UHV chamber w/ viewports | – | Capovani / BMI Surplus | $5–15 k used | B08 §3 |
| CF flange fittings, gauges, gate valves | "UHV is never just the pump" | – | another $3–5 k | B08 §3 |
| OPO squeezed-light bench (refurbished) | OPO with periodically-poled KTP/LN, balanced homodyne + tomography; PPKTP/PPLN crystal pumped by frequency-doubled stable laser | – | $20–40 k minimum / $100–150 k all-in if refurbished `[B02 §4]` | B02 §4, B09 §2 |
| Used Edwards rotary-vane vacuum pump | for plasma toroid Tier-2 demo | eBay | ~$300 | B06 §3 |
| Borosilicate plasma discharge chamber | ~10 cm dia × 30 cm sealed, custom or surplus | glass shop / surplus | $200–400 | B06 §3 |
| 13.56 MHz ISM-band RF generator (250 W) + manual matching network | unlicensed legal | hobbyist kit / instrument reseller | $1.2 k hobbyist / $3 k+ retail | B06 §3 |
| Ar/Xe gas regulator + cylinder | – | welding-gas supplier | $150 + $50/cylinder | B06 §3 |
| Magnonic film YIG on GGG substrate + microwave loop antenna + VNA + electromagnet pair (alternative phonon-probe analogue) | for Yusra's Stargate-analogue benchtop concept (B05 §4) | university-grade kit | ~$40–80k university-lab pricing | B05 §4 |
| BagelGen xenon plasma toroid kit | 13 cm dia, 15 torr xenon, 12 MHz two-turn PCB inductor — closest cheap Stargate-puddle visual that exists | bagelgen.com / AliExpress | $65 kit / $200 Hackaday "sky-guided PCB edition" | B06 §3 |
| Plug-in plasma globe (toy) | for E1 plasma-globe-in-strong-magnet experiment | Amazon | $25 | B06 §6 E1 |
| Acrylic water flume | 1.2 m clear channel | DIY / Amazon | $300–600 incl. submersible 12V pump, surface-wave generator (offset cam on hobby motor), phone for synthetic schlieren | B05 §6 expt i |
| Soliton-pulse fiber horizon kit (CW telecom laser + commercial ML seed + spool of HNL fiber + borrowed OSA) | – | Thorlabs / eBay used + university OSA loan | $3–5 k all-in if used kit; otherwise out-of-reach | B05 §6 expt ii |
| Magnetic-mirror benchtop (E3) | two opposing N52 ring magnets (or coil pairs) on non-magnetic optical rail, sealed Ar bulb at ~10⁻² torr, DC glow discharge 500–1000 V | scrounge | $600–2500 | B06 §6 E3 |

**Phase-3 total range: $10–30 k for the cold/empty plumbing path
(cryocooler + UHV); separately $20–40 k for the OPO squeezed-vacuum bench;
separately $40–80 k for a magnonic Stargate-analogue benchtop. None of
this is ordered without revenue.**

**Apartment feasibility:** RF / pulsed power above the limits in B11 §1
require renting time at a university lab, not the kitchen table `[B03 §6]`.
A pulse-tube cryocooler on a dryer outlet is feasible only if (a) the lease
permits it, (b) heat can be ducted out, (c) compressor and rotating helium
lines (250 psig charged) are physically inaccessible to a child `[B08 §2]`.
For the OPO bench: ambient T, low vacuum needed beyond optical-cavity
nominal, **viable here** at $50–150k all-in `[B08 §5]`.

---

## 4. Hard NO list

Every item the safety/cryo/QFT briefs said do not buy / do not bring into
this apartment.

**From B11 §8 (safety officer's hard blocks):**
1. **HV pulse capacitor banks (>10 J stored at >100 V).** Chest-path
   discharge = clinical cardiac event; no apartment mitigation survives a
   single muscle slip. Unblocks only at university bench with interlocked
   enclosure, two-person rule, defibrillator on-site.
2. **First-ever LN₂ pour without a witness.** Failure mode: operator
   slips, gets face-full of cold gas + cryogen splash, panics, can't
   reach door. Phone-witness on live call timing the pour is the minimum.
3. **Any laser ≥Class 3B (>5 mW) or any RF source >100 mW in the
   apartment.** Class 3B is direct-beam-blinding-in-aversion-time at 1 m;
   RF >100 mW into a directional antenna can exceed ICNIRP 2020 general-
   public limits at 30 cm without operator noticing (tissue heating).

**From B08 §7 (cryo brief's NOs — apartment cannot do regardless of
motivation):**
4. **UHV bake-out** (10⁻¹⁰ Torr, 150–250 °C / 3–7 days, 500–1500 W heater
   tape on chamber surface). Fire risk on residential surfaces; cannot run
   unattended.
5. **High voltage in tank vacuum >1 kV.** X-ray generation at 5–30 kV
   (Farnsworth fusor, e-beam evaporator, ion accelerators). Requires Pb
   shielding, dosimetry, shielded room. Hard no with child in house.
6. **Pulsed-power coils >100 V or >10 J stored** (B03 §6 reaffirmed by
   B08).
7. **Uncontained LN₂ in main living room.** LN₂ is in kitchen, window
   open, on tray, with O₂ monitor visible. Never on carpet, never in
   closed bedroom.
8. **In-house liquid helium use without an O₂ monitor + active
   ventilation.** LHe boiloff is 745× volumetric expansion. A 10 L LHe
   transfer-loss in a sealed apartment is fatal-class. If ever used here,
   one-shot demo with door open and child at a friend's house, period.
9. **Compressed-gas cylinders unsecured.** Any time we have an N₂ purge
   cylinder or He cryocooler charge bottle, chained to a wall or floor
   anchor (NFPA 55, 29 CFR 1910.101).
10. **Synthesizing YBCO from precursors.** Y₂O₃/BaCO₃/CuO sintering is a
    950 °C tube-furnace process with toxic dust. Buy the disks. NO synthesis.
    `[B03 §6 + B08 §7 agree]`
11. **Mercury for diffusion pumps.** Banned in NY State residential; use
    turbo. **³He fridge apparatus** out-of-scope. **Lithium metal** for any
    BEC variant — flammable in moist air.
12. **Dilution refrigerator** ($300–700 k new; used ~$100–250 k via lab-
    to-lab refurb; not on open market). Out-of-scope. If we need 10 mK,
    we partner.

**From B09 §4 (instrumentation brief — measurement out-of-scope):**
13. **Casimir-force experimental measurement at sub-µm.** Vibration,
    surface roughness, distance metrology all kill it. Apartment is
    broadband at 100 nm level. State explicitly in brief and README that
    Casimir measurement is out-of-scope at apartment scale. Sim renders
    Lifshitz curve only.
14. **BEC analogue experimental measurement.** Cold-atom apparatus is
    >$1M and needs UHV bake-out (NO #4 above). Sim reproduces published
    Steinhauer 2016 g⁽²⁾ from Gross–Pitaevskii integrator only.

**From B06 §4 (plasma brief — fringe physics):**
15. **EmDrive testing or "mode" in sim** — definitively falsified by
    Tajmar 2021 to <0.1 µN at 100 W input. Closed file.
16. **Heim-theory drive demos** — predictive failures catalogued, no
    blind reproduction.
17. **Tajmar gravitomagnetic London-moment** experiments — no successful
    independent replication in 20 years; mainstream consensus = artifact.

**From B11 §5 risk assessments and §3 lessor protection:**
18. **BEC laser-cooling benchtop in apartment** — needs ≥1 W tunable
    Class 3B/4 laser, UHV, kA-range pulsed magnetic-trap coils, reactive-
    metal handling. **NO-GO in apartment, period.** University collaboration
    or doesn't happen. `[B11 §5]`
19. **Ablation experiments in apartment** — sub-µm particulate not
    captured by hood-less work; OSHA PEL solder-flux 0.1 mg/m³ rosin-fume
    threshold matters. Soldering with USB fume extractor OK; ablation is
    NOT. Goes to university bench. `[B11 §1, §5]`
20. **Permanent apartment modifications.** Wall-fixture changes, non-
    portable 240 V equipment installation, anything that fails the GO/NO-GO
    "reversible setup" gate. `[B11 §3, §7]`

**From B08 §1 (cryo's bandwidth-of-the-program note):**
21. **Anything below 77 K** is a partner-lab conversation. The only
    realistic cryo CapEx for the next 12 months is $400 dewar + $200 O₂
    monitor + $1.5k scroll + $1.5k turbo = ~$3.5k for 77 K + HV.

---

## 5. Brief disagreements — explicit

The briefs are mostly aligned but in places present competing views worth
flagging.

- **Integrator choice (B01 vs. B04).** B01 (Hana, GR) wants Hamiltonian +
  symplectic for closed orbits and long traversals; B04 (Tomas, GPU) wants
  classical RK4 in 8D phase space because the geodesic equation is not
  separable canonically once metrics go off-diagonal, and RK4 has better
  accuracy-per-RHS-eval at the precision we need. **Resolution adopted in
  physics_spec.md §1.2:** RK4 as primary GPU runtime path, symplectic
  Yoshida-4 as compute-shader closed-orbit/light-ring mode for stable
  bound orbits. `H = 0` projection in both.
- **MMP throat mass (B02 vs. B10).** B02 §2 puts a 1 m throat at
  `M ~ 10²³ kg` per mouth ("Jupiter's moon Io"); B10 §1 puts it at
  `~10⁷ M_⊕` (Jupiter-mass) with potential reduction to `~10⁵ M_⊕`
  (Saturn-mass) under optimization. Both flagged `[unverified]` against
  primary source in brief. Surface both numbers in MMP scene UI; do not
  pick a single canonical without re-reading 2008.06618 §IV–V.
- **Bulk YBCO vs. tape (B03).** Brief notes one bulk disk is *not enough*
  for a Prat-Camps replica — need a tessellation. Tape is closer to what
  Prat-Camps actually used and is cheaper for tessellation. Phase-2 BOM
  lists both; tape is the recommended buy.
- **Phase-2 fluxgate sufficiency (B03 vs. B09).** B03 §2 says the original
  Prat-Camps demonstration was limited by µT-class fluxgate noise;
  B09 §1 argues that a used Mag-03 in a 3-layer mu-metal can in
  differential-gradiometer mode resolves nT-level residual and *exceeds*
  Prat-Camps's published sensitivity. **Adopt B09's recommendation as the
  decisive Phase-2 measurement spec** — the cost is the same.
- **OPO bench cost (B02 vs. B09).** B02 §4 says $100–150k all-in for a
  refurbished OPO squeezed-light bench; B09 §2 says $20–40k minimum for
  squeezed-vacuum *generation* (OPO with periodically-poled crystal +
  frequency-doubled stable laser). The disagreement is scope: B02 is the
  full bench with detection chain, B09 is the OPO source itself. Phase-3
  line item lists the range honestly.
- **Reconnection-as-topology-change framing (B06).** Internal to B06, but
  worth surfacing: in 2D, reconnection IS topology-change of the field-
  line pattern; in 3D laminar flow, it happens by dissipation; in 3D
  turbulence, "spontaneous stochasticity" makes it fast and resistivity-
  independent. None of these is spacetime topology change. Mandatory
  side-panel disclaimer language must be coordinated with Hana before F2
  ships `[B06 §5, §7 recommended next moves]`.
- **Sycamore wormhole-experiment status (B07 §3, B10 §3).** Both briefs
  agree the Kobrin–Schuster–Yao critique (Nature 638, 2025) largely won
  the technical argument that the specific N=7 instance is not
  holographic. Jafferis et al. 2025 reply argues for "pseudo-holographic"
  framing. We label honestly per anti-feature §5 #11: "holographic
  visualization of quantum-circuit correlations," not "we simulated a
  spacetime wormhole."

---

## 6. Honest bench dollar map

What can be measured at each tier, what cannot.

**Tier 0 — $0.** Sim only. Reproduce published g⁽²⁾ from BEC, Lifshitz
Casimir curve, Müller MT lensing image, Steinhauer thermal Hawking
spectrum. All purely software. Validation is pixel-match against
published figures.

**Tier 1 — $300–500.** Phase-1 magnetic-hose-only replica, Hall-probe
field map, FE-solver sanity check. Resolves: B-field channel through
mu-metal hose, demagnetization tensor, qualitative wormhole-topology
field pattern (monopole-like emergence at far mouth above background).
Does NOT resolve: true magnetic invisibility of the connecting tube
(needs SC).

**Tier 2 — $3.5–5 k.** 77 K + HV bench. Resolves: full Prat-Camps
replica field topology (with SC tape tessellation); benchtop Michelson
phase noise survey at apartment-vibration floor (~10 nm rms at 1 Hz BW,
4× orders away from LIGO strain — don't oversell); FE-solver validation
via Mager 1968 cylindrical-mu-metal shielding factor (±30%); GPSDO-
referenced timing for any coincidence work; magnetic-shielding-effective-
ness chamber (B09 §8 expt B). Does NOT resolve: Casimir-force at sub-µm
(vibration + surface roughness + distance metrology kill it); BEC
sonic horizon (UHV + dilution-fridge chain absent); dynamical Casimir
(needs dilution fridge + SNSPDs); EM-wormhole-at-microwave (open prize,
$5–15 k of materials, but needs RF infrastructure + space we don't have
in apartment).

**Tier 3 — $10–30 k+.** Cryocooler + UHV + OPO bench at apartment scale.
Resolves: HTS critical-current measurement; squeezed-vacuum generation
(if the OPO is built; ANEC accounting calibration data); 13.56 MHz RF
inductive plasma toroid demo `[B06 §6 E2]`; magnetic-mirror confinement
demo `[B06 §6 E3]`. Does NOT resolve: anything requiring sub-K (MMP-style
Casimir-from-BSM-fermions, BEC, qubit coherence, dilution-fridge DCE).
Anything requiring Class 3B+ lasers (BEC laser cooling). Anything
requiring shielded RF room or licensed transmit power.

**What an outside reader should know about scope:** This is a real-physics
visualization tool with a benchtop validation harness, not a wormhole
factory. The simulator computes geodesics, energy-condition tensors, FE
magnetostatic fields, MHD, BEC GP integrators, and SYK/GJW correlators
honestly, and validates against published images and analytic test cases.
The benchtop measures one real, replicable transformation-optics system
(the Prat-Camps magnetic wormhole) and uses it to cross-check the FE
solver. The benchtop does not measure exotic matter, does not produce
ANEC violation, does not transmit anything faster than light, and is
not a spacetime wormhole. The MMP construction is the strongest
existence proof in physics that traversable wormholes are not forbidden
by QFT+GR with sensible matter content; it requires `~10³²` magnetic
monopoles per mouth, `~10⁷ M_⊕` of mass, and BSM fermion species we
have not detected. As a construction blueprint it is untouchable on
every axis. As a teaching scene, it is the highest-pedagogy-per-line
content we ship. "Humanly traversable" is an in-joke about the
tidal-force calculation, not a build directive `[B10 §7]`.
