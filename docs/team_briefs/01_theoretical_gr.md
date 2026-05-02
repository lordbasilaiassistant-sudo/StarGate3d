# Brief 01 — Theoretical GR / Wormhole Metrics for the Stargate Simulator

**Author:** Dr. Hana Reyes (GR specialist)
**Audience:** Engineering team building WebGL/WASM real-physics simulator
**Goal:** Decide which spacetimes we numerically integrate, which energy-condition
loopholes are honest, and what we render that is physically real (not movie FX).

---

## 1. Wormhole metrics, ranked for the simulator

I'm ranking by *implementation tractability × physical interest × visual
distinguishability*. All metrics use signature `(-,+,+,+)`, units `G = c = 1`.

### Tier 1 — ship in v1

**(a) Morris–Thorne (1988).** The reference geometry. Spherically symmetric, static.
```
ds² = -e^{2Φ(r)} dt² + dr²/(1 - b(r)/r) + r² (dθ² + sin²θ dφ²)
```
- Shape function `b(r)`, throat at `r = b₀` where `b(b₀) = b₀`.
- Redshift function `Φ(r)`; `Φ` finite everywhere ⇒ no horizon (the whole point).
- Flare-out: `b'(b₀) < 1`.
- Standard pedagogical choice: `b(r) = b₀² / r`, `Φ(r) = 0` (zero-tidal-force).
- **Energy condition violated:** NEC at the throat (`ρ + p_r < 0`), hence WEC, SEC.
- **Why a user cares:** simplest possible "spherical hole through hyperspace."
  Stepping through, you see a smoothly distorted view of the far universe with a
  sharp Einstein ring at the throat. Best onboarding metric. — Morris & Thorne,
  *Am. J. Phys.* 56, 395 (1988); DOI 10.1119/1.15620.

**(b) Ellis drainhole / Ellis–Bronnikov (1973).** Closed-form, exact, no exotic
matter beyond a phantom scalar. Same shape Thorne used in *Interstellar*.
```
ds² = -dt² + dl² + (l² + b₀²)(dθ² + sin²θ dφ²)
```
where `l ∈ (-∞, +∞)` is the proper radial coordinate and the throat sits at `l = 0`.
- One free parameter: throat radius `b₀`.
- **Energy violation:** sourced by a *phantom* scalar field with negative kinetic
  term — NEC violated globally, not just at the throat.
- **Why a user cares:** because `l` is global and analytic, you get a perfectly
  smooth fly-through with no coordinate singularity to debug. This is the metric
  to validate the integrator against. James et al. 2015 used a regularized
  three-parameter Ellis variant. — Ellis, *J. Math. Phys.* 14, 104 (1973);
  Bronnikov, *Acta Phys. Pol. B* 4, 251 (1973).

**(c) Teo rotating wormhole (1998).** Stationary, axisymmetric — the rotating
generalization of Morris–Thorne. Has an ergoregion.
```
ds² = -N² dt² + e^{2μ} dr² + r²K² [dθ² + sin²θ (dφ - ω dt)²]
```
- Functions `N, K, ω, μ` of `(r, θ)`; throat where `1 - b/r → 0`.
- **Energy violation:** NEC violated at throat; Teo showed there exist geodesic
  classes that *miss* the exotic matter entirely — important for "is it
  actually traversable by a person."
- **Why a user cares:** frame dragging. Light gets twisted asymmetrically as it
  threads the throat; entering a Teo wormhole looks measurably different from
  Morris–Thorne even at the same throat radius. — Teo, *Phys. Rev. D* 58,
  024014 (1998); arXiv:gr-qc/9803098.

### Tier 2 — ship in v2

**(d) Maldacena–Milekhin–Popov "humanly traversable" wormhole (2020/2021).**
The serious one. A four-dimensional Einstein–Maxwell + charged-massless-fermion
solution where the negative Casimir energy of the fermions threads the throat.
Two near-extremal magnetically charged black holes glued by a fermion-mediated
non-local coupling.
- **Energy violation:** ANEC violated by quantum (Casimir-like) stress, not
  classical exotic matter. This is the *first arguably realistic* construction.
- **Why a user cares:** transit time is *long* in external coordinates (causality-
  preserving) but *short* in proper time — the simulator must show that
  asymmetry. Fermion field dressing means the throat has a non-trivial
  near-horizon structure. — Maldacena, Milekhin, Popov, "Traversable wormholes
  in four dimensions," arXiv:1807.04726 (final v3 2020); also the "Humanly
  traversable wormholes" follow-up *Phys. Rev. D* 103, 066007 (2021).

