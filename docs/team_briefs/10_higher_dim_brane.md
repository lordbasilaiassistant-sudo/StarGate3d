# Brief 10 — Higher-Dimensional, String, and Brane-World Routes

**Author:** Dr. Kenji Sato (theoretical physics — string theory, brane-world cosmology, higher-dim GR)
**Audience:** Engineering team + R6–R11 specialists
**Question on the table:** Do MMP / Randall–Sundrum / ADD / ER=EPR routes deserve simulator engineering budget, or do we ship benchtop-anchored scenes (analogue, magnetic, quantum-info) and treat these as Tier-3 reading material?
**Conventions:** SI, signature `(-,+,+,+)`, `ℏ = c = 1` where convenient, magnetic charge in Dirac units `g_D = 2π/e`.

I want to be useful to Hana and Marcus rather than re-cover their ground. They've already done the GR metric and the QFT energy budget. My job is the higher-dim/stringy side and an honest verdict on whether any of it is buildable, simulable, or a distraction.

---

## 1. MMP (2008.06618) — what it actually is, unpacked

**The geometry.** Take two extremal magnetically-charged Reissner–Nordström black holes in 4D, charges `+q` and `−q` in Dirac units, separated by coordinate distance `d`. Each has horizon radius `r_e ≈ q · l_P · √(α_em/π)` ~ `q · l_P / 11`. In the strict extremal limit the near-horizon geometry of each is `AdS₂ × S²` with both factors of radius `r_e`. MMP's move: instead of two disconnected near-horizon throats, glue them — the AdS₂ factors share their boundaries, producing a long throat of proper length `≈ d` connecting the two `S²`'s. The S² stays at radius `r_e` along the throat.

**The exotic-matter source.** The magnetic flux through each `S²` is quantized (`Φ = 2π q/e`). A 4D massless charged Dirac fermion in this background, on `S²`, has `2q` zero-modes from the lowest Landau level (LLL). Effectively each fermion species contributes `2q` 2D massless chiral fermions running along the throat. With `N_f` charged species, total = `2 q N_f` 2D chirals. Their 1-loop Casimir energy on the throat (a finite cylinder ending on two black-hole-like caps) is **negative**, scaling like

  `E_Cas ≈ −(c · N_f · q) / r_e`

with `c = O(1)`. This sources the ANEC violation that holds the throat open. **No classical exotic matter, no phantom scalar — just standard QFT in a topologically non-trivial background.** That is why this is the credible construction.

**Macroscopic scaling (humanly traversable, MMP §III–V).** Setting tidal force `≲ g_Earth` over a 1m body, demanding `r_e ≳ 1m`, and solving the 1-loop equations:
- `q ~ 10^32` Dirac units (`Q_electric` would be `~ 10^32 e`; this is "Jupiter charge").
- `N_f ≳ q` for the throat to actually open (lowest-Landau-level argument). MMP exploit the RS Kaluza–Klein tower — in RS-II the 5D graviton has effectively a continuum of 4D modes, and similar towers exist for matter on TeV branes — to supply `N_f` cheaply.
- Mass per mouth `M ~ (q · m_P) / √α_em ~ 10^7 M_⊕` ≈ Jupiter-mass; in MMP it can be brought down to `~ 10^5 M_⊕` ≈ Saturn-mass with optimized parameters.
- Throat proper length `d ~ r_e · log(d_ext/r_e)`. Internal proper traversal time `τ_int ~ d/c` ≈ seconds. External time `T_ext ≫ τ_int`: an outside observer waits `~10^4 yr` while the traveler ages a second. This long-external-time guarantees no closed timelike curves form when the mouths are moved — the construction is **causality-preserving by design**.
- Stability: marginal at 1-loop; 2-loop and beyond are open. There's a near-extremal SL(2,R) mode that wants to grow; MMP argue it's stabilized by the same fermion stress that holds the throat open. This is *not* iron-clad.

