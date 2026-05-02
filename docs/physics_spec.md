# Physics Specification — what the simulator must compute

Synthesis of briefs 01–11. Cited inline as `[B##]`. Every `[unverified]` flag is
laundered through; every "do not do this" is collected in §5. This is an
operating spec, not an executive summary.

---

## 1. Core physics modules

Each module specifies: equations, integrator, source brief(s), implementation
cost from those briefs, and a verification recipe.

### 1.1 Spacetime metrics — closed-form metric library

**Brief sources:** B01 (primary), B04, B10.

**Metrics shipped:**
- Morris–Thorne, signature `(-,+,+,+)`, shape `b(r) = b₀²/r`, redshift `Φ=0`
  (Tier-1 default) `[B01]`.
- Ellis–Bronnikov drainhole `ds² = -dt² + dl² + (l² + b₀²) dΩ²`, single
  parameter `b₀`, global proper-radial coordinate `l` `[B01]`.
- Teo rotating wormhole, axisymmetric, ergoregion `[B01]`.
- Maldacena–Milekhin–Popov 4D, two near-extremal magnetically-charged RN BHs
  glued by AdS₂×S² throat (Tier-2) `[B01, B02, B10]`.
- Damour–Solodukhin black-hole foil with `λ ≪ 1` (Tier-2) `[B01]`.
- Visser thin-shell wormhole, Israel junction conditions on a 2-surface
  (Tier-3 optional) `[B01]`.

**Implementation:** templated metric struct with closed-form `g_{μν}`,
`g^{μν}`, and Christoffel symbols emitted by SymPy/Mathematica → WGSL
codegen at build time `[B04 §2]`. Runtime autodiff is forbidden; `[B04]`
benchmarks autodiff at 3–5× the cost of a closed-form eval and notes fp16
in Christoffels destroys energy conservation in ≤50 steps.

**Cost:** Tier-1 metrics ~30 FLOPs per RHS eval `[B04]`; per-metric WGSL is
~50–80 lines on top of the generic integrator `[B10]`. MMP scene is one
coordinate-patch switch at `r ≈ r_e(1+ε)` for the AdS₂×S² near-horizon
gluing `[B10]`.

**Verification:** §1.2 closed-form test harness must be green for every
metric before that metric is exposed in UI `[B01 §5, B04 §6]`.

---

### 1.2 Geodesic integration

**Brief sources:** B01, B04.

**Integrator choice — disagreement noted:**
- B01 recommends **Hamiltonian formulation + symplectic** (leapfrog/Verlet
  on `H = ½ g^{μν} p_μ p_ν` or 4th-order Yoshida) for closed orbits and
  long traversals; RK45 (Dormand–Prince) acceptable for short transit
  with `H` projected back to the null cone every N steps.
- B04 recommends **classical RK4 in 8D phase space `(x^μ, p^μ)`** with
  affine parameter, arguing the geodesic equation is not separable
  in canonical form once metrics go off-diagonal, so RK4's accuracy-per-
  RHS-eval beats leapfrog for the precision the renderer needs. B04 cites
  Riazuelo and DNGR/James et al. 2015 as both using RK-style integrators.

**Resolution:** ship RK4 (B04) as the primary GPU fragment-shader
integrator because that is the dominant runtime path; ship symplectic
Yoshida-4 as the **closed-orbit / light-ring mode** in compute shader for
when the user wants stable bound orbits around a Damour–Solodukhin foil.
Keep `H` as a residual monitor in both.

**Step-size adaptation:** `Δλ = α · L / |p|` with `L = 1/√K` (K =
Kretschmann), `α ∈ [0.05, 0.2]`. Closed-form K for Morris–Thorne:
`K = 12 b₀⁴ / (b₀² + r²)⁴` (B04 — verify before shipping). For metrics
without closed-form K, use embedded RK4(5) with FSAL (Fehlberg) `[B04]`.

**Pitfalls (mandatory handling) `[B01 §3]`:**
1. Coordinate singularity at the throat: switch to proper radial `l`,
   `dl/dr = (1 - b/r)^{-1/2}`. For Ellis use `l` everywhere.
2. Turning-point sign flip: detect `dr/dλ` zero-crossings, flip sign, re-init.
3. `H = 0` drift: project to null cone every N steps.
4. Teo ergoregion: don't use `E = -p_t` inside; `t` not timelike there.
5. Step size at the throat: parameterize by `l` not `r` if using fixed step.
6. Backward ray-tracing for rendering: integrate camera→source, sign-flip
   on affine parameter.

**Closed-form Christoffels — Morris–Thorne (Φ=0)** `[B04]`:
- `Γ^θ_{rθ} = Γ^φ_{rφ} = r/(b₀²+r²)`
- `Γ^r_{θθ} = -r`, `Γ^r_{φφ} = -r sin²θ`
- `Γ^θ_{φφ} = -sinθ cosθ`, `Γ^φ_{θφ} = cot θ`

**Cost:** primary lensing pass on RTX 3060 @ 1080p estimated 5–7 ms for
Morris–Thorne, 200–800 RK4 steps × 30 FLOPs × 4 stages × 1080p = 50–200
GFLOPs/frame `[B04 §3]`. Bottleneck is register pressure / occupancy, not
ALU.