**(e) Damour–Solodukhin wormhole (2007).** A horizonless "black-hole foil" —
Schwarzschild with a tiny deformation that replaces the horizon with a throat.
```
ds² = -(1 - 2M/r + λ²) dt² + (1 - 2M/r)^{-1} dr² + r² dΩ²
```
- One small parameter `λ ≪ 1`. As `λ → 0`, recovers Schwarzschild exterior.
- **Energy violation:** NEC at the throat; can be made arbitrarily small per
  unit volume by tuning `λ`.
- **Why a user cares:** the simulator can show "an object that *looks* like a
  black hole from a distance but you can fall through it." Late-time echoes,
  no event horizon — directly tied to LIGO echo searches. — Damour & Solodukhin,
  *Phys. Rev. D* 76, 024016 (2007); arXiv:0704.2667.

### Tier 3 — optional

**(f) Visser thin-shell wormholes (1989).** Cut-and-paste two Schwarzschild
exteriors at `r = a > 2M`; concentrate all NEC violation on a 2-surface (the
shell). Israel junction conditions give the surface stress-energy. Stability
under radial perturbations is well-studied.
- **Why a user cares:** the throat is a *visible thin membrane*. Geodesics
  refract discontinuously crossing it. Pedagogically clean. — Visser, *Phys.
  Rev. D* 39, 3182 (1989); *Nucl. Phys. B* 328, 203 (1989).

---

## 2. Energy conditions and the impossibility wall

**NEC:** `T_{μν} k^μ k^ν ≥ 0` for every null `k^μ`. Every classical fluid in the
Standard Model satisfies it. Every traversable wormhole violates it at the throat
(this is a *theorem*, not an artifact — Hochberg & Visser, arXiv:gr-qc/9802046).

**ANEC:** `∫ T_{μν} k^μ k^ν dλ ≥ 0` along a complete null geodesic. Weaker than
NEC. In flat 4D Minkowski QFT, ANEC holds (Faulkner–Leigh–Parrikar–Wang 2016,
arXiv:1605.08072). In curved spacetime, ANEC can be violated by quantum effects;
this is the *only* surviving honest loophole.

**Ford–Roman quantum inequalities:** even when local NEC violation is allowed
quantum-mechanically (Casimir, squeezed vacuum), the magnitude × duration is
bounded. Roughly `⟨ρ⟩ × τ⁴ ≳ -ℏ`. For macroscopic wormhole throats this forces
either (i) microscopic throat radius or (ii) implausibly thin shells of
negative-energy matter. — Ford & Roman, "Quantum field theory constrains
traversable wormhole geometries," arXiv:gr-qc/9510071; "Averaged Energy
Conditions and Quantum Inequalities," arXiv:gr-qc/9410043.

**Surviving loopholes (be honest about which is which):**
1. *Casimir-like quantum stress* in a non-trivial topology — Maldacena–Milekhin–
   Popov route. Real but gives long, narrow wormholes.
2. *Modified gravity* (f(R), Gauss–Bonnet, Einstein–Cartan) — the effective
   stress tensor includes geometric terms that mimic NEC violation without exotic
   matter. Lobo & collaborators, arXiv:0907.1390 and follow-ups.
3. *Higher-dimensional* / braneworld constructions where 4D NEC violation comes
   from bulk curvature.
4. *Phantom scalar* sources (Ellis) — disfavored by cosmology but mathematically
   clean.

**For the simulator: label every metric with its loophole.** A user toggling
between Ellis (phantom scalar — speculative), Maldacena–Milekhin–Popov (Casimir
quantum stress — borderline plausible), and a thin-shell construction (classical
exotic matter — fully speculative) should *see* that label. This is a teaching
tool, not a vibe.

---

## 3. Numerical recipe — null geodesics in MT-class metrics

Use the **Hamiltonian formulation**, not the second-order geodesic equation.
Two reasons: (i) conserved quantities are explicit canonical momenta;
(ii) symplectic integrators preserve them to machine precision over millions of
steps.