**Why it isn't built and won't be soon.** Three independent showstoppers:
1. **No magnetic monopoles observed.** MoEDAL (LHC, Run 2) excludes monopole masses up to `~3.9 TeV` for `g = 1–10 g_D` via Drell–Yan and photon fusion (PoS ICHEP2024 621; arXiv:1712.09849 + follow-ups). IceCube relativistic-monopole flux limit `Φ < 2.0 × 10^-19 cm^-2 s^-1 sr^-1` for `0.75c < β < 0.995c` (arXiv:2109.13719); luminescence-channel limit covers `0.1c–0.55c` (arXiv:2107.10548). Sub-relativistic limits arXiv:2507.05896. **Across every accessible window, no signal.** GUT-scale monopoles `~ 10^16 GeV` predicted by inflation+GUT but undetectable individually; we'd need `~10^32` of them per mouth.
2. **Need `N_f ≳ q ~ 10^32` charged massless fermion species.** SM has `O(10)`. MMP's RS escape hatch turns `N_f` into a KK-mode count, which is allowed in principle but pegged to bulk physics we have no evidence for.
3. **Construction problem.** Assembling `~10^7 M_⊕` of extremal magnetic charge — extremality is `Q = M`, a measure-zero point in parameter space, marginally stable, sourced by something like `10^32` confined monopoles per mouth. Even if the matter existed, putting it where you want it is a `~10^53` J energetics problem.

**My read.** MMP is the strongest existence proof we have that traversable wormholes are not forbidden by `QFT + GR + sensible matter content`. As a *construction blueprint* it's untouchable on every axis.

---

## 2. Brane-world wormholes — easier, but how much?

**RS-II (Randall–Sundrum, arXiv:hep-th/9906064).** Single positive-tension 3-brane in `AdS_5` with curvature radius `ℓ`, no second brane. 4D gravity localizes on the brane via the bound-state graviton zero-mode; KK continuum corrects Newton's law as `V(r) = -GMm/r · (1 + 2ℓ²/3r²)`. Eöt-Wash submillimeter torsion-pendulum experiments (PRL 98, 201101) bound `ℓ < 44 µm`. The effective 4D Einstein equations on the brane (Shiromizu–Maeda–Sasaki, gr-qc/9910076) carry a *Weyl tensor projection term* `E_μν` from the bulk that acts as effective stress-energy with no positivity constraint — **the bulk geometry can do the NEC violation while brane matter stays vanilla.**

**Concrete brane wormhole solutions:**
- Bronnikov & Kim, "Possible wormholes in a brane world," PRD 67 (2003) 064027, gr-qc/0212112 — explicit static spherically symmetric brane wormholes with brane matter satisfying WEC; `E_μν` carries the exotic part.
- Anchordoqui & Bergliaffa, gr-qc/0306017 — RS brane wormholes embedded in bulk Schwarzschild–AdS.
- Recent: arXiv:2412.19773 (2024) lifts 4D wormholes to 5D braneworld embeddings; arXiv:2601.16969 (2026) does Ellis–Bronnikov in warped braneworld via local sum rules and shows weak energy condition can be satisfied with the warp factor.

**Are they easier? Numerically, yes — by a factor of `(M_4/M_5)² ~ 10^32` if `M_5 ~ TeV`.** ADD with `n` extra dimensions of size `R` gives `M_4² = M_*^{n+2} R^n`; for `n=2, M_* ~ 1 TeV` ⇒ `R ~ 100 µm` (excluded by Eöt-Wash); for `n=6, M_* ~ 1 TeV` ⇒ `R ~ fm` (LHC missing-energy probes this, CMS 2025 search bumps `M_*` limits ~10%; PDG 2023 review). The "wormhole stabilization budget" in 4D is `c⁴ r_0 / G_4 ≈ 10^43 J·m` for `r_0 = 1m`. In RS-II with `ℓ ≈ 1 µm`, the bulk-projected Weyl term replaces the Newton constant locally with `G_5/ℓ`, so the budget rescales to `~10^43 (M_5/M_4)²` ≈ `10^11 J·m` for `M_5 ~ TeV`. **Twelve orders of magnitude easier — but still not free.** And it requires `M_5 ~ TeV` extra-dim physics that LHC+Eöt-Wash currently disfavor for ADD and tightly constrain for RS.