**Verification recipes (CI-mandatory, all on Rust+WASM offline integrator
shared with GPU shader source) `[B04 §6]`:**
1. Schwarzschild deflection: `b = 5.2 r_s` → `α = 0.40 rad ± 1e-4`,
   tolerance 1e-3 fractional.
2. MT null-geodesic energy conservation: `|ΔE/E| < 1e-6` over 1000 steps.
3. Photon sphere stability: at `b = 3√3 M/2` orbit radius stable to 1%
   over 5 orbits.
4. Müller (2008) MT lensing image reproduction: PSNR > 35 dB against
   published checker-pattern image. `[B04 — Müller arxiv ID flagged
   unverified]`
5. Embedding-diagram check: numerical embedding of `t=const, θ=π/2`
   matches `z(r) = b₀ · arcsinh(r/b₀)` to 1e-5.
6. (Optional) Kerr ISCO at `a=0.9M` should give 2.32 M.

---

### 1.3 Energy-condition tensors

**Brief sources:** B01, B02, B04 §5d.

**Computed quantities per voxel:**
- Renormalized stress-energy `T_{μν}` (10 components) `[B02]`.
- Energy density `ρ = T^00`.
- Radial / transverse pressures `p_r, p_t`.
- Gradient magnitude `|∇T|`.
- Source tag enum `{Casimir, squeezed, MMP-fermion, none}` `[B02]`.

**Closed-form analytic sources for voxel population `[B02 §5a]`:**
- Casimir parallel-plate: `ρ_Casimir(x) = -(π²/720) · ℏc / d_eff(x)⁴`,
  scales as `-1/d⁴`. Numerics: `d=1µm → -1.3×10⁻³ J/m³`,
  `d=100nm → -13 J/m³`, `d=10nm → -1.3×10⁵ J/m³`,
  `d=1nm → -1.3×10⁹ J/m³` (ideal-conductor formula breaks below ~10nm
  per surface-plasmon corrections).
- Squeezed vacuum mode `r`: `ρ_squeezed(x,t) = ρ_vac · [cosh(2r) -
  sinh(2r) cos(2(ωt - k·x))] - ρ_vac`.
- MMP fermion line-energy: `∫ρ dl ≈ -N_f ℏc / r_e²` along the throat.

**For Morris–Thorne, closed-form `T_{μν}`:** `G_{μν} = 8π T_{μν}` gives
`T_{tt}, T_{rr}, T_{θθ}` analytically in `b, Φ`. NEC on radial null
`k = (1,1,0,0)`: `ρ + p_r = -b'/(8π r²)` — negative at the throat,
the famous exotic-matter requirement `[B04 §5d]`.

**HUD readouts (all live):**
- `E_neg(t) = ∫_{ρ<0} ρ d³x`, must equal/exceed Morris–Thorne requirement
  `E_req = -c⁴ r_0 / G` for throat radius `r_0` `[B02]`.
- Quality factor `Q_QI(t) = E_neg / E_FR_bound` — Ford–Roman QI bound on
  current geodesic sample. `Q > 1` flashes red (unphysical). `[B02]`
- ANEC integrand `I_ANEC = ∫_γ T_{μν} k^μ k^ν dλ` along central null
  geodesic. Plot as 1D curve under 3D view; 8 sample geodesics minimum
  (axial + 7 off-axis at `r/r_0 ∈ {0.25, 0.5, 0.75, 1.0}` pairs) `[B02
  §5c]`. ANEC violation flashes "WORMHOLE VIABLE"; non-violation kills
  the badge.

**Quantum-inequality bound (Ford–Roman, flat 4D, massless scalar)
`[B01 §2, B02 §3]`:**
```
∫ ⟨T_{μν} u^μ u^ν⟩ · (τ₀/π) / (τ² + τ₀²) dτ ≥ -3ℏc / (32π² τ₀⁴)
```
For Morris–Thorne throat `r_0`, exotic matter band thickness
`Δr ≲ √(l_P · r_0)`. `r_0 = 1m → Δr ≲ 4×10⁻¹⁸ m` (sub-nuclear); `r_0 =
1km → Δr ≲ 1.3×10⁻¹⁶ m`. ρ in the band must be `~ -10²⁰ × ρ_Schwarzschild`.
This is the "killer for naïve MT wormholes built from generic squeezed
vacuum"; MMP evades because the negative energy lives in higher-dimensional
Casimir geometry, not 4D Minkowski free-QFT excitation.

**Cost:** voxel population is closed-form analytic; per-frame ANEC
integrand on 8 geodesics is ~free; rendering is volumetric overlay with
diverging colormap, alpha ∝ `|ρ|/ρ_QI_bound` `[B02 §5a]`.

**Verification:** B04 §5d test — render NEC-violation shell on MT throat,
visually confirm against `ρ + p_r = -b'/(8π r²)` closed-form sign
analysis.

---

### 1.4 Exotic-matter sources (per scene)

**Brief sources:** B01 §2, B02, B10.

**Loophole label per metric `[B01 §2]` — every metric in UI must show its
loophole tag:**
- Ellis = phantom scalar (speculative, disfavored by cosmology).
- Morris–Thorne with arbitrary `b` = classical exotic matter (fully
  speculative).
- MMP = Casimir-like quantum stress in higher-D + monopole + BSM
  fermions (borderline plausible existence proof).
- Damour–Solodukhin = small NEC at throat, tunable by `λ`.
- Visser thin-shell = surface stress-energy concentrated on a 2-surface.

