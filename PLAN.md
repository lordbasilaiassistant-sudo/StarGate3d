```
+==============================================================================+
|  PROGRAM PLAN                                                                |
|  DOC ID: SG3D-PLAN-001     REV: 0.2     DATE: 2026-05-01                     |
|  CLASSIFICATION: OPEN / PUBLIC RESEARCH                                      |
+==============================================================================+
```

Phased build order. Validate before scaling. No teams for unvalidated ideas.
Kill on evidence. Same loop applied to physics that we'd apply to anything
else.

---

## §1  PHASE 0 — SANITY CHECK   ◆ COMPLETE 2026-05-01

`scripts/raytrace_throat.py` integrates null geodesics through Morris–Thorne
in the Hamiltonian formulation (Reyes brief §3). All four validation gates
pass:

```
[1] |H| residual          3.77e-15  (gate < 1e-8)
[2] b<b0 traverses        True
[3] b>b0 reflects         True
[4] photon-sphere log-div 2.298 → 2.303 (ln 10)
```

Result: integrator quality is sufficient for Phase 1 GPU port. The script is
committed as verification fixture #4 (Lindqvist R4 §6) and will run in CI.

> **Doctrine.** A 20-line test that proves the math handle is worth more than
> a 20-thousand-line engine that doesn't.

---

## §2  PHASE 1 — SIMULATOR  (target weeks 2–6)

Browser scene where the user walks up to a wormhole mouth and looks through
it. Light is integrated through the real metric per pixel, not faked with a
shader trick.

| §    | Deliverable                                                  | Owner | Source brief |
|------|--------------------------------------------------------------|-------|--------------|
| 2.1  | Three.js + WebGPU scaffold, GH Pages CI                       | E1    | R4 §1        |
| 2.2  | RK4 geodesic integrator on fragment shader (8D phase space)   | E2    | R4 §2        |
| 2.3  | Christoffel closed-forms for Morris–Thorne / Ellis            | E2    | R1 §3        |
| 2.4  | 1D LUT optimizer for axisymmetric metrics (~30–50× speedup)   | E2    | R4 §4        |
| 2.5  | Scene S1 — Morris–Thorne                                      | E1    | R1 §1        |
| 2.6  | Scene S2 — Ellis drainhole                                    | E1    | R1 §1        |
| 2.7  | Scene S3 — Teo rotating (live integrate)                      | E1    | R1 §1        |
| 2.8  | Scene S4 — MMP stabilized (with N_f, monopole HUD)            | E1    | R2 §2, R10 §1|
| 2.9  | Scene S6 — Casimir cell, T_μν per-voxel field viz             | E1    | R2 §1        |
| 2.10 | Energy-condition HUD on user worldline (NEC violation flag)   | E1    | R2 §5        |
| 2.11 | Embedding diagram side-panel                                  | E1    | R1 §4        |

**Verification fixtures** (CI gates, all from R4 §6 + R1 §3):

```
T1  Schwarzschild deflection vs analytic           tol < 1e-3
T2  Energy/H conservation along trajectory         drift < 1e-8
T3  Photon-sphere radius (Morris–Thorne, l=0)      match
T4  Müller image PSNR vs published reference       > 30 dB
T5  Embedding-diagram visual                       reproduces Flamm horn
```

Anti-features (R1 §5 + R6 §4 — explicitly NOT shipping):

- No FTL travel UI gimmickry — wormhole mouth-to-mouth is not faster than
  light from the boundary observer's frame except via the throat shortcut,
  and we will display that honestly.
- No "Heim drive" toggle. Falsified.
- No entrance-shimmer particle effect. The metric does the visual; we do not
  decorate it.
- No fake confidence bars on theory cards.

---

## §3  PHASE 2 — THEORY LEDGER  (parallel, weeks 2–8)

`theories/` directory, one markdown file per portal mechanism, each with
required ingredients, sim scene, lab analogue, materials cost, experimental
status (with arXiv IDs), kill criterion, open questions.

10 entries, sourced from the team briefs:

```
theories/
├── morris-thorne.md                ← R1
├── casimir-stabilized-mmp.md       ← R2 + R10
├── er-epr-gjw.md                   ← R7
├── magnetic-metamaterial.md        ← R3 (cheapest buildable)
├── acoustic-analogue.md            ← R5
├── bec-analogue.md                 ← R5
├── optical-metamaterial.md         ← R3
├── plasma-toroid.md                ← R6 (visual, not portal)
├── alcubierre-warp.md              ← R1 (completeness)
└── vacuum-engineering.md           ← R2 (DCE, squeezed states)
```

Ranking after the 10 are filled: `(P_traversable × ln(1 / dollar_cost))`.

---

## §4  PHASE 3 — BUILDABLE ANALOGUE  (after ranking)

Almost certainly the magnetic-metamaterial path first. R3 brief identifies a
**Phase-1 mu-metal-only replica at $300–500** that gives a measurable B-field
guiding effect — the right validation target for the FE solver before any
$1k+ YBCO step.

Capt. Torres's safety brief (R11) is binding. GO/NO-GO gating per R11 §7:

```
   ┌────────────────────────────────────────┐
   │  Hazard within tolerance?       (a)    │
   │  Child safe?                    (b)    │
   │  Reversible setup?              (c)    │
   │  Measurable outcome?            (d)    │
   └────────────────────────────────────────┘
        all four → GO   any one → NO-GO
```

**Build path:**

1. **Phase-1.** Mu-metal hose + NdFeB source + Hall probe ($300–500).
   Validate FE solver against measured field map. Kill criterion: no
   detectable field-line guiding effect at predicted strength.
2. **Phase-2.** Add YBCO + LN₂ outer shell ($3–5k all-in). Reproduce
   Prat-Camps 2015 within 5%. Kill: cannot.
3. **Phase-3.** Push beyond replication — bigger device, multi-field
   coupling, time-varying drive. Document where the math actually breaks.

Hand-off doctrine (org_chart.md §"Hand-off Doctrine"): each build is "done"
only when an outside reader with the same parts hits the same numbers.

---

## §5  PHASE 4 — DISTRIBUTION

- Repo public from day 0. MIT-implicit license; explicit license file when an
  external contributor lands.
- Simulator hosted free on GitHub Pages.
- Lab notes committed alongside code, raw measurements included.
- @THRYXAGI signal posts only on real milestones: Phase 1 sim live, Phase-1
  bench replica reading verified, theory entry killed by evidence.
- No socials beyond signal. No podcasts. No content treadmill.

After Phase 1 is live and Phase-1 bench is repeatable, **then** the funding
queue opens: NSF unsolicited, FQXi, Breakthrough, Astera, Emergent Ventures.
Not before.

---

## §6  WHAT THIS PLAN REFUSES TO DO

| Anti-pattern                                            | Why it stays out |
|---------------------------------------------------------|------------------|
| Build before validating                                 | Loses months — Phase 0 first, every time |
| Promise a working gate                                  | Honest answer is "we don't know yet" |
| Hand-wave around ANEC / Ford–Roman QIs                  | Those are real walls; we engage them |
| Spend money before something works                      | Renter, no payroll, $200/mo Claude floor |
| Theatrical redactions over honest uncertainty           | We mark `[unverified]`, not `[REDACTED]` |
| Spawn agent teams for unvalidated ideas                 | One agent + one script + one test first |

---

## §7  IMMEDIATE NEXT ACTIONS  (post-Phase 0)

1. E1 / E2: scaffold the Three.js + WebGPU app and wire CI on GH Pages.
2. E2: port `raytrace_throat.py` logic to a WGSL fragment shader, validate
   against the same numerical fixtures.
3. E3: add T1–T5 verification fixtures to CI; gate all merges on green.
4. R3 + E4: finalize the Phase-1 magnetic-wormhole BOM and place orders for
   the parts under $50/each that arrive within a week (mu-metal sheet, NdFeB
   block, Hall sensor IC).
5. O3: subscribe arxiv watch on `gr-qc`, `hep-th`, `cond-mat.quant-gas`,
   `physics.optics` and feed deltas into the theory ledger weekly.

```
+==============================================================================+
| END OF PLAN                                                                  |
+==============================================================================+
```