**Key honest caveat.** Brane wormholes don't violate NEC on the brane *in the 4D effective theory*, but they require specific bulk geometry that is itself an exotic global solution. We are not getting wormholes for free; we are moving the exotic-matter problem from `T_μν` to `E_μν`, which is a notational shuffle until you produce the 5D bulk solution that sources it. See Bronnikov & Kim §IV for the honest accounting.

---

## 3. AdS/CFT, ER=EPR, GJW — gravity-side picture

Marcus covers this from the QI side. From the gravity side:

**Maldacena–Susskind ER=EPR (1306.0533).** Two entangled CFTs in the thermofield-double state are dual to an eternal AdS-Schwarzschild black hole — a non-traversable Einstein–Rosen bridge. Entanglement = wormhole. **Non-traversable** because the two boundaries don't talk; the wormhole is spacelike.

**Gao–Jafferis–Wall (1608.05687).** Add a double-trace coupling `g O_L(t) O_R(-t)` between the two CFTs. The bulk gets a quantum stress tensor with negative averaged null energy (Casimir-like, sourced by the explicit boundary coupling) → ER bridge becomes traversable for a small qubit packet. **Crucially: the message-receiver protocol is non-local in the boundary** — it requires the sender to pre-share entanglement and a coupled Hamiltonian evolution. This is **teleportation dressed up as a wormhole**, in the precise sense that the protocol cannot send information faster than the boundary signal itself.

**Jafferis–Lykken–Spiropulu Sycamore experiment (Nature 612, 51, 2022).** Sparse N=7 SYK Hamiltonian on Google Sycamore, claimed to reproduce GJW signatures. **Heavily contested** (Kobrin et al., arXiv:2301.03522): the learned sparse Hamiltonian doesn't actually preserve scrambling+thermalization plus size winding simultaneously, so the gravitational interpretation is suspect. Five independent holography experts agree the Nature paper's interpretation is on shaky ground (Quanta, March 2023). The *quantum-circuit* result is real; the *"we made a wormhole"* framing is hype.

**The honest path from "two entangled CFTs on a chip" to "real spacetime wormhole."** There isn't one we know of. ER=EPR is a duality statement: the entangled state *is* the wormhole, in a holographic universe. **Our universe is not known to be holographic at the relevant scale.** Even granting AdS/CFT, the dual spacetime is `AdS × stuff`, not Minkowski; getting a 4D-flat-asymptotic traversable wormhole out of a flat-CFT setup requires more machinery than anybody has written down. **For our simulator, ER=EPR is a teaching tool, not a buildable mechanism.** It belongs in the same drawer as MMP — existence proof, not construction.

---

## 4. Experimental search status (current bounds, May 2026)

| Probe | Quantity | Bound (≈) | Implication if positive |
|---|---|---|---|
| Eöt-Wash torsion pendulum | Newtonian ISL deviation | `R_extra < 44 µm` for `n=1`, `< 38 µm` for `n=2` (PRL 98, 201101 + later) | RS-II curvature radius `ℓ`; ADD `R` |
| LHC monojet / missing-E | ADD `M_*` | `M_* > 10–11 TeV` for `n=2`, falling to `~5 TeV` for `n=6` (CMS 2025 single-photon+MET, PDG 2023) | Lowers Planck scale — brane wormhole budget collapses |
| LHC graviton resonance | RS-I `M_KK` | `> 4 TeV` for `c = 0.1` | First-mode KK detection |
| MoEDAL | Monopole mass | `> 3.9 TeV` for `g = 1–10 g_D`, Drell–Yan + γγ fusion | MMP loop is real |
| IceCube | Relativistic monopole flux | `< 2 × 10^-19 cm^-2 s^-1 sr^-1` (`0.75–0.995 c`) | Cosmic monopoles exist |
| ATLAS/CMS heavy ions | Schwinger monopole production | covered by ATLAS Run-3 briefing | Direct probe of strong-field pair creation |
| Sub-relativistic monopole | IceCube luminescence | covers `0.1–0.55 c` (arXiv:2107.10548, 2507.05896) | Cosmic relic monopole density |

