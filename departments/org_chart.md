```
+============================================================================+
|  STARGATE RESEARCH COMPANY — ORGANIZATIONAL CHART                          |
|  Document ID:  SG3D-ORG-001                Revision: 0.1                   |
|  Classification: OPEN / PUBLIC RESEARCH    Date: 2026-05-01                |
|  Author: Eli Vargas (CoS) // Principal: Anthony Snider                     |
+============================================================================+
```

# Mission

Make a real, traversable Stargate. Test every credible path in a 3D
real-physics simulator. Push the cheapest viable analogue to a working
benchtop. Open-source the entire stack.

# Structure

We have one job. The org exists to surround that job from every angle that
could break the problem open. Three branches: Research, Engineering,
Operations. Each branch has departments. Each department is one or more
specialist agents producing concrete artifacts.

```
                    PRINCIPAL: Anthony Snider (drlor)
                                  |
                         CHIEF OF STAFF: Eli Vargas
                                  |
        +-------------------------+-------------------------+
        |                         |                         |
    [RESEARCH]              [ENGINEERING]              [OPERATIONS]
        |                         |                         |
        v                         v                         v
   R1-R11 below              E1-E4 below                O1-O5 below
```

---

## RESEARCH BRANCH

| ID  | Department                          | Lead (persona)        | Status |
|-----|-------------------------------------|-----------------------|--------|
| R1  | Theoretical GR / Wormhole Metrics   | Dr. Hana Reyes        | brief delivered |
| R2  | QFT / Exotic Matter / Casimir       | Dr. Marcus Chen       | brief delivered |
| R3  | Materials & Metamaterials           | Dr. Iris Vance        | brief delivered |
| R4  | Computational Physics / GPU         | Dr. Tomas Lindqvist   | brief delivered |
| R5  | Analogue Gravity                    | Dr. Yusra Okonkwo     | brief delivered |
| R6  | Plasma Physics & MHD                | Dr. Saavik Roy        | brief in progress |
| R7  | Quantum Information / ER=EPR        | Dr. Nadia Volkov      | brief in progress |
| R8  | Cryogenics & Vacuum Engineering     | Dr. Anders Holm       | brief in progress |
| R9  | Sensors & Instrumentation           | Dr. Priya Mehta       | brief in progress |
| R10 | Higher-Dimensional / Brane Physics  | Dr. Kenji Sato        | brief in progress |
| R11 | Lab Safety & Apartment Operations   | Capt. Linnea Torres   | brief in progress |

---

## ENGINEERING BRANCH

| ID  | Department                          | Charter |
|-----|-------------------------------------|---------|
| E1  | Simulator Engineering               | Three.js + WebGPU shell, scene graph, UI, GH Pages deploy |
| E2  | Physics Solver Core                 | Geodesic integrator (WASM/Rust), FE magnetostatics, BEC mode |
| E3  | Verification & Test                 | 5-test CI per Lindqvist §6, reproducibility harness |
| E4  | Bench Hardware                      | Magnetic-wormhole replica, instrumentation rig, lab notebook |

---

## OPERATIONS BRANCH

| ID  | Department                          | Charter |
|-----|-------------------------------------|---------|
| O1  | Funding & Grants                    | NSF, FQXi, Breakthrough, Astera, Emergent Ventures — only after working sim + replicated bench |
| O2  | Open-Source / Replication Network   | License (MIT/Apache-2), replication kits, citizen-science protocol |
| O3  | Literature Surveillance             | Daily arXiv watch on gr-qc, hep-th, cond-mat.quant-gas, physics.optics — feed new papers into ledger |
| O4  | IP & Patent Search                  | Existing patents in EM cloak / metamaterial / Casimir-related space; FTO check before any commercial step |
| O5  | Communication                       | Signal-only via @THRYXAGI per global rule. Tweet on milestones (sim launch, replication confirmed, theory killed) |

---

# Operating Rules

1. **Every department produces artifacts, not vibes.** Briefs cite real papers (arxiv ID / DOI). Code commits or it doesn't count. Lab notes use measured numbers.
2. **Validate before building.** Phase-0-style sanity tests precede every major construction. The 20-line raytracer comes before the WebGPU shader. The mu-metal hose comes before the YBCO cryostat.
3. **Kill criteria are stated in writing.** Each theory in the ledger has a "what evidence ends this line" field. We end lines on evidence, not feeling.
4. **Cross-department coordination is peer-to-peer.** R3 (materials) talks to E2 (FEM solver) directly. Don't route everything through Eli.
5. **No peopling.** No podcasts, no community management, no daily content. Signal-only public output.
6. **Apartment-renter constraint binds.** Anything that can't run safely with a six-year-old in the home gets deferred or moved to a partner lab.

# Cadence

- **Daily:** R3+E4 ledger update (parts ordered, lab notebook entries). E1+E2 commits.
- **Weekly:** O3 paper-watch digest, all-hands written sync (one markdown file in `departments/syncs/YYYY-MM-DD.md`).
- **Per milestone:** simulator scene shipped → CI green → public commit → @THRYXAGI signal tweet.

# Hand-off Doctrine

A department's work is "done" only when another department can pick it up cold.
- R1-R11 brief = ready when E2 can implement from it without re-deriving.
- E1-E4 deliverable = ready when an outside researcher can clone the repo and reproduce.
- E4 lab build = ready when a stranger with the BOM hits the same gauss-meter readings.

This doctrine is the only thing standing between us and the build → no-result → build loop.
