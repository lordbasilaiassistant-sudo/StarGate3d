# Brief 04 — Computational GPU & Geodesic Integration

**Author:** Dr. Tomas Lindqvist (computational physicist, NR + real-time GR rendering)
**Audience:** StarGate3d team
**Scope:** how to actually run the wormhole physics on a browser GPU at >20 fps without faking the optics. Concrete enough to start coding from.

---

## 1. Recommended browser stack

**Default: Three.js r170+ on WebGPU, fragment-shader raymarcher per pixel, with a small WGSL compute pass for tabulated quantities.**

WebGPU is now baseline. As of Jan 2026 it ships stable in Chrome/Edge (Win/macOS/CrOS, Android 12+ with Qualcomm/ARM), Firefox 141+ (Win) / 145+ (macOS Apple Silicon, Tahoe 26), and Safari 26 (macOS Tahoe 26, iOS 26, iPadOS 26, visionOS 26). Linux Chrome is still rolling (144 beta, Intel Gen12+). Android Firefox still flagged. So: target WebGPU first, ship a WebGL2 fallback for Linux-Chrome users and pre-Tahoe Mac/iOS until Q3 2026.

Decision tree for the rendering layer:

| Situation | Pick |
|---|---|
| Static-ish wormhole, light only, Morris–Thorne | Three.js + WebGL2, single fragment shader. WebGPU buys little here. oseiskar/black-hole proves the approach. |
| Mixed light + matter geodesics, time-varying scene, multiple metrics | Three.js + WebGPU. WGSL fragment shader for primary lensing pass, **compute shader** for matter trajectories and tidal/Kretschmann field, shared storage buffers between them. |
| Rotating Teo wormhole, no axisymmetry tricks available, dynamic throat | Three.js + WebGPU + compute. Fragment-only will run out of registers/uniform space. |
| You want to share the integrator with a CPU verifier or run headless tests | Rust → WASM (via `wgpu` or `wasm-bindgen`) for the integrator core, JS wrappers for Three.js. Same WGSL shader source on both sides. |

**Rust+WASM is needed when:** (a) we want bit-identical results between offline test runs and the GPU shader, or (b) we are integrating massive-particle trajectories at sub-frame resolution and want CPU/SIMD as fallback for low-end devices, or (c) we're shipping a verifier (see §6) into CI. Otherwise it's overkill — TypeScript driving WGSL is plenty.

**Fragment-only suffices** for stationary axisymmetric metrics where the screen-space lensing reduces to: per-pixel ray, integrate geodesic, sample skybox / second-universe cubemap. This is Morris–Thorne and Schwarzschild. **Compute is required** when (i) we need ping-pong state larger than what fits as varyings, (ii) we need particles with persistent state across frames, (iii) we're computing volumetric fields like Kretschmann at voxel grid resolution, or (iv) we want hierarchical step-size adaptation with workgroup-scoped reduction.

---

## 2. Geodesic integration on GPU

**The integrator: classical RK4 in 8D phase space `(x^μ, p^μ)`** with affine parameter λ. Symplectic integrators (leapfrog, Verlet) are tempting but the geodesic equation `dp^μ/dλ = -Γ^μ_{αβ} p^α p^β` is not separable in canonical form once you go off-diagonal, so RK4's accuracy-per-RHS-eval beats leapfrog here for the precision we need (Riazuelo and DNGR both used RK-style integrators; James et al. 2015 §3 confirms an adaptive RK).

**Where to run it:**

- **Fragment shader RK4 (the default for primary rays):** one ray per pixel, ~200–800 RK4 steps to get from camera through throat to far-side skybox sample, ~16 multiply-adds per Christoffel evaluation for Morris–Thorne. Fits comfortably in a single draw call. This is what oseiskar/black-hole does for Schwarzschild.
- **Compute shader RK4 (for everything else):** matter particles, secondary rays (refraction off accretion disk), tidal-tensor sampling on a voxel grid. One workgroup per particle batch, persistent state in storage buffer, integrate forward by Δλ each frame, keep history for trajectory ribbons.
- **WASM-host loop:** only for the offline verifier and for CI tests. Don't put the runtime in WASM — round-tripping float buffers GPU↔WASM each frame is the slowest possible architecture.