**The summary line:** every probe of every higher-dim/monopole signature has come back null at the precision currently accessible. **A positive signal at any one of these would change the calculus enormously**: a monopole detection at MoEDAL plus a KK graviton at LHC plus an ISL deviation at sub-mm scale would, *in combination*, validate the MMP construction's matter content. None has been seen. Not even one of three. We are nowhere near the regime where "build an MMP wormhole" stops being theology.

---

## 5. What this means for the simulator

**Render MMP honestly = render the budget honestly.** The right scene is not a movie tunnel — it's a side panel showing the user the live `(q, N_f, M, r_e, T_ext, τ_int)` tuple as they drag sliders, with red flashes when they leave the regime where the 1-loop calculation is controlled. Coupled to:
- A `S²` of radius `r_e` extruded along proper-length `l ∈ [0, d]`, magnetic-flux lines visualized as Hopf-fiber arrows piercing each `S²`.
- A near-horizon redshift gradient: external region uses the RN exterior metric, throat uses `AdS₂ × S²` with the proper time-dilation factor mapped to color-shift on starlight from the far mouth.
- The "external time vs proper time" asymmetry as an HUD pair of clocks (Hana already calls for this).
- Monopole flux integral `∫ B · dA = 2π q/e` displayed numerically; LLL fermion zero-mode count `2 q N_f` displayed.

**Math cost:** geodesic integration in extremal RN + AdS₂×S² near-horizon gluing is closed-form in conformal coordinates (`AdS₂` Poincaré coordinates `ds² = (-dt² + dz²)/z²`); ~50 lines on top of the generic GR integrator.
**GPU cost:** trivial — same null-geodesic shader as Hana's MT/Ellis, with a coordinate-patch switch at `r ≈ r_e (1 + ε)`. Maybe 1.5× the Ellis fragment budget.

**Brane-world scene = 5D embedding.** Render the warped extra dimension as an *actual visible axis* (RS-II warp factor `e^{-|y|/ℓ}` shown as a vertical squish) with a thin brane at `y=0`. User's worldline lives on the brane; throat reaches into the bulk. This is the scene that *teaches* the user where the NEC violation lives (in `E_μν`, sourced by bulk Weyl curvature, not by anything on the brane). Math: 5D `AdS_5` is closed-form; brane wormhole is a 4D Bronnikov–Kim slice. ~80 lines. GPU: one extra coordinate dimension in the volumetric rendering — ~2× cost, fine.

---

## 6. Three concrete things to add to the world

**6a. `MMPParameters` config object + scene preset.**
```ts
interface MMPParameters {
  q: number;              // magnetic charge in Dirac units
  N_f: number;            // charged massless fermion species
  r_e: number;            // throat radius (m), derived from q
  d: number;              // mouth-to-mouth proper length (m)
  M_mouth: number;        // mass per mouth (kg), derived
  alpha_em: number;       // = 1/137.036
  // derived:
  q_min_for_traversability: number;  // = N_f (LLL constraint)
  T_ext_per_tau_int: number;         // external time per unit proper time
  tidal_g: number;                   // tidal acceleration in g at r_e
  is_one_loop_controlled: boolean;   // false if outside MMP regime
}
```
With analytic functions `r_e = q · l_P · sqrt(alpha_em/PI) / 11` and the budget check.

