# Brief 09 — Sensors & Instrumentation: How We Measure Anything We Claim

**Author:** Dr. Priya Mehta (R9 — instrumentation physicist)
**For:** StarGate3d sim team + benchtop build team
**Date:** 2026-05-01
**Thesis:** The single biggest failure mode of fringe physics is the unmeasured claim. Every "we built X" statement in this program must end with a sensor part number, a noise floor, and an SNR. If you can't say at how many sigma above baseline you'd see your effect, you don't have a result — you have a press release. This brief is the kill-switch.

---

## 1. Magnetic field sensing — for the Prat-Camps replica

The Prat-Camps device's signature is *topology change of the field map*: a dipole at mouth A, a quasi-monopole at mouth B, and (in the full SC version) **zero residual** along the side of the cloak. So we need not one instrument but a hierarchy: cheap-and-fast for the source, sensitive-and-quiet for the cloak.

| Class | Typical floor | Range | Cost | Best for |
|---|---|---|---|---|
| Hall IC (TI DRV5055A1, Allegro A1324) | ~0.1 mT (~1 G) noise (~0.1 µT/√Hz at decade) [unverified — derive from datasheet] | ±20 mT to ±80 mT | $5 chip / $50 board / $250 AlphaLab Milligaussmeter | Mapping the source dipole and the inside of the hose |
| Fluxgate (Bartington Mag-03, Mag-13) | Mag-03 ≈ 6 pT/√Hz at 1 Hz; Mag-13 ultra-low-noise ≤4 pT rms/√Hz at 1 Hz | ±70 µT to ±1 mT | Mag-03 used $400–$1500 / Mag-13 new $3–6 k | DC and quasi-static residual outside the cloak |
| Atomic / OPM (QuSpin QZFM Gen-3) | <4 fT/√Hz, BW to ~300 Hz | ±5 nT operating | ~$5–10 k per channel new (educational pricing rare) | Phase-2 cloak validation if we can get one on loan |
| SQUID (Cryogenic Ltd, STAR Cryo) | <1 fT/√Hz | ±100 µT | $30–80 k + LHe / pulse-tube | Overkill for our scale |

**Minimum spec for Phase-1 (hose only, no SC).** A DRV5055 + ADS1115 24-bit ADC + Arduino on a 3D-printed XYZ stage. Channel field at the hose end is in the mT range; we just need to map shape, not push noise. Total $80.

**Right spec for Phase-2 (full Prat-Camps with SC).** Mag-03 used. Outside-the-cloak residual is what *defines* a successful magnetic wormhole — Prat-Camps reported "undetectable to within their fluxgate noise (~µT)." With a Mag-03 in a 3-layer mu-metal can plus differential gradiometer mode (two probes 5 cm apart, subtract Earth-field common mode), we can resolve nT-level residual and *exceed* the published sensitivity. Decisive measurement.

**Why not OPM for Phase-2.** Cost. Also OPMs need zero-field operation (<5 nT bias), so they require a magnetically shielded room or a 3-axis Helmholtz cancellation cage. We don't have either in the apartment. Park the OPM idea for if/when we get university-lab access.

---

## 2. Optical / photon detection — for any DCE / squeezed-vacuum claim

| Detector | Dark count / NEP | Timing jitter | Cost | Use |
|---|---|---|---|---|
| Si photodiode (FDS100, FGA015) | NEP ~10⁻¹⁴ W/√Hz | ~ns | $20–$200 | Bright-light homodyne, alignment |
| PMT (Hamamatsu H10720/H10721) | dark current ~50–500 pA, ~50–500 cps | ~0.5 ns rise | $1–3 k module | UV-Vis photon counting |
| APD/SPAD module (Excelitas SPCM-AQRH) | 25–500 cps dark | 350 ps FWHM | $4–8 k | Visible single-photon |
| SNSPD (IDQ ID281) | <10⁻³ cps | 20–40 ps FWHM | $100 k+ system + cryostat | The only thing that detects DCE photons cleanly |

**For squeezed-vacuum / DCE detection — balanced homodyne BOM.** This is the harness any "we saw the dynamical Casimir effect" claim must clear. Minimum kit:
- two matched Si photodiodes (Hamamatsu S5973 or Thorlabs FDS015) — $200
- low-noise transimpedance / difference amp (Femto HCA-S, or DIY OPA847-based PCB) — $50–$1500
- 50/50 beamsplitter, polarization optics, mode-matching telescope — $500
- local oscillator: stable single-mode laser (Thorlabs HRS015B HeNe or DBR diode) + isolator — $1.5–4 k
- spectrum analyzer or FFT (Rigol DSA815, used HP 4395A on eBay) — $1–3 k
- shot-noise calibration: dark-noise clearance ≥10 dB above electronic floor [RP Photonics]

