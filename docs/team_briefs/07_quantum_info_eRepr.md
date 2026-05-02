# Brief 07 — ER=EPR, Traversable Wormhole Protocols, and the Sycamore Question

**Author:** Dr. Nadia Volkov (R7, quantum information / holography)
**Audience:** Engineering team + theory peers (builds on Brief 01 — GR metrics, and
Brief 02 — QFT exotic matter; does not duplicate either)
**Goal:** Decide what holographic / quantum-circuit content honestly belongs in
the Stargate simulator, what we can run on hardware we already have, and where
the math-vs-physics line lives.

---

## 1. ER=EPR primer (Maldacena–Susskind 2013, arXiv:1306.0533)

The conjecture states: **every Bell pair is dual to a (non-traversable)
Einstein–Rosen bridge connecting the two systems.** Maximally entangled =
classical-geometry ER bridge; partially entangled = bridge dressed with
quantum/stringy fluctuations; product state = no bridge.

The motivating example is rigorous and is *not* a conjecture: the **eternal
two-sided AdS–Schwarzschild black hole** (Maldacena 2001, hep-th/0106112) is
holographically dual to the **thermofield double (TFD) state** of two
non-interacting CFTs,

```
|TFD⟩ = Z(β)^{-1/2} Σ_n e^{-β E_n / 2} |n⟩_L ⊗ |n⟩_R
```

Trace out one side → thermal density matrix at temperature `1/β` on the other.
The two CFTs share no Hamiltonian coupling but are entangled, and the bulk dual
contains an Einstein–Rosen bridge linking the two exterior regions. That much is
standard AdS/CFT; the Einstein–Rosen bridge is real geometry in the bulk.

What ER=EPR adds is the leap from this special two-sided black hole to a
**universal** statement: any entangled pair, even two electrons in a Bell state,
is connected by some Planckian, highly fluctuating analogue. Honest distinction:

- **Formal duality (uncontroversial):** TFD ↔ eternal AdS–Schwarzschild.
- **Conjecture (still open):** the entanglement-→-bridge correspondence
  generalizes to arbitrary entangled systems.
- **Not claimed by ER=EPR:** that you can send a signal through the bridge.
  Eternal AdS–Schwarzschild is famously **non-traversable** — the two sides
  cannot communicate; the wormhole pinches off faster than light can cross.
  ER=EPR is consistent with no-signalling because EPR pairs cannot signal either.

For the simulator, treat ER=EPR as a *visualization principle*, not a transport
mechanism: every entangled qubit pair can be drawn as a thread in an
auxiliary "bulk." That's interpretation, not a new channel.

---

## 2. Gao–Jafferis–Wall (GJW) traversable-wormhole protocol (arXiv:1608.05687)

GJW (2016, JHEP 12 (2017) 151) showed the eternal BTZ black hole becomes
**transiently traversable** when you turn on a direct **double-trace
deformation** coupling the two boundary CFTs:

```
δH = g ∫ dt dx O_L(t,x) O_R(t,x)
```

`O_L`, `O_R` are local single-trace primaries on the two boundaries; `g` is a
real coupling switched on for a finite time window.

What this does, mechanically:

1. The coupling correlates the two sides — analogous to opening a classical
   communication channel between Alice and Bob.
2. In the bulk, the deformation injects a **stress tensor with negative
   averaged null energy** (ANEC violation) along a null geodesic threading
   the bridge. This is a 1-loop quantum effect — the bulk fields' two-point
   function is modified by the boundary coupling.
3. The negative-ANEC pulse **back-reacts** on the metric and lifts the horizon
   off the geodesic for a brief window. A signal sent in from the left
   exterior can now exit on the right.

Crucial caveats:

- **Both sides under control.** The protocol requires simultaneous, coordinated
  operations on both CFTs. You can't do this with a black hole pair you don't
  own — the coupling is non-local and must be applied to both Hamiltonians.