For Morris–Thorne with `Φ = 0`:
```
H = ½ g^{μν} p_μ p_ν
  = ½ [ -p_t² + (1 - b/r) p_r² + p_θ²/r² + p_φ²/(r² sin²θ) ]
```
Conserved:
- `E = -p_t` (energy at infinity)
- `L = p_φ` (axial angular momentum)
- `H = 0` (null)
Reduce to 2D in the equatorial plane `θ = π/2`. The radial equation becomes
```
(dr/dλ)² = (1 - b/r)(E² - L²/r²)
```
Turning point at `r_tp` where the bracket vanishes.

**Integrator choice.** I want **symplectic** for closed orbits and long traversals
(leapfrog/Verlet on the Hamiltonian, or 4th-order Yoshida). RK45 (Dormand–Prince)
is fine for short transit shots through the throat — adaptive error control
handles the throat region well — but it drifts on `H = 0` over long integrations.
Recommendation: **adaptive Dormand–Prince 5(4) with `H` monitored as a residual,
project back to the null cone every N steps.** If we ever do bound photon orbits
around the throat (light rings), switch to Yoshida-4.

**Pitfalls a naive impl will hit:**
1. **Coordinate singularity at the throat** (`g_{rr} → ∞` as `b/r → 1`). Fix:
   switch to proper radial coordinate `l`, defined by `dl/dr = (1 - b/r)^{-1/2}`.
   For Ellis this is global and analytic — use `l` everywhere.
2. **Turning-point sign flip.** When `dr/dλ → 0`, naive ODE solvers stall or
   bounce wrong. Detect zero-crossings of `dr/dλ`, flip sign manually, and
   re-initialize the step.
3. **`H = 0` drift.** RK45 will leak ~1e-6 per 1e5 steps. Monitor and project.
4. **Ergoregion in Teo.** Inside the ergoregion `g_{tt} > 0`; `t` is no longer
   timelike. Don't use `E = -p_t` to define "energy at infinity" without care;
   use `p_t` directly as the conserved momentum.
5. **Step size at the throat.** Affine-parameter step that's fine in the asymptotic
   region under-resolves the throat by ~10×. Adaptive stepping is mandatory; if
   you must use fixed-step, parameterize by `l` not `r`.
6. **Backward ray-tracing.** For rendering, integrate from camera *backward* to
   source. Geodesics are time-reversal symmetric, so this is just a sign flip on
   the affine parameter, but the boundary conditions reverse.

---

## 4. What to render that's physically real

For each metric we ship, the simulator should reproduce — and the user should be
able to verify against — published results:

1. **Gravitational lensing pattern at the throat.** The "other universe" appears
   inside a circular disk of angular radius set by `b₀` and observer distance.
   Outside the disk, the near-universe is distorted by the throat's gravitational
   pull. Compare directly to James et al. 2015 Figs. 6, 10, 15 (arXiv:1502.03809).
2. **Einstein ring at the throat.** A bright source directly behind the throat
   produces a ring whose radius is computable analytically for Ellis. This is the
   single best validation test — if our ring radius doesn't match the closed-form
   answer to <1%, the integrator is broken.
3. **Redshift / blueshift on transit.** For Morris–Thorne with non-zero `Φ`, an
   ingoing photon's frequency shifts by `e^{Φ(observer) - Φ(source)}`. The user
   should see the spectrum (we fake spectra with three RGB channels weighted by
   blackbody at shifted T) of stars on the far side change as they cross.
4. **Time-dilation artifacts.** A clock dropped through the throat reads less
   proper time than a clock that stays outside; a user "stepping through" should
   see external clocks tick fast. We render an HUD clock pair.
5. **What the "other side" looks like.** For Ellis, both asymptotic regions are
   flat Minkowski; the user sees a different starfield (we use two HEALPix sky
   maps and switch). For Maldacena–Milekhin–Popov, the "other side" is the
   *interior* of a near-extremal black hole — much more exotic; we render the
   AdS₂ × S² near-horizon throat with appropriate redshift.
6. **Shadow / photon sphere for Damour–Solodukhin.** As `λ → 0`, the
   Schwarzschild shadow forms; for `λ ~ 0.1` the shadow has subtle internal
   structure — late-time photon echoes. This is the metric closest to current
   LIGO/EHT science.

The benchmark images we match: Riazuelo's Schwarzschild ray-traced renderings
(2008, *Voyage au coeur d'un trou noir*, [unverified] specific arxiv ID — Riazuelo
publishes mostly in proceedings; we should validate against his published
imagery, not cite the wrong paper) and James et al. 2015 (arXiv:1502.03809) for
the Ellis-class wormhole specifically.

---

## 5. Three features to insist on, three to kill