**MMP scaling math the simulator must surface live `[B02 §2, B10 §1]`:**
- Throat radius `r_e ~ q · l_P · √(α_em/π)`.
- Holding open requires `N_f ≳ q` charged-fermion species.
- 1m throat → `q ~ 10²⁹–10³²` Dirac units, `M ~ 10²³ kg` per mouth (B02)
  to `~10⁷ M_⊕` Saturn-mass with optimization (B10 — small numerical
  disagreement, both flagged `[unverified]`).
- Internal proper time `τ_int ~ L_throat/c` (seconds for meter throat).
- External time `T_ext ≫ τ_int`, boost factor huge → no closed timelike
  curves form provided mouths stay sub-light.

**Three failure modes the sim must visualize `[B02 §6]`:**
1. Semiclassical backreaction: ⟨T_{μν}⟩ as 1-loop quantity feeds
   Einstein eqs linearly; perturbations have positive feedback in most
   geometries; throat collapses on timescale `r_0/c`. MMP claims
   1-loop stability; 2-loop open.
2. QI squeeze: §1.3 above.
3. Chronology protection: moving mouths produces CTCs; vacuum
   polarization diverges on would-be Cauchy horizon and destroys
   wormhole. Only escape = mouths nearly co-moving forever.

**Cost:** §1.3 voxel + closed-form parameter calculator. MMPParameters
config object `[B10 §6a]` ~50 lines TS with derived quantities.

**Verification:** UI sliders for `(q, N_f, M, r_e, T_ext, τ_int)` must
red-flag when user leaves regime where 1-loop calculation is controlled
`[B10 §5]`.

---

### 1.5 Magnetostatic FE solver (Prat-Camps replica)

**Brief sources:** B03 §5, B05 §5 mode A, B09.

**Equations:** `∇×(μ⁻¹ ∇×A) = J + ∇×M`, `B = ∇×A`, on tetrahedral mesh
with first-order Nédélec edge elements (vector A is naturally edge-
based; avoids spurious modes) `[B03]`. Backend: Python + scikit-fem
or compiled C++ (MFEM / FEniCS bindings). Real-time on small meshes
(~50k tets); precompute for large.

**Material library — nonlinear B-H `[B03]`:** mu-metal (saturation at
`B_sat ≈ 0.7–0.8 T`), soft iron, ferrite, NdFeB (hard remanence `M_r`,
coercivity `H_c`), Type-II SC (London regime, `μ_r → 0` above `H_c1`,
penetration depth `λ_L`). Mu-metal **cannot** be modeled as constant
`μ_r = 50000`; use piecewise B(H) curve and Newton iteration. Pull
B-H data from Magnetic Shield Corp. MuMETAL data sheets, fit tanh.

**Eddy-current / quasi-static AC mode `[B03 §5 feature 5]`:**
`∇×(σ⁻¹ ∇×H) + jωB = 0` in conductors. Lets user sweep frequency, watch
SC cloak fail above corner frequency. Tells build team whether AC
modulation idea works before any tape is bought.

**Transformation-optics layer designer `[B03 §5 feature 4]`:** user
specifies coordinate transform (punch hole between A and B); solver
computes required `μ_r` tensor field via Jacobian `μ' = J·μ·J^T / det(J)`.
Display where this exceeds physical bounds (`μ_r > 100k` impossible at
room T; `μ_r < 0.001` needs SC) → highlights what's buildable vs.
transformation-optics fantasy.

**Cost:** ~50k-tet mesh real-time on a CPU `[B03]`; one-shot via
magpylib for analytic shell, or FEMM/ngsolve for full 3D `[B05]`.

**Verification:** field at far mouth must match published Prat-Camps
Sci. Rep. 5:12488 figures within ~5% `[B05]`. Ship the comparison plot
in `docs/validation/magnetic_wormhole.png`. Independent FE validation
via Mager 1968 cylindrical-mu-metal shielding-factor analytic formula
on benchtop chamber must agree within 30% `[B09 §8 expt B]`.

---

### 1.6 MHD solver (plasma toroid scene)

**Brief sources:** B06.

**Equations (ideal MHD)** `[B06 §5 F1]`:
```
∂ρ/∂t + ∇·(ρv) = 0
∂(ρv)/∂t + ∇·(ρvv + p* I − BB/μ₀) = 0      p* = p + B²/(2μ₀)
∂B/∂t − ∇×(v×B) = 0                         (∇·B = 0 maintained)
∂E/∂t + ∇·[(E+p*)v − B(v·B)/μ₀] = 0
```

**Solver:** Godunov-type HLLD Riemann (Miyoshi & Kusano 2005), same as
Athena/Athena++ (Stone et al. 2008, 2020). Constrained transport on
staggered B for `∇·B`. Target 128³ grid → ~30 fps mid-range GPU.
~5000 lines of WGSL + ~2 weeks engineering. Memory at 128³×8 fields×fp32
≈ 64 MB.