**Step-size adaptation:** in flat asymptotic regions take big steps, near the throat take small steps. Standard recipe: estimate local curvature scale `L = 1 / sqrt(K)` where K is Kretschmann, set step `Δλ = α · L / |p|` with α∈[0.05, 0.2]. For Morris–Thorne with shape function `b(r) = b0² / r`, K is closed-form and cheap, so no autodiff needed. For metrics where K isn't closed-form, fall back to embedded RK4(5) with FSAL (Fehlberg) — keep an error estimate, halve step on tolerance breach, double it after N consecutive accepts. In a fragment shader, "step halving" means substepping inside the integration loop body; per-pixel divergence is fine because adjacent rays mostly take the same number of steps.

**Christoffel symbols for Morris–Thorne — closed form, do NOT autodiff.** The metric

`ds² = -dt² + dr² + (b₀² + r²)(dθ² + sin²θ dφ²)`

(coordinate `r` is the proper radial distance, not Schwarzschild r) has only a handful of nonzero Christoffels:

- `Γ^θ_{rθ} = Γ^φ_{rφ} = r / (b₀² + r²)`
- `Γ^r_{θθ} = -r`
- `Γ^r_{φφ} = -r sin²θ`
- `Γ^θ_{φφ} = -sin θ cos θ`
- `Γ^φ_{θφ} = cot θ`

That's it. Inline them in WGSL as a single function returning the four nonzero `dp^μ/dλ` components. ~30 FLOPs per RHS eval. For more general shape functions (Ellis drainhole, Teo rotating, MMP-stabilized), keep them as analytic templates — write a small Mathematica/SymPy script that emits WGSL, run it once per metric, commit the generated shader. Runtime autodiff (forward-mode through a metric function) costs ~3–5× a closed-form eval and is only worth it when prototyping new metrics.

**Reference implementations to read:** oseiskar/black-hole (`raytracer.glsl` is the template), rantonels/starless (numpy, but the integrator is clear), peabrainiac/black-hole-renderer (WebGL Schwarzschild), bytebat/TraceIt (GR raytracing sandbox, modified Ellis wormhole — closest to our use case).

---

## 3. Performance budget, 1920×1080@60 on RTX 3060

Target: 16.6 ms/frame, primary lensing pass should fit in <10 ms to leave headroom for UI, post, particles.

Per-pixel cost: 200–800 RK4 steps × ~30 FLOPs Christoffel × 4 stages = 24–100 kFLOPs/pixel for primary rays. At 1080p that's 50–200 GFLOPs/frame. RTX 3060 delivers ~13 TFLOPs FP32, so theoretical lower bound is 0.4–1.5 ms. Realistic: 4–9 ms once you factor occupancy, register pressure, divergent step counts, and skybox sampling. **Bottleneck is register pressure / occupancy, not ALU.** RK4 in 8D wants 32+ live floats per stage; on Ampere this caps occupancy and makes memory-latency hiding worse.

Mitigations: (a) cap steps at 600 with a safety termination, (b) use mediump (fp16) only in the skybox sample stage, never in the integrator — fp16 in Christoffels destroys energy conservation within ~50 steps, (c) tile the screen and skip pixels that hit the throat bowl directly (pre-pass), (d) for second-universe rays, reuse the same shader with a sign-flipped coordinate.

Expected delivered numbers on a 3060 at 1080p, Morris–Thorne, no matter:
- Primary lensing pass: 5–7 ms
- Tidal/Kretschmann visualization (when on): +2 ms
- Matter particles (compute): 0.2 ms per 10k particles
- Three.js scene + UI: 1–2 ms

So ~10 ms total → 100 fps headroom, drop to 60 fps locked with vsync. Mid-range integrated graphics (Iris Xe / M1 base) will hit 30–45 fps; we should expose a "step budget" slider.

---

## 4. Visual fidelity vs. speed tradeoffs

**LUT (lookup table) approach for stationary axisymmetric metrics.** Morris–Thorne and Ellis are spherically symmetric → for a given camera radius `r_cam`, the deflection function `α(impact_param)` is a 1D function. Precompute α at 1024 impact parameters, sample at runtime. James et al. 2015 (§3, "ray-bundle integration") used precomputed maps for Kerr — same idea. For our case the LUT is much smaller (1D not 4D) because of the symmetry. Build it once on app load with a compute pass, then primary rays become a single texture lookup + skybox sample. Expected speedup: ~30–50× over per-frame integrate. Caveat: any time the camera moves radially, you regenerate or sample-with-blend along a 2D LUT (r_cam, b). Still cheap. **For Morris–Thorne, this is what we ship by default.**

