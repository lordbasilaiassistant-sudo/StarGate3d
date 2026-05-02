# Brief 08 — Cryogenics & Ultra-High Vacuum: What a Renter Can Actually Reach

**Author:** Dr. Anders Holm (cryogenics / UHV / instrument plumbing). R8.
**Audience:** StarGate3d sim + bench team.
**Status:** Working brief. Prices are 2025–2026 USD; verify at quote time.
**Scope discipline.** Vance (Brief 03) costs the YBCO + LN₂ stack for the magnetic wormhole. Chen (Brief 02) costs the *physics* benches (Casimir, OPO, DCE). I do not re-cost those. I cost the **infrastructure** — the cold-and-empty plumbing under every credible exotic-matter experiment — and decide which of it is reachable from a Vestal NY apartment with no payroll, a six-year-old in the house, and no university affiliation.

---

## 1. The temperature ladder and the vacuum ladder, with what each unlocks

Two independent axes. Most experiments need a point on each.

### Temperature

| Tier | T (K) | Apparatus | All-in cost (used / new) | What it unlocks | Killed without it |
|---|---|---|---|---|---|
| Ambient | 295 | none | $0 | room-T squeezed light (OPO bench), MEMS-Casimir at µm separations, water-flume analogue gravity | superconductivity, BEC, dynamical Casimir |
| Dry ice | 195 | foam cooler | $5 | thermal noise reduction on optics; nothing exotic | YBCO not yet cold |
| LN₂ | 77 | dewar + transfer | $300 dewar + ~$1–3/L LN₂ | YBCO superconductivity (Tc=92 K), low-noise CCDs, IR detector cooling, magnetic-wormhole replica | sub-77 K SC physics, BEC, mK qubits |
| LHe (pumped) | 1.2–4.2 | bath cryostat + helium plant access | LHe **$30–60/L** in 2025, single-shot bath ~$100–500 per cooldown | LTS magnets, traditional Casimir torsion-pendulum at low thermal noise, hot-electron bolometers | sub-K coherence, dilution physics |
| Cryocooler (GM/PT) | 2.8–4 (2-stage) | closed-cycle, He compressor + cold head | **$5–15k used / $30–80k new** | LHe-equivalent without consumables; superconducting cavities for DCE-style work; YBCO Jc-limited regimes | nothing below 2.8 K without a sub-K stage |
| ³He fridge | 0.25–0.3 | sorption/closed-cycle ³He insert | $20–60k used; ³He gas itself ~$2–5k for charge | low-noise calorimetry, single-photon SC detectors | mK qubit coherence times |
| Dilution fridge | 0.007–0.020 | ³He/⁴He DR (Bluefors LD, Oxford Triton) | **$100k used (rare) / $300–700k new** | superconducting qubit experiments, dynamical Casimir on SQUID-cavity (Wilson 2011 regime), mK Casimir | nothing below ~250 mK |
| Adiabatic demag (ADR) / nuclear demag | 0.05 → µK | one-shot magnet + paramagnetic salt | $30–80k used | sub-mK thermodynamics, anomaly hunts | continuous operation |

**Reachable without a tier upgrade:**
- *Without LHe:* you can still measure the **static Casimir force** at 295 K (Lamoreaux-class torsion or MEMS), demonstrate squeezed vacuum in an OPO bench, run a magnetic-wormhole replica, and operate water-flume / fiber-optic analogue-gravity demos.
- *Without sub-K:* dynamical Casimir in superconducting circuits dies (it lives at ~10–50 mK), and any BEC dies (atoms condense at ~µK, but the **dilution fridge or laser cooling chain is what gets you there**).

### Vacuum

| Tier | Pressure (Torr) | Pump | All-in cost | What it unlocks |
|---|---|---|---|---|
| Rough | 10⁻¹ – 10⁻³ | rotary-vane oil pump, scroll, **or DIY fridge compressor** | $50 DIY / $200 used / $400 new (scroll) | LN₂ dewar pre-evacuation; vacuum insulation; coarse Casimir at ~µm where 10⁻³ Torr is fine if plates aren't reactive |
| High | 10⁻⁴ – 10⁻⁶ | turbomolecular pump backed by rough | $400 used (small) / $2–4k mid / $8k new | most Casimir work, optics chambers, cryostat insulation vacuum |
| Very high (HV) | 10⁻⁷ – 10⁻⁸ | turbo + bake + ion gauge | $3–8k used | residual-gas-sensitive surfaces, low-outgassing optics |
| UHV | 10⁻⁹ – 10⁻¹¹ | ion pump + Ti sublimation + bake-out | $20k+ used, $80k+ new | atomic-physics MOTs (Rb BEC needs ~10⁻¹⁰), surface-clean Casimir at sub-100 nm, electron-beam work |
| XHV | <10⁻¹² | NEG + ion + cryopumping | $100k+ | not us. Ever. |