**Initial conditions:**
- F1 — analytic FRC equilibrium (Rigid-rotor or Hill's vortex) with
  Balmer-α emissivity proxy `∝ n_e n_H × T_e^{-1/2}` (recombination)
  or simple `n²` for a pretty proxy.
- F2 — 2D Harris current sheet `B_x(y) = B_0 tanh(y/L)`, perturb,
  watch X-point form. Tracks against Yamada/MRX (Princeton
  Reconnection Experiment) figures, Yamada–Kulsrud–Ji RMP 2010.

**Reconnection topology disclaimer (mandatory side-panel text)
`[B06 §2, §5]`:** "this is field-line topology change, not spacetime
topology change — see GR brief §1." Coordinate with Hana before F2 ships.

**Cost:** F1 ~2 weeks; F2 trivial extension of F1 (3 days, same solver,
different IC, plus a connectivity tracer).

**Verification:** F1 against published FRC equilibrium profiles
(SSPX, TAE C-2W params); F2 against Sweet–Parker reconnection rate
scaling `S^{-1/2}` (Lundquist number).

---

### 1.7 BEC analogue (Gross–Pitaevskii)

**Brief sources:** B05 §5 mode B, B09 §5.

**Equations:** 1D Gross–Pitaevskii, split-step Fourier, 256-grid, with
step potential evolving condensate into black-hole-laser configuration.
CPU-cheap, no GPU.

**Plot:** density-density correlation `g⁽²⁾(x, x')`, look for anti-
diagonal Hawking-correlation feature reported in Steinhauer 2016 fig. 2.

**Verification `[B09 §5]`:** correlation amplitude at anti-diagonal peak
within 10% of Steinhauer 2016 published figure. **This is the only
honest BEC claim** — the experimental BEC apparatus is out-of-scope
(see §6 hard-NO), so the simulator reproducing the published g⁽²⁾ is
the entire deliverable.

---

### 1.8 Quantum information / SYK + GJW protocol

**Brief sources:** B07, B10 §3.

**6a — Two-mouth wormhole with simulated entanglement `[B07 §6a]`:**
two BTZ-like mouths side-by-side, each "decorated" with N qubits whose
pairwise entanglement (from stored density matrix or TFD-like state) is
drawn as a thread bundle through the throat. Thread density at radius
`r` ∝ mutual information `I(A_L : A_R)`. Map to thread color/density
via `1 - exp(-I)`. **GPU cost:** O(N²) for mutual-info matrix; N≤64 →
~4k cells, ~30µs/frame.

**6b — GJW slider `[B07 §6b, B10 §6c]`:** UI slider = double-trace
coupling `g`. As `g` crosses zero, sim integrates perturbed null
geodesic, shows horizon retreating off geodesic for finite window.
Closed-form for BTZ from arXiv:1608.05687 §3. Render traversal window
as shaded region on Penrose diagram inset. **Bandwidth counter
displays `log₂(traversed qubits)` and greys out when QI or causal-
shortcut bounds are saturated.** `[B07]` Crucial: sim gates traversal
on user enabling boundary coupling — visualizes that the wormhole
doesn't transmit anything until the boundaries communicate classically.
Kills FTL misconception more effectively than any caption.

**6c — Holographic-dual visualizer `[B07 §6c]`:** split-view, left =
AdS₂×S² (or AdS₃) bulk with embedded wormhole; right = boundary as 1D
circle of qubits with per-pair entanglement chord diagram (Ryu–
Takayanagi style). Drag a chord on boundary → corresponding RT minimal
surface lights up in bulk. RT surfaces in pure AdS₃ closed-form;
back-reacted geometry uses §1.2 integrator on `t=const` slice.

**Honest labeling (mandatory) `[B07 §5]`:** simulator's ER=EPR/GJW mode
labeled "holographic visualization of quantum-circuit correlations,"
NOT "we simulated a spacetime wormhole." The Sycamore/Jafferis 2022
result is contested by Kobrin–Schuster–Yao (Nature 638, 2025) and
the technical argument largely went their way for the N=7 instance.

**Software-side experiment `[B07 §7c]`:** classical SYK_q=4 simulator,
N up to ~24 Majoranas (Hilbert dim ~4096/side, 16M total), via
`dynamite` or `qutip-jax`, Colab-free-tier viable. Establishes the
classical-simulable baseline against which any quantum-hardware result
must be compared. **Run this baseline before quoting any hardware run.**

---

### 1.9 Higher-dimensional / brane visualizers

**Brief sources:** B10.

**MMPParameters config object `[B10 §6a]`:** `(q, N_f, r_e, d, M_mouth,
α_em)` with derived `q_min_for_traversability`, `T_ext_per_τ_int`,
`tidal_g`, `is_one_loop_controlled` boolean. Analytic
`r_e = q · l_P · √(α_em/π) / 11`.

**RS2Geometry class `[B10 §6b]`:** bulk `ds² = e^{-2|y|/ℓ} η_{μν} dx^μ
dx^ν + dy²`. Brane wormhole shape function from Bronnikov–Kim
(gr-qc/0212112). Effective `E_μν` on brane computed from bulk Weyl
tensor. Energy-condition HUD shows `T_μν^brane` (positive, green) AND
`E_μν` (sign-indefinite, colored). **This is the single best teaching
tool for "where does the exotic matter live."**

**Visual scene:** render warped extra dimension as actual visible axis
(RS-II warp factor `e^{-|y|/ℓ}` shown as vertical squish), thin brane
at `y=0`, user worldline on brane, throat reaches into bulk.

**Cost:** geodesic integration in extremal RN + AdS₂×S² near-horizon
gluing closed-form in conformal coords (AdS₂ Poincaré
`ds² = (-dt²+dz²)/z²`); ~50 lines on top of generic GR integrator
`[B10 §5]`. ~80 lines for brane scene. GPU ~1.5× Ellis fragment cost
for MMP, ~2× for brane scene.

**Verification:** UI tuple `(q, N_f, M, r_e, T_ext, τ_int)` must red-
flag outside controlled regime; experimental-search status overlay
shows current null bounds (MoEDAL monopole mass `> 3.9 TeV`, IceCube
relativistic monopole flux `< 2×10⁻¹⁹ cm⁻² s⁻¹ sr⁻¹`, Eöt-Wash
`R_extra < 44 µm` for n=1, LHC ADD `M_* > 10–11 TeV` for n=2).

**Cut order `[B10 §7]`:** if engineering budget forces choice between
MMP/brane/ER=EPR scenes vs. analogue/magnetic/quantum-info scenes,
ship benchtop-anchored ones first. Cut brane-world 5D scene first
(highest GPU cost, narrowest pedagogy). Keep MMP (highest
pedagogy/line). Keep ER=EPR (cheapest, biggest misconception-killer).

---

## 2. Scenes

Each scene maps onto one or more modules from §1.

| # | Scene | Modules | Notes |
|---|---|---|---|
| S1 | **Morris–Thorne textbook** | §1.1, §1.2, §1.3 | Default onboarding scene. Closed-form Christoffels. LUT-based for static demo. Illustrates "fails QI — show user why" `[B02 §implementation]`. |
| S2 | **Ellis drainhole** | §1.1, §1.2, §1.3 | Closed-form, validates integrator (Einstein-ring radius is the single best test). Two HEALPix sky maps for the two asymptotic regions `[B01 §4]`. |
| S3 | **Teo rotating** | §1.1, §1.2 | Frame-dragging. Compute pass needed (no axisymmetry tricks). Live integration only `[B04]`. |
| S4 | **MMP humanly traversable** | §1.1, §1.4, §1.9 | Render AdS₂×S² near-horizon, magnetic-flux Hopf-fiber arrows, redshift gradient on starlight, external/proper clock pair. Constraint visualizer not construction blueprint `[B10 §5]`. |
| S5 | **Damour–Solodukhin foil** | §1.1, §1.2 | Black-hole shadow + late-time photon echoes. Closest metric to current LIGO/EHT science `[B01 §1e]`. |
| S6 | **Casimir cell** | §1.3, §1.5 | µm-scale parallel plates, `ρ_Casimir` overlay. Pedagogical "works at µm scale, throat too small to be a stargate" preset `[B02]`. |
| S7 | **Prat-Camps magnetic-wormhole replica** | §1.5 | Three-shell geometry (mu-metal hose / SC shell / outer mu-metal compensator). Magnetostatic FE, field-line streamlines, "Prat-Camps mode" toggle on/off animates topology change `[B03 §5 feature 3]`. |
| S8 | **Plasma toroid (FRC)** | §1.6 | Ideal MHD on 128³ grid, Balmer-α emissivity proxy. The visual the property is named after. `[B06 §5 F1]` |
| S9 | **Reconnection X-point** | §1.6 | 2D Harris sheet → X-point. Connectivity-tracer colors field lines from each domain. Mandatory disclaimer: "field-line topology change, NOT spacetime topology change" `[B06 §5 F2]`. |
| S10 | **ER=EPR two-mouth** | §1.8 | Two BTZ mouths + thread-bundle through throat, GJW slider, classical-coupling gate on traversal `[B07 §6, B10 §6c]`. |
| S11 | **Brane RS-II** | §1.9 | 5D embedding with visible warp, brane at `y=0`, throat into bulk, Bronnikov–Kim brane wormhole shape function, dual energy-condition HUD `[B10 §6b]`. |
| S12 | **BEC sonic horizon** | §1.7 | 1D Gross–Pitaevskii, density-density correlation panel. "Press play, watch Hawking radiation appear" `[B05 §5 mode B]`. |
| S13 | **Visser thin-shell** (optional, Tier-3) | §1.1, §1.2 | Geodesics refract discontinuously crossing the surface. Pedagogically clean `[B01 §1f]`. |

**Visual references to match in CI:**
- James et al. 2015 Figs. 6, 10, 15 (arXiv:1502.03809) for Ellis-class
  lensing.
- Müller (2008) MT lensing image for verification test #4 `[arxiv ID
  unverified per B04 §8]`.
- Steinhauer 2016 g⁽²⁾ fig. 2 for BEC.
- Prat-Camps Sci. Rep. 5:12488 figures for magnetic wormhole.

---

## 3. Diagnostics & HUDs

| HUD | What it shows | Source brief | Cost |
|---|---|---|---|
| **Energy-budget readout** | live `E_neg(t)`, `Q_QI(t)`, "WORMHOLE VIABLE" badge gated on ANEC violation | B02 §5b, B01 §5 | Free |
| **ANEC integrand plot** | 1D curve of `T_{μν} k^μ k^ν` along central null geodesic, integrated value, 8 sample geodesics for radial profile | B02 §5c, B01 §5 (energy-condition HUD) | Free |
| **Kretschmann scalar field** | volumetric 64³ overlay of `K = R_{μνρσ}R^{μνρσ}`, contour shells where curvature is dangerous; closed-form for MT, ~10 µs static / ~0.5 ms/frame dynamic | B04 §5b | 1–2 days impl |
| **Time-dilation accumulator** | `dτ/dt = √(-g_{μν} u^μ u^ν)`, accumulated proper τ vs. lab t, HUD clock pair | B04 §5c, B01 §4 | 1 hr impl |
| **Local energy-condition tensor** | per-voxel NEC check `T_{μν} k^μ k^ν ≥ 0` for null `k`, voxels in red where violated; for MT throat: `ρ + p_r = -b'/(8π r²)` < 0 | B04 §5d | 1 day impl |
| **Embedding-diagram side panel** | 2D `(r, z)` Flamm-style embedding of `t=const, θ=π/2` slice with user geodesic in real time; for Ellis: `z(r) = b₀·arcsinh(r/b₀)` | B01 §5 | – |
| **Sensor overlay** | virtual probe (Hall, fluxgate, OPM, photodiode) at user-dragged point. FE-solver field + realistic noise: 1/f flicker + white floor at spec'd nT/√Hz + 60 Hz mains pickup + ADC quantization. Output trace looks like AlphaLab/Bartington output, not a clean curve. | B09 §7 feature 1 | ~200 lines NumPy |
| **Calibration-routine simulator** | walks user through zero-Gauss zeroing, Helmholtz span check, gradiometer common-mode rejection. Returns calibration certificate JSON (slope, offset, residual, χ²) | B09 §7 feature 2 | – |
| **Sensitivity calculator / claim killer** | inputs: experiment config + instrument pick + integration time + shielding. Returns SNR three-line verdict color-coded green/yellow/red. **Every experiment in this program must pass through this calculator before parts are bought.** | B09 §7 feature 3 | – |
| **Lab-budget mode** | drag-in component palette `{LN2_dewar, cryocooler_PT410, roughpump_DIY, turbo_pfeiffer_HiPace80, ionpump_60Ls, chamber_3DP, chamber_CF6, vibration_isolation_passive, MEMS_accel, OPO_bench}` with `(T_min, P_min, bandwidth, cost_used, cost_new, power_W, noise_floor, apartment_safety_flag)`. Greys-out experiments whose `T_required` or `P_required` is unmet. **Highest-leverage pedagogical feature — the one that says "no, you can't, here's why."** | B08 §6a | – |
| **Vacuum pump-down curve simulator** | three regimes (viscous / transitional / molecular) with Knudsen handling; `Kn = λ/D`, `λ = k_B T / (√2 π d² P)`, outgassing dominates below 10⁻⁶ Torr with `P_outgas = q·A/S` per material (SS unbaked 10⁻⁹ Torr·L/s/cm², baked 10⁻¹², viton 10⁻⁷, PETG print 10⁻⁵) | B08 §6b | – |
| **Cryogen consumption simulator** | bath cryostat boiloff `dV/dt = (Q_load+Q_rad+Q_cond)/(ρ·L_v)` (LN₂ ρ·L_v=161 kJ/L, LHe 2.6 kJ/L); closed-cycle electricity `P_compressor·t·$/kWh`; break-even plot | B08 §6c | – |
| **MMP parameter constraint visualizer** | live `(q, N_f, M, r_e, T_ext, τ_int)` tuple, red flashes outside 1-loop-controlled regime, monopole flux integral `∫B·dA = 2π q/e`, LLL fermion zero-mode count `2qN_f` | B10 §5, §6a | – |
| **GJW bandwidth counter** | `log₂(traversed qubits)` per traversal, greys out at QI / causal-shortcut bound saturation | B07 §6b | – |
| **Cosmetic plasma-sheath shader** (off by default, opt-in only, labeled "non-physical aesthetic overlay") | screen-space glow on wormhole throat using Langmuir-Child `j ∝ V^{3/2}/d²` proxy. Respects "no entrance shimmer" rule via opt-in + label. Disabled in validation harness. | B06 §5 F3 | 1 day |