**LUT does not work for:** rotating Teo (axisymmetric but not spherically symmetric, frame-dragging breaks the 1D parametrization → 4D LUT, 256MB+, not viable), dynamic throats (b₀ changing in time), MMP-stabilized scenes if we animate the Casimir source, scenes with two simultaneous wormholes. For those: live integration, accept the cost, use compute pass with persistent ray state if needed for temporal upsampling.

**Hybrid strategy:** ship LUT for the static demo scenes (1, 3 — Morris–Thorne, Ellis), live-integrate scenes 2 and 4. The user toggling "exotic matter density visualization" never invalidates the lensing LUT, only the overlay shader.

---

## 5. Beyond optics — physics that needs to run live

**5a. Massive-particle (test-body) trajectories.** Same RK4, same Christoffels, but `g_{μν} p^μ p^ν = -m²` instead of `0`. User flicks an object through the throat → spawn a particle with initial 4-momentum, integrate in compute shader at fixed Δτ (proper time), render as a sphere with motion-blur trail. Cost: trivial (one workgroup, ~10k FLOPs/particle/frame). Implementation: 1 day. Worth it for the "throw a wrench through" demo — that's the moment the simulator stops being a visualizer and becomes a sandbox.

**5b. Tidal force / Kretschmann scalar field.** `K = R_{μνρσ} R^{μνρσ}` measures real curvature. For Morris–Thorne with `b(r) = b₀²/r`, closed-form: `K = 12 b₀⁴ / (b₀² + r²)⁴` (verify this against Herman's notes before shipping — see §8). Compute on a 64³ voxel grid each frame (or precompute for static metrics), upload as 3D texture, render as volumetric overlay or contour shells. Cost: ~10 µs for static, ~0.5 ms/frame for dynamic. Implementation: 1–2 days. Lets the user *see* where the curvature is dangerous.

**5c. Time-dilation accumulator.** Per-camera-frame integrate `dτ/dt = sqrt(-g_{μν} u^μ u^ν)` where u is the camera 4-velocity, accumulate elapsed τ vs. lab time t, display as HUD. Free — single CPU multiply per frame. Implementation: 1 hour. Big psychological payoff.

**5d. Local energy-condition tensor evaluator.** Compute the stress-energy `T_{μν}` required to source the metric via `G_{μν} = 8π T_{μν}`. For Morris–Thorne, `T_{tt}, T_{rr}, T_{θθ}` are all closed-form in b and Φ. Then check NEC: `T_{μν} k^μ k^ν ≥ 0` for all null k. For Morris-Thorne the radial null `k = (1, 1, 0, 0)` gives `ρ + p_r = -b'/(8π r²)` which is negative at the throat — that's the famous exotic-matter requirement. Render voxels where it's violated in red. Cost: closed-form per voxel, basically free. Implementation: 1 day, dominated by getting the visualization right. **This is the killer feature for the theory ledger** — it makes "we need exotic matter" not a sentence in a paper but a glowing red shell in the user's view.

---

## 6. Verification recipes (commit to CI)

We need these green before any UI work merges. All run as Node + WASM tests, no GPU required (use the Rust integrator):

1. **Schwarzschild deflection angle.** Set b₀=0, switch to Schwarzschild metric (sanity baseline). Send rays at impact parameter `b = 5.2 r_s`, integrate. Expected α = 0.40 rad ± 1e-4 (analytic, weak-field corrected). Tolerance 1e-3 fractional. *Catches: wrong sign in Christoffels, wrong affine parameter step, conserved-quantity drift.*
2. **Morris–Thorne null geodesic energy conservation.** For any null geodesic, `E = -g_{tt} dt/dλ` is conserved. Run 1000 steps, assert |ΔE/E| < 1e-6. *Catches: integrator instability, wrong Christoffel.*
3. **Photon sphere radius (Schwarzschild check).** Inward-spiraling photon at impact parameter `b = 3√3 M / 2` should orbit. Assert radius stable to 1% over 5 orbits. *Catches: step-size adaptation breaking near unstable orbits.*
4. **Reproduce Müller (2008) Morris-Thorne lensing image.** Specific camera position, specific throat b₀, render a checker-pattern skybox, compare against published image with PSNR > 35 dB. *Catches: coordinate-chart bugs, wrong sign on far-side traversal.*
5. **Embedding-diagram check.** Numerical embedding of the t=const, θ=π/2 slice into 3D Euclidean should match `z(r) = b₀ · arcsinh(r/b₀)` to 1e-5. *Catches: metric typed wrong.*

(Optional 6th: Kerr ISCO at a=0.9M when we add the rotating scene — published value 2.32 M.)

These are cheap. Run them on every PR. If any goes red the integrator changed and we don't trust the visuals.

---

## 7. Three OSS projects to crib from (verified live as of 2026-05)

1. **oseiskar/black-hole** — https://github.com/oseiskar/black-hole. WebGL Schwarzschild raytracer in Three.js, GLSL fragment shader integrates geodesics on GPU. *Take:* `raytracer.glsl` integrator structure, the way it composes shader code with `glsl-bench`, the toggleable relativistic effects panel as a UI pattern. Closest spiritual ancestor of what we're building.
2. **rantonels/starless** — https://github.com/rantonels/starless. CPU numpy raytracer, Schwarzschild only. *Take:* the integrator math (clearer than the GLSL), the time-dependent worldtube intersection logic for animated objects, the redshift framework. Use as our offline verifier reference.
3. **bytebat/TraceIt** — https://github.com/bytebat/TraceIt. "GR Raytracing Sandbox," includes a *modified Ellis wormhole* renderer based on the DNEG/Interstellar approach. *Take:* the multi-metric architecture, how they parametrize the metric to swap between scenes. This is the closest existing project to our wormhole-specific use case. Verify license before pulling code.

Honorable mentions to read but not lift wholesale: peabrainiac/black-hole-renderer (clean WebGL Schwarzschild), gnikoloff/webgpu-raytracer (modern WebGPU compute patterns, not GR), s-macke/WebGPU-Lab (compute-shader patterns).

---

## 8. Citations

- **James, von Tunzelmann, Franklin, Thorne (2015).** "Gravitational Lensing by Spinning Black Holes in Astrophysics, and in the Movie Interstellar." arxiv:1502.03808. Class. Quantum Grav. 32, 065001. *DNGR architecture, ray-bundle propagation through Kerr.*
- **James, von Tunzelmann, Franklin, Thorne (2015).** "Visualizing Interstellar's Wormhole." arxiv:1502.03809. *Three-parameter wormhole family, embedding diagrams, the actual film wormhole spec.*
- **Morris, Thorne (1988).** "Wormholes in spacetime and their use for interstellar travel." Am. J. Phys. 56, 395. *Source of the metric we're using.*
- **Riazuelo (2008).** "Voyage au cœur d'un trou noir." Sciences et Avenir / IAP documentary. Approach paper not formally arxived; see https://luth.obspm.fr/~luthier/riazuelo/ [unverified link — confirm before citing].
- **Müller (2008).** "Visual appearance of a Morris–Thorne-wormhole." Am. J. Phys. 72, 1045. *Reference image for verification test #4. arxiv:gr-qc/0402071 [unverified — Müller has multiple wormhole-vis papers, double-check arxiv ID].*
- **Maldacena, Milekhin, Popov (2020).** "Traversable wormholes in four dimensions." arxiv:1807.04726. *For the MMP scene.*
- **Herman, R.** "Geodesic Equations for the Wormhole Metric." UNC Wilmington course notes — https://people.uncw.edu/hermanr/GRcosmo/GeodesicGR.pdf. *Cleanest derivation of the Morris–Thorne Christoffels we'll use.*

GitHub repos verified live 2026-05-01: oseiskar/black-hole, rantonels/starless, bytebat/TraceIt, peabrainiac/black-hole-renderer, gnikoloff/webgpu-raytracer.

---

## TL;DR for Anthony

Three.js + WebGPU, fragment-shader RK4 with closed-form Christoffels for Morris–Thorne, 1D LUT for the stationary scenes, compute pass for matter and tidal field, Rust+WASM verifier in CI running 5 numerical tests against published values. 60 fps on a 3060 is realistic. The Phase 0 script (`scripts/raytrace_throat.py`) becomes our test #4 — same integrator, same metric, scipy reference.

— Tomas