### Insist on
1. **Closed-form validation harness.** For every metric, bundle 3–5 analytic
   test cases (Einstein ring radius, deflection angle vs. impact parameter,
   ISCO radius for Damour–Solodukhin) and run them in CI. Without this we won't
   catch when a renderer change silently breaks the physics.
2. **Energy-condition HUD.** A toggle that draws `T_{μν} k^μ k^ν` along the
   user's worldline as they transit. Negative regions render red. This makes the
   "exotic matter" tangible — users *see* where they passed through NEC-violating
   stress.
3. **Embedding-diagram side panel.** A 2D `(r, z)` Flamm-style embedding of the
   `t = const, θ = π/2` slice, with the user's geodesic drawn on it in real time.
   This is what makes wormhole geometry click for a non-specialist.

### Kill
1. **The lens-flare "swirly tunnel" effect** from sci-fi films. It's not a
   geodesic structure, it's a post-processing shader. If we want a tunnel look
   it must come from actual gravitational lensing of a structured background
   (accretion disk, dust), not screen-space effects.
2. **Faster-than-light traversal animations.** Even traversable wormholes don't
   transmit information FTL in the ambient space (Maldacena–Milekhin–Popov is
   explicit about this). Any UI that suggests "1 ly in 5 seconds external" is
   physically wrong; show the long-external / short-proper time asymmetry instead.
3. **Wormhole "entrance shimmer" / particle effects at the throat.** Real
   throats in classical solutions are smooth surfaces. The only physical
   "shimmer" is Hawking-like radiation from the exotic matter, which is
   undetectably faint. Don't fake it.

---

## 6. Citations

- Morris & Thorne, "Wormholes in spacetime and their use for interstellar
  travel," *Am. J. Phys.* 56, 395 (1988). DOI 10.1119/1.15620.
- Ellis, "Ether flow through a drainhole — a particle model in general
  relativity," *J. Math. Phys.* 14, 104 (1973).
- Bronnikov, "Scalar-tensor theory and scalar charge," *Acta Phys. Pol. B* 4,
  251 (1973). [unverified — paginated print only, no arXiv]
- Teo, "Rotating traversable wormholes," *Phys. Rev. D* 58, 024014 (1998);
  arXiv:gr-qc/9803098.
- Visser, "Traversable wormholes: Some simple examples," *Phys. Rev. D* 39,
  3182 (1989).
- Visser, "Traversable wormholes from surgically modified Schwarzschild
  spacetimes," *Nucl. Phys. B* 328, 203 (1989).
- Damour & Solodukhin, "Wormholes as black hole foils," *Phys. Rev. D* 76,
  024016 (2007); arXiv:0704.2667.
- Maldacena, Milekhin, Popov, "Traversable wormholes in four dimensions,"
  arXiv:1807.04726 (v3 2020).
- Maldacena & Milekhin, "Humanly traversable wormholes," *Phys. Rev. D* 103,
  066007 (2021); arXiv:2008.06618.
- Hochberg & Visser, "The null energy condition in dynamic wormholes,"
  arXiv:gr-qc/9802046.
- Ford & Roman, "Averaged energy conditions and quantum inequalities,"
  *Phys. Rev. D* 51, 4277 (1995); arXiv:gr-qc/9410043.
- Ford & Roman, "Quantum field theory constrains traversable wormhole
  geometries," *Phys. Rev. D* 53, 5496 (1996); arXiv:gr-qc/9510071.
- Faulkner, Leigh, Parrikar, Wang, "Modular Hamiltonians for deformed
  half-spaces and the averaged null energy condition," *JHEP* 09 (2016) 038;
  arXiv:1605.08072.
- Lobo, "Closed timelike curves and violation of the null energy condition,"
  arXiv:0710.4474 [unverified specific ID — Lobo has many wormhole papers,
  the modified-gravity review I have in mind is arXiv:0907.1390 but verify
  before quoting].
- James, von Tunzelmann, Franklin, Thorne, "Visualizing Interstellar's
  Wormhole," *Am. J. Phys.* 83, 486 (2015); arXiv:1502.03809.
- Riazuelo, black-hole visualization work circa 2008 [unverified arXiv ID —
  he publishes mostly in proceedings/imagery; cite the imagery directly].
- Fewster & Roman, "Wormhole restrictions from quantum energy inequalities,"
  arXiv:2405.05963 (recent review — useful synthesis for the energy-condition
  HUD).

— Hana