---

## 4. Hard `[unverified]` flags

Every claim across the briefs that came in flagged `[unverified]`. Listed
with which brief raised it. **None of these may be silently laundered
into customer-facing copy.** Maya/QA must verify before public quote.

- B01: **Riazuelo 2008 specific arXiv ID** — he publishes mostly in
  proceedings; cite imagery directly. Validate against his published
  imagery, not the wrong paper.
- B01: **Bronnikov 1973 *Acta Phys. Pol. B*** — paginated print only,
  no arXiv.
- B01: **Lobo arXiv:0710.4474** — Lobo has many wormhole papers; the
  modified-gravity review the brief had in mind is arXiv:0907.1390 but
  verify before quoting.
- B02: **Sparnaay 1958 DOI** — flagged in draft.
- B02: **Vahlbruch et al. 15-dB squeezed light, PRL 117, 110801 (2016)**
  — arXiv ID unverified.
- B02: **General [unverified] disclaimer** — items in §7 not re-checked
  from primary source in the brief; flag for Maya/QA before any public
  quote.
- B03: **Steinhauer Nature 569, 688 (2019)** — user cited
  arXiv:1809.00913; canonical follow-up is arXiv:1910.09363
  ("Observation of stationary spontaneous Hawking radiation"). Brief
  flags arXiv ID unverified.