**Crosswalk to Chen Brief 02 §4 experiments:**
- *Static Casimir, µm range:* ambient T + 10⁻⁴ Torr. **Both reachable.**
- *MEMS-Casimir (Decca-class, sub-µm):* ambient T + 10⁻⁷ Torr + low-vibration. **HV reachable; vibration is the harder problem.**
- *OPO squeezed-vacuum bench:* ambient T, no vacuum needed beyond optical-cavity nominal. **Reachable.**
- *Dynamical Casimir (Wilson 2011):* 20 mK + 10⁻⁶ Torr inside the IVC. **Not reachable without a DR.**
- *BEC analogue horizon (Steinhauer):* ~µK + UHV (10⁻¹⁰ Torr). **Not reachable.**
- *Casimir torque / birefringent plates:* ambient + HV. **Reachable.**

So three of the six benches in Chen's table are reachable in principle from this apartment with $5–30k of infrastructure. The other three need a university lab or a partnership.

---

## 2. Apartment realism — operating safely with a six-year-old

The hazards are not theoretical. Real numbers, real exposure limits.

**LN₂ asphyxiation.** 1 L LN₂ → 696 L gaseous N₂ at room T (NIST/CGA). OSHA 29 CFR 1910.146 defines O₂-deficient atmosphere as <19.5%; below 16% causes impaired judgement, below 12% unconsciousness in minutes (Compressed Gas Association P-39, U.S. CSB Bulletin 2003-10-B). Vestal apartment kitchen volume ~30 m³. A 4 L dewar boiloff in a sealed kitchen is ~2.8 m³ of gas — drops O₂ from 20.9% to ~19.0%, *just* below OSHA threshold. **Mandatory:** open window + open interior door = >5 air-changes/hr; child not in same room during transfers; wall-mounted O₂ monitor (~$200, e.g. Macurco OX-6 or Forensics Detectors O2-300) with audible alarm at 19.5%.

**Cryogenic burns.** LN₂ contact with skin is ~−196 °C. Boiling-induced Leidenfrost protects briefly, but trapped LN₂ (in a cuff, glove, or shoe) defeats the film and causes deep frostbite in seconds. **Loose-fitting cryo gloves** (not insulated synthetic — leather or cryo-rated; e.g. Tempshield Cryo-Gloves, $50–80), **face shield** (not just safety glasses), pants over shoes, no rings/watches.

**Floor.** Hardwood + LN₂ = thermal-shock spalling and a permanent mark — losing the security deposit. Use a stainless tray on a silicone mat; spills go into the tray. Carpet is worse (fiber shatters cold and abrasively).