**6b. Brane-world `RS2Geometry` class.**
- Bulk metric `ds² = e^{-2|y|/ℓ} η_μν dx^μ dx^ν + dy²`.
- Brane wormhole shape function `b(r)` from Bronnikov–Kim.
- Effective `E_μν` on the brane computed from bulk Weyl tensor.
- Energy-condition HUD shows `T_μν^{brane}` (positive — green) AND `E_μν` (sign-indefinite — colored).
- This is the single best teaching tool we can ship for "where does the exotic matter actually live."

**6c. ER=EPR / GJW toy chip.**
A small Bloch-sphere widget showing two qubits in a Bell pair on the left, the GJW double-trace coupling `g O_L O_R` as a knob in the middle, and an animated "qubit traverses the wormhole" event. Crucially, the simulator gates the traversal on **the user enabling the boundary coupling** — visualizing that the wormhole doesn't transmit anything until the boundaries communicate classically. This kills the FTL misconception more effectively than any caption. Math is `O(50)` lines of TFD-state evolution; GPU cost negligible.

---

## 7. Honest verdict on buildability

Three questions, three answers:

**(a) Is there *any* path from "MMP exists in math" to "we build something at any scale"?**
No. Not in the next century, probably not ever in the form MMP wrote down. The construction needs (i) magnetic monopoles we haven't found and (ii) `N_f ~ 10^32` extra fermion species we haven't found and (iii) Jupiter-scale extremal mass placement that requires more energy than humanity has ever generated by `~30` orders of magnitude. **MMP is an existence proof, not a roadmap.** Calling it "humanly traversable" is an in-joke about the tidal-force calculation, not a build directive.

**(b) Can we build a *scaled-down* MMP?**
No, because the construction has no continuous parameter that lets you shrink it while staying in the controlled regime. As `q` decreases, `r_e → l_P` fast, you leave semiclassical control, and the Casimir-energy 1-loop calculation stops being valid. You don't get a "tabletop MMP" the way you get a tabletop Casimir cavity. The Hawking-radiation cousin of this fact: MMP throats with `r_e < µm` decay by Hawking emission of the LLL fermions in `< second`.

**(c) If we had unlimited compute and entanglement, could we simulate a *holographic* MMP and learn anything new?**
Maybe — and this is the interesting question. A holographic dual to MMP would be two coupled SYK-like systems with `O(N_f q)` fermion modes and an explicit double-trace deformation. With `N ~ 10^3` qubits and high-fidelity gates, we could simulate the boundary theory directly and look at: (i) two-sided correlation functions and whether they show the "long external time" scaling MMP predicts; (ii) information-recovery protocols à la GJW and how they degrade as we move toward the MMP regime; (iii) whether the 1-loop stability claim is robust to non-perturbative corrections. **This is the only path I see where the simulator does real physics rather than theater.** It belongs to the QI brief (Marcus / Dr. Vasquez) more than to me, but I flag it here because it's the one MMP-adjacent experiment that has a benchtop hook on a 10-year horizon: noisy intermediate-scale quantum hardware getting honest about coupled-SYK dynamics.

**Recommendation to engineering.** Ship the MMP scene as a *constraint visualizer*, the brane-world scene as a *5D-embedding teaching tool*, and the ER=EPR widget as an *anti-FTL inoculation*. Total budget: ~250 lines of TS, ~2× the Ellis renderer GPU cost. Do **not** build an "MMP simulator" that pretends construction is on the table — that would be the build-without-validation anti-pattern in pure form. The win is honesty, not theater.

If the limited engineering budget forces a choice between MMP/brane/ER=EPR scenes vs. analogue/magnetic/quantum-info scenes, **ship the benchtop-anchored ones first.** MMP/brane/ER=EPR are second-priority because they have no benchtop verification path; they are valuable as teaching scenes layered on top of the validated benchtop scenes, not as replacements. If we have to cut, cut the brane-world 5D scene first (highest GPU cost, narrowest pedagogical payoff), keep MMP (highest pedagogical payoff per line), keep ER=EPR (cheapest, biggest misconception-killer).