**Realistic verdict.** A *classical* shot-noise floor demonstration is buildable on the bench for ~$3 k — and that alone is the test we'd run before claiming any squeezing. Actual squeezed-vacuum *generation* needs an OPO with a periodically-poled crystal pumped by a frequency-doubled stable laser; minimum $20–40 k. **DCE photon counting from a modulated-mirror experiment? Off the table at apartment scale.** The 2011 Wilson superconducting-circuit DCE experiment used a dilution fridge and SNSPDs; we have neither.

---

## 3. Interferometry

Michelson (folded path, common for distance / displacement) and Mach-Zehnder (split path, common for phase imaging) bound the universe of DIY phase sensing. The Thorlabs **EDU-MINT2/M Michelson kit** ($1.2–1.8 k, [unverified — confirm Thorlabs current price]) gives you a working interferometer on a breadboard. Add a stabilized HeNe (Thorlabs HRS015B, ~$3 k) for sub-MHz frequency drift and you reach **~λ/100 ≈ 6 nm path-length sensitivity** at 1 s integration on a kitchen table — *if* you put it on a passive sorbothane-isolated optical breadboard ($300, MB1224 or used Newport breadboard) and run at 4 AM with the HVAC off.

Hard limits in an apartment: floor vibration is broadband at the 100 nm level (people walking, refrigerator compressor), and thermal drift over 10 min runs is hundreds of nanometers without an enclosure. So our practical floor is **~10 nm rms displacement at 1 Hz BW**, which is ample for "see fringes shift when you wave a hand" demos and adequate for milligram-scale Casimir-adjacent thought experiments — but four orders of magnitude away from LIGO-style strain sensitivity. Don't oversell.

For benchtop ($300–$3 k all in): unstabilized HeNe + cube beamsplitter + two front-surface mirrors on kinematic mounts + fast Si photodiode + Arduino-driven PZT for fringe-locking. Achievable: λ/20 phase noise, calibration-grade for any optical-path-length claim we make in the sim.

---

## 4. Force / displacement — Casimir at sub-µm

Lamoreaux 1997 (PRL 78:5) used a *torsion pendulum* with a sphere-plate geometry, 0.6–6 µm separations, thermal-noise floor in the pN regime, and got 5 % agreement with theory. Mohideen 1998 used an AFM and pushed to <100 nm, hitting % agreement.

**Realistic DIY answer: no.** Three blockers:
1. Vibration. Casimir signal at 1 µm and cm² area is order pN; thermal noise of a g-mass torsion pendulum needs Q>10⁴ and µHz resonance, achievable only on a floating optical table in a basement.
2. Surface roughness. The force formula assumes nm-flat metal surfaces. We can't polish those on a kitchen counter.
3. Distance metrology. Knowing the gap to ±10 nm at 500 nm separation requires a capacitive bridge or interferometric readout, which is what AFMs are built around — and a research AFM is $50 k+.

What we *can* do: simulate the force vs. distance curve in the sim (Lifshitz formula, plate-plate is ~ℏcπ²/(240 d⁴)) and **state explicitly in the brief and the README that the experimental Casimir measurement is out of scope** for the apartment program. This is the clearest no in this whole document and we should stand on it.

---

## 5. Acoustic / phonon probes for BEC analogues