- **Causal censorship preserved.** The signal arrives later through the wormhole
  than it would through the boundary coupling itself. No FTL — the wormhole
  is a redundant channel, not a shortcut. (Maldacena–Qi 2018 "Eternal
  traversable wormhole," arXiv:1804.00491, made this sharp.)
- **Small bandwidth.** Information capacity is bounded by `~log(g·N)` qubits
  per traversal in the BTZ setup.

GJW is the cleanest theoretical bridge between "ER=EPR philosophy" and "you can
push a qubit through the bridge" — and it's the protocol everyone since 2017
has tried to instantiate.

---

## 3. The Sycamore experiment and the controversy (arXiv:2203.13193)

**Setup.** Jafferis et al., *Nature* 612, 51 (2022). 9 qubits on Google
Sycamore. They prepared a TFD-like state of two N=7 Majorana SYK systems,
applied a learned (machine-trained) Hamiltonian intended to mimic SYK_q=4
dynamics, then turned on a coupling between the two sides analogous to GJW's
double-trace deformation. They measured **operator size winding** on the right
side after injecting an operator on the left, and reported that
- the size distribution wound around the origin in the complex plane the way
  it does in semiclassical SYK with a traversable-wormhole dual, and
- the teleportation fidelity peaked at the predicted "wormhole-opens" coupling
  sign and time.

**Controversy (Kobrin, Schuster, Yao — arXiv:2302.07897, *Nature* 638, 2025
"Experiments implementing small commuting models lack gravitational features").**
Three substantive objections:

1. **Hamiltonian doesn't thermalize.** A real holographic system at this
   temperature should scramble; the learned Hamiltonian that Jafferis et al.
   used is closer to a *commuting* (free-fermion-like) model. Commuting models
   don't have black-hole duals.
2. **Size winding is generic for tiny commuting models.** Perfect size winding
   appears in N=7 commuting Hamiltonians by accident of small-N structure; it
   is not a witness of bulk gravity. Kobrin et al. show it disappears in
   larger commuting models and never appears in non-commuting non-SYK models.
3. **The signal generalizes only to trained operators.** ψ_4 and ψ_7 (operators
   not in the training set) showed poor size winding at the protocol's
   working time `t₀ ≈ 2.8`.

**Jafferis reply (*Nature* 638, 2025; also arXiv:2308.00697 community
discussion).** Argues the slower-thermalizing fermions are the lighter ones —
late-time size winding is a feature, not a bug — and that the experiment
demonstrates a **pseudo-holographic** regime worth studying even if the
learned Hamiltonian isn't exactly SYK. Gao (2024) showed a large-N commuting
SYK at q=4 reproduces several semiclassical-wormhole signatures in distinct
parameter regimes, partly vindicating the "pseudo-holographic" framing.

**Honest current status:** The Sycamore experiment demonstrated **operator
teleportation in a small spin chain**. Whether what was teleported "passed
through a wormhole" depends on whether the learned Hamiltonian is
holographic. Kobrin/Schuster/Yao have largely won the technical argument
that the specific N=7 instance is not. The protocol *would* show wormhole
physics if run on a system that genuinely thermalizes like SYK at large N —
that system has not yet been built.

---

## 4. What it would take to scale past "SYK simulation"

To produce a holographic-wormhole signature that can't be reproduced by a
small commuting model, you need:

- **N ≳ 50–100 Majorana fermions per side**, i.e. ≥100 qubits per boundary
  (≥200 total) for SYK_q=4 to enter the large-N semiclassical regime where
  the bulk geometry is even approximately defined.
- **Two-qubit gate fidelity ≥ 99.9%** sustained over ~10⁴–10⁵ gates per shot.
  Sycamore 2022 ran at ~99.4% — fine for 9 qubits, fatal at 100.
- **All-to-all (or efficiently-routed) connectivity.** SYK has random
  all-to-all four-fermion couplings; native all-to-all (Quantinuum trapped
  ion) saves an order of magnitude in depth vs. nearest-neighbor lattices
  (Google/IBM superconducting).
- **Mid-circuit measurement + feed-forward** for the protocol's coupling
  step, ideally at sub-µs latency.

State of the art (mid-2026):

- IBM Heron r2 (`ibm_kingston`, on free Open Plan): 156 qubits, median 2Q
  error ~2×10⁻³ (i.e. 99.8% fidelity), heavy-hex connectivity. This is
  enough qubits but the connectivity tax pushes effective SYK depth past
  what fidelity supports.
- Quantinuum H2: 56 trapped-ion qubits, all-to-all, 99.8% 2Q, recent runs at
  99.914%. Fewer qubits, much better depth budget.
- Google Willow (2024 generation): 105 qubits, ~99.7% 2Q.

Roadmaps converge on **≥1000-qubit logical-qubit-encoded systems by ~2029
(IBM Starling target, Quantinuum 2030 fault-tolerance roadmap)**. Until
then, every "wormhole" experiment will be a small-N SYK or commuting analog,
and the Kobrin–Schuster–Yao critique will keep applying.

---

## 5. What this means for the Stargate simulator

**Brutal answer:** A quantum-circuit "Stargate" is **a holographic dual that
lives in the math, not a physical spacetime channel.** The boundary qubits
are real; the bulk wormhole through which information appears to pass is an
emergent description of the boundary correlations. There is no extra
spacetime channel — the qubit reaches the right side because of the boundary
coupling, full stop. The wormhole language is a faithful but not unique
re-description.

**What would convert the dual into a real channel?** Three things would have
to hold simultaneously, and we have no evidence any does:

1. **The bulk is independently real**, not just a useful dual. (No known
   experimental discriminator; this is a metaphysical preference until
   somebody designs one.)
2. **The boundary system is itself embedded in our 4D spacetime in a way
   that makes its bulk physical.** AdS/CFT requires asymptotically AdS
   boundary conditions; our universe is asymptotically de Sitter. dS/CFT
   is much less under control.
3. **The protocol can deliver ANEC violation in 4D Minkowski**, not just on
   the AdS₂ throat of an SYK dual. This crosses back into Brief 02
   territory (Maldacena–Milekhin–Popov is the only credible 4D route, and
   it needs magnetic monopoles + BSM fermion content).

We should label the simulator's "ER=EPR / GJW" mode honestly: **holographic
visualization of quantum-circuit correlations**. Not "we simulated a
spacetime wormhole."

---

## 6. Three simulator features

### 6a. Two-mouth wormhole with simulated entanglement on each side
Two BTZ-like mouths rendered side-by-side. Each mouth is "decorated" with N
qubits whose pairwise entanglement (computed from a stored density matrix or
TFD-like state) is drawn as a thread bundle through the throat. Thread
density at radius r in the throat ∝ mutual information `I(A_L : A_R)`
between corresponding boundary regions. Math: 2D BTZ embedded as in Brief
01; entanglement is a 2D scalar field over the boundary parameterization,
mapped to thread color/density via `1 - exp(-I)`. **GPU cost:** O(N²) for
the mutual-information matrix per frame; for N≤64 this is ~4k cells, ~30 µs
on any modern GPU. Free.

### 6b. GJW-protocol slider that opens the throat
A UI slider corresponds to the double-trace coupling `g`. As `g` crosses
zero, the simulator integrates the perturbed null geodesic and shows the
horizon retreating off the geodesic for a finite window. Math: closed-form
for BTZ from arXiv:1608.05687 §3 — back-reacted metric is a known function
of `g`, conformal weight ∆, and time. Render the **traversal window** as a
shaded region on a Penrose diagram inset. Tie the slider to a **bandwidth
counter** displaying `log₂(traversed qubits)` and grey it out when the
quantum-inequality or causal-shortcut bounds are saturated. **GPU cost:**
trivial; this is a 1D ODE in conformal time. Free.

### 6c. Holographic-dual visualizer (AdS bulk + boundary CFT side-by-side)
Split-view: left pane shows the AdS₂×S² (or AdS₃) bulk with the wormhole
embedded; right pane shows the boundary as a 1D circle of qubits with a
per-pair entanglement chord diagram (Ryu–Takayanagi-style). Drag a chord
on the boundary → see the corresponding RT minimal surface light up in
the bulk. Math: minimal-surface computation in pure AdS₃ has closed-form
geodesics; for back-reacted geometry use Brief 01's symplectic integrator
restricted to the (t=const) slice. **GPU cost:** RT surfaces are 1D curves,
~N² of them, N ≤ 64 → ~4k curves, fragment-shader-friendly. Free.

---

## 7. Three concrete experiments

### 7a. GJW-style protocol on IBM Quantum free tier (Heron r2 / Eagle r3)
**What:** Replicate the Jafferis-style 9-qubit SYK-teleportation on
`ibm_kingston` (Heron r2, free Open Plan, 156 qubits, 99.8% 2Q). Same
N=7 Majorana → 7 qubits per side + 2 bell-pair qubits = 9 active qubits.
**Gates:** ~120 two-qubit gates (CZ/ECR), ~250 single-qubit, depth ~30
after transpilation onto heavy-hex.
**Runtime:** ~10⁴ shots × ~50 µs/shot ≈ 0.5 s of QPU time, well under the
10 min/month free quota (the 2026 promo bumps to 180 min over 12 months
for active users).
**What it proves:** That we can reproduce the published teleportation
signature on a different platform — useful to confirm it's protocol-level,
not Sycamore-specific. **What it doesn't prove:** that the bulk is real
(see §3). Cost: $0 (free tier).

### 7b. Larger SYK-teleportation on Quantinuum H2 (paid; price-check only)
**What:** N=20 Majorana → 20 qubits per side, all-to-all SYK_q=4 with
random Gaussian couplings, GJW double-trace deformation. The all-to-all
trapped-ion architecture is the only commercial platform where SYK depth
fits in fidelity budget at N≥20.
**Gates:** ~6000 two-qubit gates at 99.9% → expected output fidelity
~0.997^6000 ≈ 0.002 — borderline. Need richer error mitigation.
**Cost:** Quantinuum H2 is paid-only via Azure Quantum. *Per global rule
#1, we don't run this — it's listed for the roadmap.*
**What it would prove:** Whether size winding survives at N=20 without
Hamiltonian learning (the criticism in §3 hinges on N=7 small-model
artifacts). **What it wouldn't prove:** still no real bulk.

### 7c. Simulated SYK + GJW on a CPU (pure software)
**What:** Direct numerical simulation of two coupled SYK_q=4 Hamiltonians
with N up to ~24 Majoranas (Hilbert dim ~4096 per side, 16M total). Run
the GJW protocol classically, plot the size-winding observable and the
teleportation fidelity vs. coupling. Use the Python `dynamite` or
`qutip-jax` packages on a single GPU (free tier on Colab works for N≤22).
**Cost:** $0 — runs locally or on free Colab.
**What it proves:** Establishes the **classical-simulable baseline**
against which any quantum-hardware result must be compared. The
Kobrin–Schuster–Yao critique is fundamentally that the Sycamore result
was at this level of difficulty — so we *must* run this baseline if we
ever quote a hardware run.

**Recommendation:** Do 7c first (this week, costs nothing). Do 7a after
the simulator's GJW-slider feature is built, so we can overlay
hardware-measured size winding on the simulator's predicted curve. Skip
7b until we have revenue.

---

## 8. Citations

- Maldacena, Susskind, "Cool horizons for entangled black holes," *Fortsch.
  Phys.* 61, 781 (2013). arXiv:1306.0533.
- Maldacena, "Eternal black holes in anti-de Sitter," *JHEP* 04 (2003) 021.
  arXiv:hep-th/0106112.
- Gao, Jafferis, Wall, "Traversable Wormholes via a Double Trace
  Deformation," *JHEP* 12 (2017) 151. arXiv:1608.05687.
- Maldacena, Qi, "Eternal traversable wormhole," arXiv:1804.00491.
- Jafferis, Zlokapa, Lykken, Kolchmeyer, Davis, Lauk, Neven, Spiropulu,
  "Traversable wormhole dynamics on a quantum processor," *Nature* 612, 51
  (2022). arXiv:2203.13193. DOI:10.1038/s41586-022-05424-3.
- Kobrin, Schuster, Yao, "Comment on 'Traversable wormhole dynamics on a
  quantum processor,'" arXiv:2302.07897. Published as "Experiments
  implementing small commuting models lack gravitational features,"
  *Nature* 638 (2025). DOI:10.1038/s41586-025-08939-7.
- Jafferis et al. reply, *Nature* 638 (2025).
  DOI:10.1038/s41586-025-08995-z.
- Wittek/community discussion, "Debating the Reliability and Robustness of
  the Learned Hamiltonian in the Traversable Wormhole Experiment,"
  arXiv:2308.00697.
- Brustein, Sherf, "The Neverending Story of the Eternal Wormhole and the
  Noisy Sycamore," arXiv:2301.03522.
- Schuster, Kobrin, Gao, Cong, Khabiboulline, Linke, Lukin, Monroe, Yao,
  Zhuang, "Many-body quantum teleportation via operator spreading in the
  traversable wormhole protocol," *Phys. Rev. X* 12, 031013 (2022).
  arXiv:2102.00010.
- Maldacena, Stanford, "Remarks on the Sachdev–Ye–Kitaev model,"
  *Phys. Rev. D* 94, 106002 (2016). arXiv:1604.07818. [unverified — cite
  for SYK background, not specifically used above.]
- Gao, "Commuting SYK and pseudo-holography," 2024. [unverified arXiv ID;
  flagged in §3 from secondary report — confirm before quoting publicly.]
- IBM Quantum hardware page, accessed May 2026:
  https://www.ibm.com/quantum/hardware (Heron r2 specs, Open Plan limits).
- Quantinuum H2 product data sheet, https://www.quantinuum.com/products-solutions/quantinuum-systems/system-model-h2
  (56 qubits, 99.8% 2Q, all-to-all).

— Nadia