- B03: **Nat. Comms 2025 doi:10.1038/s41467-025-63981-3** — "wormhole
  claim" scope flagged unverified.
- B04: **Riazuelo 2008 link luth.obspm.fr/~luthier/riazuelo/** —
  unverified, confirm before citing.
- B04: **Müller (2008) Am. J. Phys. 72, 1045 / arXiv:gr-qc/0402071** —
  Müller has multiple wormhole-vis papers; double-check arXiv ID before
  shipping verification test #4.
- B05: **Moisy/Rabaud/Salsac 2009 Exp. Fluids 46, 1021** — specific page
  numbers unverified; method itself well-established.
- B07: **Maldacena & Stanford "Remarks on SYK" arXiv:1604.07818** —
  cite for SYK background, unverified for our specific use.
- B07: **Gao, "Commuting SYK and pseudo-holography," 2024** — arXiv ID
  unverified, flagged from secondary report; confirm before public quote.
- B08: **Compressed Gas Association P-39** — verify edition before quote.
- B08: **General `[unverified]` disclaimer** — items not cross-checked
  against primary source this session; flag for Maya/QA before public
  quote. Specifically Maya was asked to verify CGA P-39 edition and the
  LHe expansion ratio (745×) against a 2025 datasheet.
- B09: **TI DRV5055 noise floor in nT/√Hz** — derive from datasheet,
  not directly cited.
- B09: **Thorlabs EDU-MINT2/M Michelson kit price** — unverified 2026
  price.
- B09: **Leo Bodnar Mini-Precision GPSDO** — verify product still
  listed 2026.
- B09: **General `[unverified]` tags** flag prices/specs not directly
  confirmed; verify at quote time.
- B10: **Eöt-Wash 38 µm bound for n=2** — verify against latest
  Eöt-Wash results page before public quote.
- B10: **CMS 2025 single-photon+MET HEPData ins3085605** — specific
  limit improvements unverified; quoted CMS press-release figure of
  10% enhancement.
- B10: **Casadio, Ovalle et al. gravitational decoupling for brane
  wormholes** — many recent refs; pick one canonical for the
  simulator before quoting; flagged for Maya.
- B11: **NFPA 70E specific edition** — verify against 2024 ed. before
  quoting; principle is current.
- B11: **General `[unverified]` markers** call out where principle is
  current but section/edition numbers should be verified before audit
  context.

---

## 5. Anti-features (do not do this)

All "kill" / "do not" / "no" rules across briefs, collected here. Every
one is binding.

**Rendering / GR (B01 §5, B04, B06):**
1. **No lens-flare "swirly tunnel" effect.** Not a geodesic structure;
   if we want a tunnel look it must come from actual gravitational
   lensing of a structured background, not screen-space shaders `[B01]`.
2. **No FTL traversal animations.** Even traversable wormholes don't
   transmit information FTL in ambient space (MMP is explicit). UI
   suggesting "1 ly in 5 seconds external" is physically wrong; show
   long-external / short-proper time asymmetry instead `[B01]`.
3. **No "entrance shimmer" / particle effects at the throat.** Real
   throats in classical solutions are smooth. The only physical
   "shimmer" is Hawking-like radiation, undetectably faint. Don't
   fake it `[B01]`. The plasma-sheath shader (§3) is opt-in and
   labeled "non-physical aesthetic overlay" specifically to respect
   this `[B06 §5 F3]`.
4. **No fp16 in Christoffels.** Destroys energy conservation within
   ~50 steps `[B04 §3]`. fp16 ok in skybox-sample stage only.
5. **No runtime autodiff.** 3–5× cost vs. closed-form; only worth it
   when prototyping new metrics `[B04 §2]`.

**Plasma / fringe physics (B06 §4, §7):**
6. **No Heim drive mode.** Theory firmly fringe; predictive failures
   catalogued; mass formulas had hand-tuned fitting parameters; nothing
   reproduced under blind tests `[B06 §4]`.
7. **No Tajmar gravitomagnetic London-moment effects in GR module.**
   No successful independent replication in 20 years; mainstream
   consensus = artifact (likely thermal/mechanical accelerometer
   coupling) `[B06 §4]`.
8. **No EmDrive mode toggle.** Definitively falsified by Tajmar's own
   group at TU Dresden 2021 — zero thrust above 0.1 µN at up to 100 W
   input. Closed file. Do not platform `[B06 §4]`.
9. **No "ionizing the vacuum to make exotic matter" mode** `[B06 §7]`.
10. **No reconnection-as-wormhole framing.** Reconnection is field-
    line topology change in Euclidean 3-space; spacetime manifold is
    unaffected. Mandatory disclaimer on F2 scene. Coordinate disclaimer
    language with Hana before ship `[B06 §2]`.

**Quantum-info honesty (B07 §5):**
11. **Do not label ER=EPR / GJW mode as "we simulated a spacetime
    wormhole."** Label honestly as "holographic visualization of
    quantum-circuit correlations" `[B07 §5]`.
12. **Do not quote a Sycamore-style hardware run without first running
    the classical-simulable baseline (B07 §7c).** Every hardware claim
    must be overlaid on the simulator's predicted curve.

**Implementation discipline (B09 §1.7):**
13. **No claim-sized confidence bars without instrument noise floor.**
    Sensor-overlay must add realistic 1/f flicker + white floor + mains
    pickup + ADC quantization to FE-solver output. Output looks like
    real AlphaLab/Bartington trace, not a clean curve `[B09 §7]`.
14. **No experiment claim leaves the program before sensitivity
    calculator (§3) returns SNR ≥5σ.** "Sensors before sources.
    Calibration before claims." `[B09 §9]`
15. **Casimir-force experimental measurement in the apartment is
    out-of-scope.** State explicitly in brief and README. Sim renders
    Lifshitz `F ~ ℏcπ²/(240 d⁴)` curve only `[B09 §4]`.
16. **BEC analogue experimental claim is out-of-scope.** Sim
    reproduces Steinhauer 2016 published g⁽²⁾ figure from
    Gross–Pitaevskii integrator only. That is the only honest claim
    `[B09 §5]`.

**Cryo / vacuum (B08 §7):**
17. **No UHV bake-out** (10⁻¹⁰ Torr requires 150–250 °C / 3–7 days /
    500–1500 W heater tape — fire risk on residential surfaces, not
    unattendable) `[B08 §7]`.
18. **No high voltage in tank vacuum >1 kV.** X-ray generation at
    5–30 kV. Hard no with child in house `[B08 §7]`.
19. **No mercury for diffusion pumps** (banned NY State residential).
    No ³He fridge apparatus. No lithium metal for any BEC variant
    `[B08 §7]`.
20. **No dilution-fridge / 10 mK / sub-K work in apartment.** Partner
    or no-go `[B08 §1]`.

**Lab safety / SOP (B11 §8):**
21. **Hard NO on HV pulse capacitor banks (>10 J at >100 V).** Chest-
    path discharge at this energy is a clinical cardiac event. No
    apartment mitigation survives a single muscle slip `[B11 §8]`.
22. **Hard NO on first-ever LN₂ pour without a remote witness on live
    call + O₂ meter on bench** `[B11 §8]`.
23. **Hard NO on any laser ≥Class 3B (>5 mW) or any RF source >100 mW
    in apartment** `[B11 §8]`.
24. **Hard NO on synthesizing YBCO from precursors** (950 °C tube
    furnace, toxic dust). Buy disks `[B08 §7, B03 §6]`.
25. **Hard NO on ablation experiments in apartment** (sub-µm
    particulate, no hood). University bench only `[B11 §1`item 9]`.
26. **No live experiments in shared living space when daughter is home
    and awake.** Lab room only `[B11 §2]`.

**Honesty discipline (general):**
27. **Every metric in UI must show its loophole tag** (phantom scalar,
    Casimir, classical exotic, modified-gravity, higher-D). This is a
    teaching tool, not a vibe `[B01 §2]`.
28. **Do not silently re-use "wormhole" between magnetic-field
    transformation-optics, reconnection, ER=EPR holographic, and
    spacetime contexts.** Label each `[B05, B06, B07]`.

---

## 6. Per-module cost summary

| Module | From brief | Implementation cost | Verification recipe |
|---|---|---|---|
| Spacetime metrics library | B01, B04, B10 | ~50–80 LOC WGSL per metric (codegen) | §1.2 closed-form harness |
| Geodesic integration (RK4 + symplectic) | B01, B04 | core ~500 LOC; per-metric Christoffels closed-form | 5 CI tests in §1.2 |
| Energy-condition / `T_{μν}` voxel field | B01, B02, B04 §5d | ~1 day for visualization | NEC sign check vs. closed form |
| Exotic-matter sources (Casimir, squeezed, MMP) | B02 | static analytic methods, ~few hundred LOC | match published ρ vs. d curves |
| MHD solver F1 | B06 | ~5000 LOC WGSL, ~2 weeks | FRC equilibrium params |
| Reconnection F2 | B06 | ~3 days extension of F1 | Sweet–Parker rate |
| Magnetostatic FE | B03, B05 | ngsolve/scikit-fem; ~50k tets real-time | Prat-Camps figs ±5%; Mager 1968 ±30% |
| BEC GP integrator | B05, B09 | 256-grid 1D, no GPU, ~few days | Steinhauer 2016 g⁽²⁾ ±10% |
| ER=EPR / SYK / GJW | B07, B10 | ~50 LOC TFD evolution; bandwidth counter | classical SYK baseline (B07 §7c) |
| MMP scene | B10 | ~50 LOC over generic GR | MoEDAL/IceCube/Eöt-Wash live-bound overlay |
| Brane RS-II | B10 | ~80 LOC | dual energy-cond HUD vs. Bronnikov–Kim |
| Lab-budget mode (component palette) | B08 §6a | TS UI + per-component spec table | – |
| Sensor-overlay + sensitivity calc | B09 | ~200 LOC NumPy noise + UI | every experiment must pass through |
| Vacuum pump-down + cryogen sims | B08 §6b–c | – | Knudsen crossover plot pedagogy |

**Stack target:** Three.js r170+ on WebGPU, fragment-shader raymarcher
per pixel, small WGSL compute pass for tabulated quantities `[B04 §1]`.
WebGL2 fallback for Linux-Chrome and pre-Tahoe Mac/iOS until Q3 2026.
Rust→WASM only for offline verifier and CI tests; do not put runtime in
WASM (round-tripping float buffers GPU↔WASM each frame is the slowest
possible architecture). Performance target: 60 fps locked @ 1080p on
RTX 3060 for Morris–Thorne; mid-range integrated graphics 30–45 fps;
expose "step budget" slider `[B04 §3]`.
