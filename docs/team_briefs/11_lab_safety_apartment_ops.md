# Brief 11 — Lab Safety SOP for Apartment Ops

**Author:** Capt. Linnea Torres (R11, lab safety officer / former research-lab EHS)
**Audience:** the experimenter (Anthony), anyone Anthony hands a bench to, future contractor / inspector who reads this when something goes wrong.
**Scope:** real research, real apartment, real six-year-old. Vestal NY, second-floor 2BR rental. One occupant adult, one occupant child (Lucia, 6). Lab room is the second bedroom, door-closeable. Shared kitchen is the only ventilated space with an exterior window that opens reliably.

This is not OSHA cargo-cult. The goal is *the document gets followed*, which means: short enough to re-read before every run, conservative where the stakes warrant, pragmatic where they don't.

---

## 1. Hazard Inventory (what we will actually face)

| # | Hazard | Standard / limit | Threat at our scale | Hardware mitigation | Procedural mitigation |
|---|---|---|---|---|---|
| 1 | NdFeB rare-earth magnets (N52, ½–1") | ICNIRP 2009 static-B: 400 mT public, 2 T occupational head/trunk | Field at 10 cm <10 mT; *real* threat is **mechanical** — two 1" cubes snap with ~25 kgf, takes a fingertip | Plastic separators in storage; non-ferrous workbench; tweezers/wood pusher for handling | Never bring two strong magnets within 30 cm of each other off-bench; one magnet on bench at a time during placement; inventoried in locked drawer when not in use |
| 2 | Mu-metal sheet, 0.014" stress-annealed | OSHA 1910.151 first aid; sheet-metal cuts | Sharp burrs; mu-metal degrades on flex (loses µ_r) so re-bending it for cuts is double-bad | Edge tape on stock; cut-resistant gloves (A4 minimum) for handling; deburring tool | Cut once, file edges, store flat. Never let Lucia touch raw stock. |
| 3 | Liquid nitrogen (LN₂), ≤4 L at a time | OSHA: O₂-deficient atmosphere <19.5 % v/v; ACGIH cryogen burn = direct contact | 1 L LN₂ → 694 L gaseous N₂. Lab bedroom ≈ 25 m³. 4 L spilled = O₂ from 20.9 % to ~16 % if room sealed. **Real asphyxiation risk if door+window closed.** Cryo burn on splash, brittle floor under spill. | Open dewar, cryo gloves (loose-cuff leather, not insulated synthetic), face shield, sheet-pan tray under work area, O₂ meter (portable, $150 used) clipped at chest height | LN₂ work only with bedroom window open ≥6", lab door closed, kitchen window cross-vent open, child confirmed in living room or out of apartment. Pour <100 mL/s. ≤4 L on premises ever. |
| 4 | High-current DC supplies (≤30 V, ≤10 A bench) | OSHA 1910.303–.335; NFPA 70E shock-protection boundary <50 V = "low risk" but arc/burn still possible | Arc burn at lead-disconnect under load; thermal burn on coil; battery-fire on shorted lithium pack | Insulated 4 mm banana leads, in-line fuse on every supply, current-limited supply (CC mode), Kapton tape on busbars | Lead-makeup and lead-removal with supply OFF; one-hand rule (right hand only on energized leads, left hand in pocket); fire extinguisher (Class C, dry chem, $30) within arm's reach |
| 5 | RF source — DCE replication ≈ 5 GHz, ≤10 mW | ICNIRP 2020 RF general-public: 10 W/m² (1–10 GHz) whole-body, 30-min average; SAR 0.08 W/kg WB | At 10 mW into a small-aperture horn the near-field exceedance zone is <30 cm. Real risk is *cumulative* if you stand in the beam during alignment. | Aluminum-foil-lined cardboard absorber screen behind device; dummy load on every TX line; spectrum analyzer to confirm out-of-band leakage <-60 dBc | Power-on only with screen up; no operator within 50 cm of transmit aperture; never operate above 10 mW until band/license reviewed (FCC Part 15 unintentional radiator territory) |
| 6 | Laser pointers / He-Ne ≤5 mW, 633 nm | ANSI Z136.1-2022: Class 3R = ≤5 mW visible CW; MPE for 0.25 s aversion blink ~25 W/m² | Direct intra-beam exposure >0.25 s causes retinal burn. Specular reflection off metal optics is the realistic threat. | Class-3R-rated goggles for the wavelength in use (OD 2+ at 633 nm); beam blocks (anodized Al posts); matte-black bench cloth | Beam height ≤bench height (waist-high, never head-high); remove watches/rings before alignment; eyes never below beam line; door closed + "LASER ON" sign during alignment; no Class 3B+ ever in this lab |
| 7 | Tabletop optics (HeNe, mirrors, BS) | ANSI Z136.1-2022 — stray reflections | A spec of dust on a steering mirror at 5 mW is enough to reach MPE on a 1 s glance | Beam-tube enclosures where possible; iris on every optical path; black-anodized post bases | Two-person rule waived for ≤5 mW; one-person rule with door-closed + audible alarm OK; alignment cards (IR sensor / fluorescent) instead of paper-and-eyeball |
| 8 | HV pulse capacitors | NFPA 70E; IEEE C95 | **Hard NO at our scale.** Energy-stored (½CV²) >10 J at >100 V is the line where a discharge across the chest is a clinical event, not a pinch. | n/a — see §8 | n/a |
| 9 | Smoke / particulate (laser ablation, flux, soldering) | OSHA PEL solder-flux 0.1 mg/m³ rosin-fume | Hand-soldering with rosin flux is fine in open air; ablation is NOT — sub-µm particulate, not captured by hood-less work | Soldering: USB fume extractor + activated carbon ($40) within 15 cm of joint. Ablation: NOT in apartment. | Soldering only with extractor on; ablation experiments require university bench-time |

---

## 2. Child-Protection Layer

Lucia is six. Six-year-olds are bright, fast, curious, and have terrible risk perception by design. Procedure not luck.

**Hard rules.**
1. **Hazard runs only when Lucia is not home, OR is asleep with the lab door closed and labelled, OR is in a different room with a closed door and a babysitter/Anthony's-eye-line on her.** "Hazard run" = LN₂ open, RF transmitting, laser energized above Class 2, DC supply >30 V active, OR any first-time-this-config run. Cold-bench work (CAD, soldering small DC, magnet placement <½" cubes) does not require this.
2. **No live experiments in shared living space when she is home and awake.** The lab room exists for a reason. Shared spaces (kitchen, living room) revert to non-lab use as soon as a session ends — no half-built rigs left on the dining table.
3. **Locked storage** for: NdFeB magnets >½", LN₂ dewar (when full), laser, exposed HV components if any get acquired. A $20 toolbox with a padlock is sufficient — the threat model is "Lucia opens a drawer to look," not a determined adversary.
4. **Hazard zones** in a 2BR apartment:
   - **Red zone** = lab room during a hazard run. Door closed, sign on the door ("LAB IN USE — DO NOT ENTER — CALL FIRST"). She knocks, waits, never enters.
   - **Yellow zone** = lab room between runs. Powered down, locked drawers locked, door closable. She can enter only with Anthony.
   - **Green zone** = rest of apartment. Always non-lab.
5. **Teach, don't only forbid.** A six-year-old who has been shown what a magnet does to a steel washer ("watch how hard it pulls — that's why we don't put fingers near it") complies better than one who's only told no. Teach the *why*, age-appropriate, and re-teach after every config change. Show her the LN₂ vapor cloud from across the kitchen — once. Never let her near it lit.

---

## 3. Lessor-Protection Layer

Anthony rents. The lease and the renter's insurance policy are the binding documents; this SOP works inside them.

- **Renter's insurance:** typical NY policy covers personal property to ~$15–30k and liability to ~$100k. It **does not** cover business operations or lab equipment as such — declared scientific equipment may need a rider. Action: read the policy this month, add a rider for ≥$10k of lab kit if the carrier offers it. If they refuse, that's a signal not to escalate the kit count.
- **Electrical:** standard residential branch circuits in NY are 15 A or 20 A at 120 V. NEC/NFPA 70 §210.20(A) limits *continuous* load to 80 % of breaker rating: 12 A on a 15 A circuit, 16 A on a 20 A circuit. Lab bench draws (DC supply + computer + soldering iron + lights) should stay under 10 A on a single circuit. **Map the apartment's circuits before running anything that draws >5 A.** A $30 plug-in circuit-tracer pays for itself the first time you trip a breaker mid-experiment.
- **Fire detection:** confirm working smoke alarm in lab room AND adjacent hallway. Add a **CO + smoke combo alarm** ($25) in the lab room independent of the building system — no soldering / cryogenic / electrical work without it. Test monthly.
- **Particulate / smoke from ablation:** *do not do ablation experiments in this apartment.* Those go to a university bench. Soldering and small ferrite-cutting with a fume extractor are fine.
- **Floor protection:** LN₂ on hardwood = thermal-shock mark = lessor charge at move-out. Sheet-pan tray under all cryogen work. ABS/PE drop cloth ($15) under the magnet bench prevents impact dings if a magnet pair snaps loose.
- **Landlord notification:** at our current scale, **no notification required** — this is "a person doing electronics and physics hobby work in a bedroom," indistinguishable from "a software engineer with a 3D printer." Notification *would* be required if we ever: store ≥10 L LN₂, install non-portable 240 V equipment, modify wall fixtures, or operate any RF source outside FCC Part 15 limits.

---

## 4. Standard Operating Procedures

### 4.1 Pre-run checklist (every hazard run, no exceptions, signed in lab notebook)

- [ ] Lucia status confirmed (location, awake/asleep, supervised by whom)
- [ ] Lab door closable, sign posted
- [ ] Window open per hazard (LN₂ → ≥6"; RF → no requirement; laser → closed for stray-light)
- [ ] O₂ meter reading ≥20.5 % at start of run (LN₂ runs only)
- [ ] Fire extinguisher within 2 m, charge gauge in green
- [ ] Phone charged, on bench, not in pocket
- [ ] Single-task focus: no music with lyrics, no parallel debugging on the laptop
- [ ] Dead-man timer set (kitchen timer, 30 min default — forces a re-check)
- [ ] PPE on body, not on shelf

### 4.2 In-run monitoring — one-person rule

The honest answer for an apartment lab with a child in the next room: a true two-person buddy rule isn't available. We substitute:
- Phone-on-bench with one trusted contact pre-dialed (text "starting LN2 run, ETA 30 min" before; "done" after; if that text doesn't arrive in 45 min the contact calls, then 911).
- Dead-man timer — every 30 min you must reset it. If it expires you stop and re-check yourself, the room, the experiment.
- Audible alarms on: O₂ meter, smoke alarm, RF leakage detector if used. Eyes can be wrong; ears are harder to fool.
- Door-closed-from-inside is **never** locked from inside (Lucia / EMS access). Sign on door, knob unlocked.

### 4.3 Per-hazard procedure

**Magnet handling:** unbox one magnet at a time on a non-ferrous bench. Steel hand tools stay >50 cm away. Two magnets together only via a controlled-approach jig (acrylic block with channels). After placement, label every magnet's location on the device with tape. Never store loose in a pocket — the field reaches your phone, your card, your pacemaker (none of us, but the principle).

**LN₂ fill / transfer:** dewar on the floor, on a tray. Face shield + cryo gloves + closed-toe shoes + cotton/wool long sleeves (synthetics melt). Pour slowly, ≤100 mL/s, into a pre-cooled receiver — a room-temperature glass receiver will shatter from thermal shock. After fill, cap dewar, return to ventilated storage spot (corner of lab room near window). Used LN₂ evaporates in place; never pour down a drain (P-trap freeze) or into a sealed container (pressure burst).

**HV / DC supply:** lead-makeup OFF. Visual continuity check (multimeter on resistance, not on the live circuit). Power on at lowest setting, ramp. CC mode if available. Lead removal OFF. Discharge any capacitor >1 µF >10 V with a 10 kΩ bleeder for 5 τ before touching.

**Laser alignment:** goggles ON before laser ON. Beam height ≤bench top. Use IR/fluorescent alignment cards, not paper and eye. Block specular reflectors (use matte mounts). One steering mirror at a time. Hands stay below beam line. Door closed, "LASER IN USE" sign on door. He-Ne off when not actively aligning — these tubes don't like thermal cycling but they like "left on overnight" even less.

### 4.4 Post-run secure-and-store

Power down in reverse of power-up. Verify zero current/voltage on supplies before disconnect. Cap LN₂ dewar (loose cap — never airtight). Magnets back to locked drawer with separators. Optics covered with lens tissue + dust cap. Lab notebook entry: what you did, what you saw, what surprised you, what you'd do differently. Door closed, sign down (or flipped to "OFF").

---

## 5. Experiment-Specific Risk Assessments

**Phase-1 mu-metal magnetic wormhole replica (no SC).** Hazards: (1), (2). Both manageable. **GO.** Can be set up on the dining table for daytime work when Lucia is at school, broken down at end of session. Field external <10 mT at any accessible point; mu-metal edge-taped. Insurance / lessor concern: zero.

**Phase-2 Prat-Camps full replica with YBCO + LN₂.** Hazards: (1), (2), (3). LN₂ is the gating risk. **CONDITIONAL GO** subject to: O₂ meter purchased and tested; bedroom window operable; 4 L max on premises; child not in apartment OR supervised by a second adult outside the lab room with door closed; first three runs done with a recorded video safety-check by Anders or a remote witness on phone. **Do not do first-ever LN₂ pour without a witness on the phone.**

**Casimir-attempt benchtop.** As actually described in Brief 02, a real Casimir measurement is a $50 k+ AFM-on-vibration-isolation problem. A *demonstration* (parallel plates, capacitance shift) is thinkable at <$500. Hazards: (4) low-V DC, (1) magnets if used for piezo drive. **GO** for the demonstration scale; **NO-GO** for a metrologically-real measurement (out of apartment-vibration scope, period — neighbors walking on the floor above will swamp pN-scale signals).

**BEC laser-cooling benchtop.** This requires: ≥1 W tunable narrow-linewidth diode laser (Class 3B/4), ultra-high vacuum (≤10⁻⁹ torr, turbo pump on glass cell), magnetic-trap coils (kA-range pulse), Rb/Sr/Yb getter source. Capital ≥$100 k, hazards (5),(6),(8) all elevated, vacuum-implosion risk, reactive-metal handling. **NO-GO in apartment, period.** Yusra's brief 05 already says BEC is out of scope for us. This SOP makes it formal: BEC laser-cooling is a university-collaboration path or it doesn't happen.

---

## 6. Incident Response (template — customize and post on lab door)

**Before any incident: post on lab door, a single laminated card with:**
- Anthony's mobile · trusted-contact mobile · 911
- Apartment address (full, with apt #) and intersection landmarks
- Building manager / super phone
- Poison Control: **1-800-222-1222** (US national)
- Nearest ER: [fill in — e.g. UHS Wilson Medical, Johnson City]
- Location of breaker panel; location of fire extinguisher; location of O₂ meter

**Cryogen spill (LN₂):**
1. Step back. If splashed on skin: do **not** rub; flush with lukewarm (not hot) water for 15 min.
2. Open window fully, open door, leave room. Wait for O₂ meter to read ≥20.5 % before re-entry.
3. If the spill is on flooring: do not pick up frozen material with bare hands. Let it boil off (minutes).
4. If a person is unresponsive: 911, do not enter the room until ventilated.

**Magnet finger-pinch:**
1. Don't try to pull the magnets apart with brute force — slide them off each other (lateral, not normal).
2. If a fingertip is between them: slide a thin plastic shim (credit card) from the side, lever them apart.
3. Crush injury → ER. A pinched fingertip is rarely "just bruised" with N52s.

**Electrical shock:**
1. Don't touch the victim directly if still in contact with the source. Kill power at the breaker panel first.
2. 911. Cardiac monitoring is required even after a "small" shock if the path was hand-to-hand or hand-to-foot.
3. Burn at contact point: dry sterile dressing, ER for evaluation.

**Fire (electrical / lithium / general):**
1. If small (<frying-pan size), Class C extinguisher, sweep base of flames.
2. If lithium battery: do **not** use water. Smother with a metal lid or sand. Evacuate; lithium fires re-ignite.
3. >small: leave, close door behind you, pull alarm on the way out, 911 from outside. Get Lucia first, then yourself, then nothing.

**Child present during any incident:** her safety is the only priority until paramedics arrive. The experiment is replaceable; she isn't.

---

## 7. GO / NO-GO Gating

Every experiment must clear all four:

```
   ┌─────────────────────────────────────┐
   │  (a) Hazard within tolerance?       │ ──no──> NO-GO (engineer the hazard down or skip)
   └─────────────────┬───────────────────┘
                    yes
   ┌─────────────────▼───────────────────┐
   │  (b) Child safe?                    │ ──no──> NO-GO (reschedule)
   │      (location/supervision verified)│
   └─────────────────┬───────────────────┘
                    yes
   ┌─────────────────▼───────────────────┐
   │  (c) Reversible setup?              │ ──no──> NO-GO (no permanent apartment mods)
   │      (lab broken down end of day)   │
   └─────────────────┬───────────────────┘
                    yes
   ┌─────────────────▼───────────────────┐
   │  (d) Measurable outcome?            │ ──no──> NO-GO (define the measurement first)
   │      (what number ends the run?)    │
   └─────────────────┬───────────────────┘
                    yes
                  ─── RUN ───
```

Gate (d) is non-negotiable: if you can't write down "we will measure X to ±Y and the run ends when we have Z data points," you're playing, not experimenting, and the hazard is not justified.

---

## 8. Three Things I Block Immediately

1. **HV pulse capacitor banks (>10 J stored at >100 V).** Why: a chest-path discharge at this energy is a clinical cardiac event. There is no mitigation procedure that survives a single muscle slip in a bedroom lab. **Unblocks when:** moved to a university bench with interlocked enclosure, two-person rule, defibrillator on-site.
2. **First-ever LN₂ pour without a witness.** Why: the failure mode is "operator slips, gets a face-full of cold gas + cryogen splash, panics, can't reach door." A phone-witness who knows where you are and is timing the pour is the minimum. **Unblocks when:** Anders or a remote witness is on a live call for the duration of the first three pours, plus an O₂ meter is on the bench.
3. **Any laser ≥Class 3B (>5 mW) or any RF source >100 mW in the apartment.** Why: Class 3B is direct-beam-blinding-in-aversion-time at 1 m; RF >100 mW into a directional antenna can exceed ICNIRP 2020 general-public limits at 30 cm and you don't notice until you've been heating tissue for an hour. **Unblocks when:** laser → enclosed laser system with interlocked beam path + signed risk assessment, never with Lucia in the apartment. RF → moved to anechoic / Faraday space (university), or licensed and metered.

---

## 9. Citations

- **OSHA 29 CFR 1910.146** — Permit-required confined spaces. Defines O₂-deficient atmosphere as <19.5 % v/v. https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.146
- **OSHA 29 CFR 1910.151** — Medical services and first aid. https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.151
- **OSHA 29 CFR 1910.303–.335** — Electrical safety, general industry. https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910SubpartS
- **OSHA Liquid Nitrogen guidance** — 1 L LN₂ → 694 L gaseous N₂ expansion ratio, asphyxiation hazard in unventilated spaces. https://www.co2meter.com/blogs/news/liquid-nitrogen-safety-requirements-osha
- **NFPA 70 (NEC) §210.20(A)** — Branch-circuit overcurrent protection: continuous load ≤80 % of breaker rating. https://up.codes/s/continuous-and-noncontinuous-loads (paraphrased; full text in the licensed NEC).
- **NFPA 70E** — Standard for Electrical Safety in the Workplace. Shock-protection boundary distinctions <50 V vs ≥50 V. [unverified specific edition — verify against 2024 ed. before quoting; principle is current]
- **ANSI Z136.1-2022** — American National Standard for Safe Use of Lasers. Class definitions, MPE tables, Class 3R ≤5 mW visible CW, Class 3B AEL 0.5 W (315 nm–far IR). https://blog.ansi.org/ansi/ansi-z136-1-2022-safe-use-of-lasers/
- **ICNIRP 2009** — Guidelines on limits of exposure to static magnetic fields. Public 400 mT, occupational 2 T head/trunk / 8 T limbs. https://www.icnirp.org/en/frequencies/static-magnetic-fields-0-hz/
- **ICNIRP 2020** — Guidelines for limiting exposure to electromagnetic fields (100 kHz–300 GHz). Whole-body SAR public 0.08 W/kg, reference level 10 W/m² in 1–10 GHz, 30-min average. https://www.icnirp.org/cms/upload/publications/ICNIRPrfgdl2020.pdf
- **Poison Control (US)** — 1-800-222-1222, 24/7. https://www.poison.org/
- **NIH ORS Oxygen Monitoring Protocol** (operational template for O₂ meter use around cryogens). https://ors.od.nih.gov/sr/dohs/Documents/protocol-for-use-and-maintenance-of-oxygen-monitoring-devices.pdf

[unverified] markers above call out where I'm pointing at a current-edition principle without having the edition cite-checked this session. The principles hold; the section/edition numbers should be verified before any audit context.

---

— Linnea