The Steinhauer BEC-Hawking measurement used in-situ absorption imaging on an Andor iXon EMCCD — peak QE >95%, dark current <0.001 e/pix/s with TEC, $35–60 k camera plus the entire BEC apparatus ($1–3 M). The thing being measured is a density-density correlation g⁽²⁾(x,x') with anti-diagonal feature; this requires:
- a BEC with sub-µm imaging resolution
- ~10⁵ shots stacked to beat shot noise on the correlation
- magnetic shielding to nT level for the RF-evaporation stage

**What we cannot do in this apartment.** Make a BEC. Make a sonic horizon. Image atom density at 0.5 µm/pixel. **Therefore we do not claim BEC analogue results.** The simulator will reproduce the published g⁽²⁾ figure (Steinhauer 2016 fig. 2) from a Gross-Pitaevskii integrator (Brief 05 §5 mode B), and the validation criterion is "match to within 10% of the published correlation amplitude at the anti-diagonal peak." That is the only honest claim.

For the water-tank kinematic-horizon analogue (Brief 05 §6.i): a phone camera + free-surface synthetic schlieren (Moisy et al. 2009 method, OpenCV implementation) gets us ~100 µm wave-amplitude resolution. That is enough to see mode blocking at the horizon. ~$50 of incremental sensors over the tank itself.

---

## 6. Time / frequency reference

Why we need it: any claim about coincidence detection (DCE, entanglement, two-detector cross-correlation) is bounded by the timing jitter of the worst clock in the chain. Also Allan-deviation bounds set the longest useful integration time for any low-frequency lock-in measurement.

| Source | Allan dev. (1 s) | Allan dev. (1 day) | Cost |
|---|---|---|---|
| Cheap TCXO | 10⁻⁸ | 10⁻⁶ | $5 |
| OCXO (Bliley NV45, used) | 10⁻¹¹ | 10⁻⁹ | $50–$300 |
| GPSDO (Leo Bodnar Mini, Trimble Thunderbolt) | 10⁻¹⁰–10⁻¹¹ | <10⁻¹² | $150–$700 |
| Surplus Rb (FE-5680A, LPRO-101) | 10⁻¹¹ | 10⁻¹¹ | $100–$400 on eBay |

**Recommendation:** one Leo Bodnar Mini-Precision GPSDO ($300) + one surplus Rb on standby ($150 eBay). That gives us a 10-MHz reference good enough for any interferometry or sub-ns coincidence work we'd actually attempt.

---

## 7. Three simulator features (sensor side)

1. **Sensor-overlay mode.** User drags a "virtual probe" (Hall, fluxgate, OPM, photodiode) into the 3D scene. Sim computes the field at that point from the FE solver (Brief 03 §5 feature 1) and *adds* the realistic noise model: 1/f flicker + white floor at the spec'd nT/√Hz, plus 60 Hz mains pickup (USA) at user-set amplitude, plus a quantization step set by the spec'd ADC bits. Output is a live trace that *looks like* the AlphaLab/Bartington output, not a clean curve. **This is what makes the sim a calibration tool.** Implementation: ~200 lines of NumPy noise generator on top of the existing FE post-process.
2. **Calibration-routine simulator.** Walks the user through the standard procedures: zero-Gauss chamber zeroing (with simulated drift), Helmholtz-coil span check (input known field, read output), gradiometer common-mode rejection sweep. Each routine returns a calibration certificate JSON (slope, offset, residual, χ²) consumable by feature 3. Models the tedium honestly so users grasp why "I just plugged it in and got a number" is wrong.
3. **Sensitivity calculator / claim killer.** User specifies (a) experiment configuration, (b) instrument pick from §1–6 above, (c) integration time, (d) shielding model. Sim returns: "Phase-1 magnetic wormhole replica residual outside the (no-SC) hose at 5 cm = 12 µT. DRV5055 noise in 1 Hz BW = 30 µT rms. **SNR = 0.4. Effect not resolvable.** Use Mag-03 (1 nT rms in 1 Hz BW): SNR = 12,000. Resolvable at >>5σ." Three-line verdict, color-coded green/yellow/red. **Every experiment in this program must pass through this calculator before parts are bought.**

---

## 8. Three apartment experiments under $5 k

### (A) Phase-1 magnetic-hose field map — $250
Mu-metal foil hose ($60) + N52 cube source magnet ($15) + DRV5055 board ($15) + ADS1115 ADC ($10) + Arduino ($25) + 3D-printed XYZ stage on linear rails ($100) + connectors / wire ($25). **Expected sensitivity:** 30 µT rms in 1 Hz BW; field at hose mouth ~5 mT. **SNR ~150.** **Kill criterion:** if the field at mouth B (far end of hose) is not at least 10× background within a 2 cm radius, the FE solver in Brief 03 §5 is wrong and we stop coding the wormhole sim until we understand why.

### (B) Mu-metal shielding effectiveness chamber — $400
Three concentric mu-metal cans (12-oz coffee cans wrapped in MagShield foil, $80 each in materials) + Bartington Mag-03 used ($600 if we splurge — borderline budget) or a Honeywell HMC5883L breakout ($10) + Earth field as known input. **Expected sensitivity:** with Mag-03, 6 pT/√Hz; with HMC5883L, ~100 nT. **Kill criterion:** measured shielding factor must agree with the cylindrical-mu-metal analytic formula (Mager 1968) to within 30 %. If not, we don't trust the FE solver's permeability handling and Brief 03's hose model is suspect. This is the cheapest possible *FE-solver validation experiment* we can run.

### (C) Benchtop Michelson + thermal-drift survey — $1.8 k
Thorlabs EDU-MINT2/M Michelson kit (~$1.4 k) + sorbothane breadboard pad ($150) + Si photodiode + Arduino lock-in. **Expected sensitivity:** ~10 nm rms displacement at 1 Hz BW, kitchen-table conditions. **Kill criterion:** if we can't hold a fringe stable for 30 s with the HVAC off at 3 AM, no optical-analogue experiment in this program is feasible at home. Decides whether interferometric work happens here or only at a borrowed lab. Also generates the *real noise PSD* we feed back into simulator feature (1).

All three experiments deliberately test our **measurement chain**, not exotic physics. That is the point — calibrate the instrument before claiming the result.

---

## 9. Citations and vendor links

- **Lamoreaux S.K.** *Demonstration of the Casimir Force in the 0.6 to 6 µm Range.* Phys. Rev. Lett. 78, 5 (1997). DOI:10.1103/PhysRevLett.78.5. https://www.mit.edu/~kardar/research/seminars/Casimir/PRL-Lamoreaux.pdf
- **Steinhauer J. et al.** *Observation of thermal Hawking radiation and its temperature in an analogue black hole.* Nature 569, 688 (2019). arXiv:1809.00913.
- **Wilson C.M. et al.** *Observation of the dynamical Casimir effect in a superconducting circuit.* Nature 479, 376 (2011). DOI:10.1038/nature10561.
- **Bartington Mag-03 / Mag-13 datasheet** (DS0013). https://gmw.com/product/mag-03-mag-13/ ; ultra-low-noise variant <4 pT rms/√Hz at 1 Hz, https://gmw.com/mag-13-ultra-low-noise/
- **QuSpin QZFM Gen-3** OPM, <4 fT/√Hz to 300 Hz. https://quspin.com/technology/
- **TI DRV5055** datasheet. https://www.ti.com/product/DRV5055 ; https://www.ti.com/lit/ds/symlink/drv5055.pdf
- **ID Quantique ID281** SNSPD: <10⁻³ cps dark, <40 ps jitter, $100 k+ system. https://www.idquantique.com/quantum-detection-systems/snspd-technology/
- **Excelitas SPCM-AQRH** datasheet (Si SPAD module).
- **Hamamatsu H10720/H10721** PMT modules. https://www.hamamatsu.com/us/en/product/optical-sensors/pmt/pmt-module/current-output-type/H10720-01.html
- **Thorlabs EDU-MINT1/2** Michelson kit. https://www.thorlabs.com/thorproduct.cfm?partnumber=EDU-MINT2/M [unverified 2026 price]
- **Stanford Research SR830** lock-in (used) ~$3.5–4.5 k via ValueTronics / AccuSource. https://www.thinksrs.com/products/sr830.html
- **Leo Bodnar Mini-Precision GPSDO.** https://www.leobodnar.com/shop/index.php?main_page=product_info&products_id=234 [verify product still listed 2026]
- **Andor iXon Ultra EMCCD** specs (>95% peak QE). https://andor.oxinst.com/cameras-for-quantum-optics
- **Moisy F., Rabaud M., Salsac K.** *A synthetic Schlieren method for the measurement of the topography of a liquid interface.* Exp. Fluids 46, 1021 (2009). [open-source FCD implementations exist on GitHub]
- **RP Photonics** encyclopedia, balanced photodetection. https://www.rp-photonics.com/balanced_photodetection.html
- **Mager A.** *Magnetic shielding efficiencies of cylindrical shells with axis parallel to the field direction.* J. Appl. Phys. 39, 1914 (1968). [for analytic FE-solver validation]

[unverified] tags above flag prices/specs not directly confirmed in this session; verify at quote time.

---

**Bottom line for the team.** Until experiment (A), (B), and (C) are running and the simulator's sensor-overlay + sensitivity-calculator features are in place, **no claim leaves this program**. Sensors before sources. Calibration before claims. The wormhole stays in the sim until the meter agrees with the model on a system whose physics we already understand.