**Cryocooler electrical.** Sumitomo / Cryomech compressors are 200 V single-phase or 208/230 V split. A US apartment normally has 120 V outlets and one 240 V dryer/range circuit. Running a CP-970 or CSW-71 from a dryer outlet works (with an electrician's blessing) but the compressor draws **5–7 kW continuous** and dumps that into a water-cooled head. Air-cooled variants exist but vent ~3 kW of heat into the room — unbearable in summer. **A pulse-tube on a dryer outlet is feasible only if (a) the lease lets you, (b) the heat can be ducted out, and (c) the compressor and rotating helium lines are physically inaccessible to a child.** The lines run at 250 psig charged; a pinch point on a flex line is a real hand-injury risk.

**Oil-mist from rough pumps.** Rotary-vane oil pumps (the cheap rough-pump default) emit a fine oil aerosol from the exhaust under load. Not a child-safe room without an oil-mist eliminator (~$80, KF25 inline) or a switch to oil-free **scroll pump** (~$1.5k used Edwards XDS-5 / Agilent IDP-3). I recommend the scroll. Oil mist + apartment HVAC return = bad.

**Static magnetic field.** Already covered by Vance (ICNIRP 2009 — 400 mT public limit). I won't re-litigate.

---

## 3. Used-equipment market — where to actually shop, with 2025–2026 prices

**Cryocoolers.** eBay carries Sumitomo and Cryomech parts more reliably than dedicated resellers. Verified listings late 2025:
- Sumitomo SRDK-408 cold head (4 K, 1 W @ 4.2 K): **~$4,000** + $350 shipping (eBay).
- Sumitomo RDK-415D cold head, refurbished: **~$7,500** (eBay).
- Cryomech CP-970 compressor (CP-900 series, water-cooled, 4 kW): **$800–1,000** used, but **needs a matching cold head and a chiller**. Don't buy the compressor first.
- A *complete* working 2-stage GM cryocooler (head + compressor + flex lines + chiller) **realistically lands $8–15k used**. New is $30–80k from SHI Cryogenics or Cryomech. (American Instrument lists a Cryomech PT410 used; quote-only.)
- **Pulse-tube specifically** is preferred over Gifford-McMahon for our purposes because the cold head has no moving displacer — much less vibration into the cryostat — but used pulse-tubes are rarer than GMs by ~3:1.

**Turbomolecular pumps.** eBay and LabX both have deep inventories. Verified bands:
- Small turbo (e.g. Pfeiffer TPU 062, Edwards EXT 70, ~70 L/s): **$200–500** used, working.
- Mid (e.g. Pfeiffer HiPace 300, Agilent TwisTorr 84, 250–300 L/s): **$1,500–3,000** used.
- Controller is an extra **$300–800** if not bundled — *always confirm a working controller is included*; orphan turbos are coffee tables.
- Pfeiffer Vacuum and Agilent dominate listing counts (~320 and ~180 active eBay listings respectively as of late 2025).

**Ion pumps & UHV chambers.** Capovani Brothers (capovani.com) and BMI Surplus (bmisurplus.com) carry these; LabX aggregates. Working Gamma / Varian 60 L/s ion pumps run **$1.5–4k used**; full UHV chambers with viewports run $5–15k used. **You will pay another $3–5k in CF flange fittings, gauges, gate valves before pumping down.** UHV is never just the pump.

**LN₂ supply.** Local welding-gas suppliers (Airgas, Praxair/Linde) sell LN₂ at **$0.50–1.78/L** in bulk delivery, **$2–5/L** in 10–50 L dewars (Banagee 2025 survey, Rutherford & Titan 2025 USA price page). Minimum-order fees $50–150. A Cryofab CL-10 10 L dewar runs $400–600 new; used are common on eBay at $150–300.

**LHe.** $30–60/L (Physics Today 2024–25 surveys; Northwestern reported $30/L, U-Crete $49/L). **Single-shot LHe budget for a bath cryostat experiment in this apartment is ~$300–500 per cooldown for ~8 L.** That is sustainable for 1–2 demonstration runs. It is not sustainable for a research program; that's why a closed-cycle cryocooler is the right purchase if we go below 77 K at all.

**Dilution refrigerator.** Bluefors LD/SD and Oxford Triton are the market. New $300–700k. Used dilution fridges essentially do not appear on the open market — they are sold lab-to-lab or by Bluefors/Oxford under refurbishment programs at $100–250k. **Out of scope for this apartment.** If we need 10 mK we partner.

---

## 4. Bench-build path — what to make vs. buy

**Build, gladly.**
- **Rough vacuum from a refrigerator compressor.** Real, established hobbyist technique (Stephen Hansen, *The Bell Jar*, belljar.net "Vacuum on the Cheap" page; Instructables/YouTube tutorials are derivative of his work). Ultimate pressure ~0.1 Torr (29.5 inHg gauge), good enough for cryostat insulation vacuum and pre-evacuation of any HV chamber. Cost: a discarded fridge ($0) + KF fittings + an oil trap. **Caveat:** the compressor isn't designed for sustained vacuum service; oil vaporizes after a few hours, the motor overheats. Treat as a *roughing* pump on duty cycle, not a continuous fore-pump.
- **3D-printed vacuum chamber for HV (10⁻⁵ Torr).** PETG/Nylon prints with epoxy gaskets reach ~10⁻⁴ Torr. 6061 aluminum on a $2k benchtop CNC reaches HV. **Outgassing of plastics caps you at HV; UHV requires bakeable metal.**
- **Insulating dewar from nested SS Thermos flasks** for bench LN₂ work where the commercial dewar is overkill (small samples).
- **Helmholtz coil pair** for residual-field cancellation (Earth's 50 µT) — trivial copper-wire build, $50.

**Buy, no debate.**
- **Turbomolecular pump.** A used Pfeiffer/Edwards/Agilent at $400–2k beats any DIY. There is no hobbyist turbo build that works; the bearings are 60–90 krpm magnetic-suspension or oil-lubricated precision parts.
- **Ion pump.** Same story.
- **Cryocooler.** Stirling/pulse-tube heads exist as DIY in *theory* (free-piston Stirling demos hit ~110–150 K with $5k of parts; see ScienceDirect S0140700720301675 and Refport FPSC datasheets) — but ~77 K is the floor for hobbyist Stirling. DIY 4 K is a multi-year mechanical-engineering project and a bad use of our time. **Buy used.**
- **Pressure gauges (Pirani, ion, capacitance manometer).** Buy used.

**Stretch DIY:** a free-piston Stirling at ~110 K from a Twinbird/Sage/Sunpower-derived prototype ($3–5k of parts + machine-shop time) buys us LN₂-equivalent cooling without LN₂ logistics. Not a priority — LN₂ is cheap and works — but a real project for a future student.

---

## 5. Where each Chen-Brief experiment hits a wall on cheap-tier infra

**Cheapest credible Casimir-force measurement (parallel-plate or sphere-plate, sub-µm):** Lamoreaux 1997-class torsion pendulum, with a *commercial MEMS accelerometer* readout (arXiv:1810.09295, $30 chip + Arduino) instead of a fiber interferometer. All-in $2–5k of optics + $1k vacuum + $200 vibration isolation pad. Gets you 1–10% precision at 1 µm. **Walls hit:** vibration (apartments shake at 1–10 Hz from foot traffic and HVAC; sub-µm separation requires <0.1 nm/√Hz isolation, achievable with a passive air-table, ~$3k used). Thermal drift between plates limits precision below ~0.5 µm.

**BEC-analogue horizon:** Steinhauer-class needs Rb MOT + UHV (10⁻¹⁰ Torr) + dilution-fridge-or-laser-evaporation to ~µK. **Cheapest credible academic MOT** is ~$25k (Olszewski 2011); open-source DIY MOT is ~$8k (OpenQuantum 2023, diyphysics.com). But a MOT alone is not a BEC — getting from cold-trapped to condensed costs another factor of 5–10 in apparatus, and **the chamber UHV bake-out at 200–250 °C for 3–7 days is where this collapses for an apartment** (see §7).

**Magnetic-wormhole replica (Prat-Camps):** Vance has it costed at $2–3.5k. Cryo cost is one $300 dewar + ~$30 of LN₂ per session. **No wall here at the cheap tier.** It works.

**Dynamical Casimir / Wilson 2011 SQUID:** dilution fridge + microwave low-noise amplifiers + qubit-grade microwave sources. Floor is **$200k of secondhand kit and a partner lab** to run it. Not viable in this apartment.

**Squeezed-vacuum OPO bench:** ambient T, low vacuum needed, **viable here** at $50–150k all-in (Chen Brief 02). The cryo/vac infrastructure cost rounds to zero.

---

## 6. Three simulator features (math + UI)

**6a. "Lab Budget" mode.** A drag-in component palette: `LN2_dewar`, `cryocooler_PT410`, `roughpump_DIY`, `turbo_pfeiffer_HiPace80`, `ionpump_60Ls`, `chamber_3DP`, `chamber_CF6`, `vibration_isolation_passive`, `MEMS_accel`, `OPO_bench`. Each component carries (`T_min`, `P_min`, `bandwidth`, `cost_used`, `cost_new`, `power_W`, `noise_floor`, `apartment_safety_flag`). The user composes a stack; the sim greys-out experiments whose `T_required` or `P_required` is unmet and lights up those that are. UI: left panel = component shelf with prices; centre = bench schematic; right panel = "Experiments unlocked" with photo and a link to the relevant arXiv. Math: experiment unlocks iff `T_stack ≤ T_exp_max AND P_stack ≤ P_exp_max AND vib_stack ≤ vib_exp_max AND budget_total ≤ user_budget`.

**6b. Vacuum pump-down curve simulator.** Real Knudsen-aware physics, not the textbook exponential-only approximation. Three regimes:
- *Viscous* (Kn < 0.01): dP/dt = −(S_eff/V)·P, exponential. S_eff = S_pump · (C / (C + S_pump)) with C the conductance of connecting tube.
- *Transitional* (0.01 < Kn < 10): interpolated between viscous and molecular per Knudsen's empirical tube-conductance correction.
- *Molecular* (Kn > 10): dP/dt = −(S/V)·(P − P_outgas), with **P_outgas = q·A/S** dominating once P drops below ~10⁻⁶ Torr. Outgassing rate q is per-material (stainless 10⁻⁹ Torr·L/s/cm² unbaked, 10⁻¹² baked; viton 10⁻⁷; PETG print 10⁻⁵).
- Kn = λ/D, with λ = k_B·T / (√2·π·d²·P), molecular diameter d for N₂ ≈ 3.7×10⁻¹⁰ m.

UI: log-log P(t) plot, draggable "leak rate" and "outgassing surface area" sliders. The crossover from exponential to outgassing-floor is the pedagogical money shot — it's *the* reason UHV needs bake-out.

**6c. Cryogen consumption simulator.** Two modes:
- *Bath cryostat boiloff:* dV/dt = (Q_load + Q_radiation + Q_conduction) / (ρ·L_v). For LN₂: ρ·L_v = 161 kJ/L. For LHe: 2.6 kJ/L. Show "L per day" and "$ per day" with the user's cryogen unit price. Default Q_radiation from a 30 K shield at 4.2 K bath ≈ 0.05 W per cm² of cold surface; conduction Q via supports user-specifies (G10 at A/L geometry, k(T) integrated).
- *Closed-cycle cryocooler:* no cryogen consumption, but show **electricity cost** = P_compressor · t · ($/kWh). At $0.16/kWh (NY 2025 residential) and a 7 kW compressor, that's $1.12/hr ≈ $27/day continuous. Compare side-by-side with the LHe-bath cost on a "months to break-even" plot. (Typical break-even on a $40k cryocooler vs. LHe is ~3–5 years for a continuous-running bench — match Northwestern/UF figures.)

---

## 7. Hard NO list — things this apartment cannot do regardless of motivation

1. **UHV bake-out.** Reaching 10⁻¹⁰ Torr requires baking the chamber at 150–250 °C for 3–7 days continuous, with heater tape drawing 500–1500 W on the chamber surface. This is a **fire risk** on any organic surface, requires an interlocked thermocouple loop, and is **not** something to run unattended in a residential building. NO.
2. **High voltage in tank vacuum (>1 kV).** X-ray generation at 5–30 kV (Farnsworth fusor, electron-beam evaporator, ion accelerators). Requires Pb shielding, dosimetry, and a shielded room. **Hard no with a child in the house.**
3. **Pulsed-power coils >100 V or >10 J stored.** Vance already covered this; I reaffirm.
4. **Uncontained LN₂ in the main living room.** LN₂ work is in the kitchen with the window open, on a tray, with the O₂ monitor visible. Never on carpet, never in a closed bedroom.
5. **In-house liquid helium use without an O₂ monitor and active ventilation.** LHe boiloff is 745× volumetric expansion — slightly worse than LN₂. A 10 L LHe transfer-loss in a sealed apartment is fatal-class. If we ever use LHe here it's a one-shot demonstration with the door open and the kid at a friend's house, period.
6. **Compressed-gas cylinders unsecured.** Any time we have an N₂ purge cylinder or a He cryocooler charge bottle, it's chained to a wall or floor anchor (NFPA 55, 29 CFR 1910.101).
7. **Synthesizing YBCO from precursors.** Vance flagged this. The Y₂O₃/BaCO₃/CuO sintering is a 950 °C tube-furnace process with toxic dust. Buy the disks. NO synthesis.
8. **Mercury, ³He, lithium metal.** Mercury for diffusion pumps — banned in NY State residential; use turbo. ³He fridge — the gas itself is fine, but the apparatus is out-of-scope. Lithium for any BEC variant — flammable in moist air.

The rule is simple: *if it can hurt the kid faster than I can intervene, it doesn't happen here.*

---

## 8. Citations & vendor URLs

**Standards / safety:**
- OSHA 29 CFR 1910.146, Permit-required confined spaces. https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.146
- OSHA 19.5%/23.5% O₂ limit (1910.134(d)(1)(iii); 1910.146). https://www.osha.gov/etools/shipyard/ship-repair/confined-spaces/oxygen-deficient
- ICNIRP Static Magnetic Field Guidelines (2009), Health Phys. 96(4):504. https://www.icnirp.org/en/frequencies/static-magnetic-fields-0-hz/
- U.S. Chemical Safety Board, Bulletin 2003-10-B, Hazards of Nitrogen Asphyxiation. https://www.csb.gov/file.aspx?DocumentId=5636
- Compressed Gas Association P-39, Oxygen-Deficient Atmospheres. [unverified — verify edition before quoting publicly]
- NIH/ORS, Compressed Gas and Cryogen Safety Guidelines. https://ors.od.nih.gov/sr/dohs/Documents/compressed-gas-and-cryogen-safety-guidelines-document.pdf

**Vendors & marketplaces:**
- eBay categories — Turbomolecular Pumps: https://www.ebay.com/b/Turbomolecular-Pumps/184101/bn_78213465 ; Cryocoolers: https://www.ebay.com/sch/i.html?_nkw=cryocooler
- LabX: https://www.labx.com/categories-a/vacuum-pumps , https://www.labx.com/product/pfeiffer-turbo-pumps
- Capovani Brothers (ion pumps, UHV): https://www.capovani.com/ilist.cfm?lcl=148
- BMI Surplus: https://bmisurplus.com/product-category/vacuum-equipment/vacuum-pumps/
- Lab Merchant: https://www.labmerchant.com/used-vacuum-pumps
- AllSurplus on LabX: https://www.labx.com/sellers-a/profile/allsurplus/64755
- American Instrument (Cryomech parts): https://www.americaninstrument.com/products/cryomech-pt410-cryocooler-1466d-circ
- SHI Cryogenics Group: https://shicryogenics.com/products/cryocoolers/pulse-tube-cryocoolers/
- Bluefors (DR market reference): https://bluefors.com/products/dilution-refrigerator-measurement-systems/
- Cryofab (LN₂ dewars): https://www.cryofab.com/

**Cryogen pricing (2025):**
- Rutherford & Titan, "Price of Liquid Nitrogen in the USA (2025)." https://www.rutherfordtitan.com/liquid-nitrogen-generators/liquid-nitrogen-price-usa/
- Banagee Cryoflask, LN₂ dewar pricing 2025. https://www.cryoflask.com/ln2-dewar-price-breakdown/
- Physics Today, "Helium prices surge to record levels as shortage continues" (2024). https://physicstoday.aip.org/news/helium-prices-surge-to-record-levels-as-shortage-continues
- UF Physics, helium cost comparisons. https://www.phys.ufl.edu/~cryogenics/hecost.htm

**Hobbyist / DIY references:**
- Stephen P. Hansen, *The Bell Jar* — quarterly vacuum-technique journal for amateurs. https://www.belljar.net/ ; "Vacuum on the Cheap (Refrigeration Compressors)" https://www.belljar.net/refrig.htm
- Instructables, "Making A Fridge Compressor Into A Vacuum Pump." https://www.instructables.com/Making-A-Fridge-Compressor-Into-A-Vacuum-Pump/
- OpenQuantum DIY MOT (~$8k full BOM): https://www.diyphysics.com/2023/11/10/openquantums-diy-open-source-magneto-optical-atomic-trap/
- Free-piston Stirling cryocooler engineering (110 K): ScienceDirect S0140700720301675. https://www.sciencedirect.com/science/article/abs/pii/S0140700720301675

**Casimir / MEMS-Casimir benchtop refs:**
- "Building a Casimir metrology platform with a commercial MEMS sensor," *Microsystems & Nanoengineering* (2019). https://www.nature.com/articles/s41378-019-0054-5 ; arXiv:1810.09295
- "Casimir Effect in MEMS: Materials, Geometries, and Metrologies — A Review," *Materials* 17(14):3393 (2024). https://www.mdpi.com/1996-1944/17/14/3393

Items marked **[unverified]** above I have not cross-checked against primary source this session — flag for Maya/QA before public quote.

---

**Hand-off to the team.**
- *Sam (Treasurer):* the only realistic cryo CapEx for the next 12 months is a $400 LN₂ dewar + $200 O₂ monitor + $1.5k used scroll pump + $1.5k used small turbo. Total ~$3.5k buys us 77 K + HV — enough for the magnetic-wormhole replica AND a Casimir bench at 10⁻⁶ Torr. Anything below 77 K is a partner-lab conversation.
- *Kai/Zara (sim):* features 6a–6c are all worth shipping; 6a (lab budget) is the highest-leverage pedagogical feature in the whole simulator. It's the one that says "no, you can't, here's why."
- *Maya (QA):* please verify CGA P-39 edition and the LHe expansion ratio (745×) against a 2025 datasheet before any public quote.

— Anders