---

## 8. Citations (with arxiv IDs, [unverified] flagged)

- Maldacena & Milekhin, "Humanly traversable wormholes," arXiv:2008.06618 (PRD 103, 066007, 2021).
- Maldacena, Milekhin, Popov, "Traversable wormholes in four dimensions," arXiv:1807.04726 (final v3 2020).
- Randall & Sundrum, "An alternative to compactification," arXiv:hep-th/9906064 (PRL 83, 4690, 1999).
- Randall & Sundrum, "A large mass hierarchy from a small extra dimension," arXiv:hep-ph/9905221 (PRL 83, 3370, 1999).
- Arkani-Hamed, Dimopoulos, Dvali, "The hierarchy problem and new dimensions at a millimeter," arXiv:hep-ph/9803315 (Phys. Lett. B 429, 263, 1998).
- Shiromizu, Maeda, Sasaki, "The Einstein equations on the 3-brane world," arXiv:gr-qc/9910076 (PRD 62, 024012, 2000).
- Bronnikov & Kim, "Possible wormholes in a brane world," arXiv:gr-qc/0212112 (PRD 67, 064027, 2003).
- Anchordoqui & Bergliaffa, "Wormhole surgery and cosmology on the brane," arXiv:gr-qc/0306017.
- "On the uplift of 4D wormholes in Braneworld models," arXiv:2412.19773 (2024).
- "Embedding Wormholes and Dyonic Black Strings in Warped Braneworlds via Local Sum Rules," arXiv:2601.16969 (2026).
- Maldacena & Susskind, "Cool horizons for entangled black holes" (ER=EPR), arXiv:1306.0533.
- Gao, Jafferis, Wall, "Traversable wormholes via a double trace deformation," arXiv:1608.05687 (JHEP 12, 151, 2017).
- Gao & Jafferis, "Traversable wormhole teleportation protocol in SYK," arXiv:1911.07416 (JHEP 07, 097, 2021).
- Jafferis et al., "Traversable wormhole dynamics on a quantum processor," Nature 612, 51 (2022). [Sycamore experiment — interpretation contested]
- Kobrin et al., "The Neverending Story of the Eternal Wormhole and the Noisy Sycamore," arXiv:2301.03522 (2023). [Critique of above]
- MoEDAL: Acharya et al., "Search for magnetic monopoles with the MoEDAL forward trapping detector," arXiv:1712.09849 (PRL 118, 061801, 2017); ICHEP 2024 update PoS(ICHEP2024)621.
- IceCube: "Search for Relativistic Magnetic Monopoles with Eight Years of IceCube Data," arXiv:2109.13719 (PRL 128, 051101, 2022).
- IceCube luminescence: arXiv:2107.10548 (low-relativistic regime).
- IceCube sub-relativistic: arXiv:2507.05896.
- Eöt-Wash: Kapner et al., "Tests of the Gravitational Inverse-Square Law below the Dark-Energy Length Scale," PRL 98, 021101 (2007); Adelberger et al. follow-ups. [unverified specific bound 38 µm — verify against latest Eöt-Wash results page before quoting publicly]
- PDG 2023 review of extra dimensions, rpp2023-rev-extra-dimensions.pdf.
- CMS, "Search for new physics in single photon + missing E_T," 2025 release on HEPData (ins3085605). [unverified specific limit improvements — quoted CMS press release figure of 10% enhancement]
- Casadio, Ovalle et al., gravitational decoupling for brane wormholes — many recent refs; we should pick one canonical for the simulator before quoting [unverified — flag for Maya].
- Visser, *Lorentzian Wormholes* (AIP, 1996), ISBN 1-56396-394-9. [book, no arxiv]

---

— Kenji
