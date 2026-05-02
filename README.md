```
+==============================================================================+
|                                                                              |
|   S T A R G A T E   R E S E A R C H   P R O G R A M                          |
|                                                                              |
|   +--------------------+   +-------------------+   +-----------------------+ |
|   | CLASSIFICATION     |   | DOCUMENT ID       |   | REVISION              | |
|   | OPEN / PUBLIC      |   | SG3D-MAIN-001     |   | 0.2  (2026-05-01)     | |
|   +--------------------+   +-------------------+   +-----------------------+ |
|                                                                              |
|   ALL DATA, METHODS, AND CODE IN THIS REPOSITORY ARE RELEASED                |
|   FOR PUBLIC RESEARCH USE. NO COMPARTMENT. NO EMBARGO. NO PATENT WALL.       |
|                                                                              |
|   PROGRAM PRINCIPAL : SNIDER, A. (drlor)                                     |
|   CHIEF OF STAFF    : VARGAS, E.                                             |
|   ORIGIN            : VESTAL, NY · 2026-05-01                                |
|                                                                              |
+==============================================================================+
```

---

## §0  ABSTRACT

A 3D simulation world that obeys real physics, where every credible path to a
traversable wormhole is tested against numerical relativity, then ranked by
buildability so the cheapest viable analogue can be moved to a benchtop. Not a
movie prop. Not a science-fiction tribute. An open-source research program
whose output is either a working portal or the most accurate public record of
exactly which wall stopped us and why.

This repository is the workshop.

---

## §1  MISSION

> Make a real, traversable Stargate. Or kill every plausible attempt and
> publish the autopsy.

If our current theories say it's impossible, those theories are incomplete and
we treat that as a hypothesis to break, not a verdict to accept. We will run
out of paths long before we run out of patience.

---

## §2  BASIS IN PRIOR ART

The pieces already exist in real laboratories. Nobody has assembled them.

| #   | Result                                            | Year | Citation                                            |
|-----|---------------------------------------------------|------|-----------------------------------------------------|
| 2.1 | Morris–Thorne traversable wormhole geometry       | 1988 | Am. J. Phys. **56**, 395                            |
| 2.2 | Casimir effect, measured negative energy density  | 1958/1997 | Sparnaay; Lamoreaux PRL **78**, 5             |
| 2.3 | Dynamical Casimir radiation, superconducting cct  | 2011 | Wilson et al., arXiv:1105.4714                      |
| 2.4 | Magnetic-field "wormhole" via metamaterials       | 2015 | Prat-Camps et al., Sci. Rep. **5**, 12488           |
| 2.5 | Stabilized 4D traversable wormhole construction   | 2018/2020 | Maldacena, Milekhin, Popov, arXiv:1807.04726 / 2008.06618 |
| 2.6 | Quantum-circuit "wormhole" protocol on Sycamore   | 2022 | Jafferis et al., Nature **612**, 51                 |
| 2.7 | Status of #2.6 contested                          | 2023/25 | Kobrin–Schuster–Yao, arXiv:2302.07897              |
| 2.8 | BEC analogue Hawking radiation                    | 2014/16/19 | Steinhauer et al., Nature Phys. **10**, 864 et seq. |

The gap between these and a person-sized portal is enormous. It is not,
however, a gap of physics-not-existing. It is a gap of engineering on top of
physics that has already cleared.

---

## §3  PROGRAM STRUCTURE

Three branches, twenty departments. Full org chart at
`departments/org_chart.md`.

```
                         PRINCIPAL  ⟶  CHIEF OF STAFF
                                 |
        +------------------------+------------------------+
        |                        |                        |
   [RESEARCH]               [ENGINEERING]            [OPERATIONS]
   R1  Theoretical GR       E1  Simulator           O1  Funding & Grants
   R2  QFT / Exotic Matter  E2  Physics Solver      O2  Open-Source Release
   R3  Materials            E3  Verification & CI   O3  Literature Surveillance
   R4  Computational / GPU  E4  Bench Hardware      O4  IP / Patent Search
   R5  Analogue Gravity                              O5  Communication
   R6  Plasma / MHD
   R7  Quantum Information
   R8  Cryogenics & Vacuum
   R9  Sensors / Instr.
   R10 Higher-Dim / Brane
   R11 Lab Safety / Apt Ops
```

Eleven specialist research briefs (one per R-department) are committed to
`docs/team_briefs/`. Each brief cites real papers (arXiv ID / DOI) and
identifies items it cannot verify, marked `[unverified]` rather than
laundered. **Rolled-up specs:** `docs/physics_spec.md` (what the simulator
must compute) and `docs/materials_ledger.md` (what we buy and don't).

---

## §4  STATUS

| Ref      | Item                                              | State        | Date       |
|----------|---------------------------------------------------|--------------|------------|
| §4.1     | Repo initialized, public, MIT-implicit            | DONE         | 2026-05-01 |
| §4.2     | Org chart + 11 specialist briefs                  | DONE         | 2026-05-01 |
| §4.3     | Synthesis: physics_spec.md + materials_ledger.md  | DONE         | 2026-05-01 |
| §4.4     | Phase 0 — Morris–Thorne geodesic integrator       | **PASS**     | 2026-05-01 |
| §4.5     | Phase 1 — WebGPU simulator scaffold               | NOT STARTED  |    —       |
| §4.6     | Phase 1 — Morris–Thorne lensing scene             | NOT STARTED  |    —       |
| §4.7     | Phase 3 — Prat-Camps replica BOM finalized        | IN PROGRESS  |    —       |
| §4.8     | Phase 3 — Bench replica fabricated                | NOT STARTED  |    —       |

**Phase 0 result.** `scripts/raytrace_throat.py` integrates null geodesics
through a Morris–Thorne metric (b₀ = 1) using the Hamiltonian formulation in
the Reyes (R1) brief §3. Validation gates:

```
[1] max |H| residual across all rays    : 3.77e-15  (gate < 1e-8)   PASS
[2] photon b=0.5  traverses the throat  : True                      PASS
[3] photon b=1.5  reflects (p_l flip)   : True                      PASS
[4] photon-sphere log-divergence Δφ→ln10 : 2.2982 vs 2.3026         PASS
```

The integrator is cleared for the Phase 1 WebGPU port and is committed as
verification fixture #4 in the Lindqvist (R4) test plan. Plot saved at
`out/phase0_raytrace.png`.

---

## §5  KILL CRITERIA

A theory leaves the program when evidence ends it, not when fashion does. Each
entry in `theories/` (forthcoming) carries an explicit kill criterion.

| Class           | Kill condition                                                    |
|-----------------|-------------------------------------------------------------------|
| 4D classical    | Ford–Roman QI bound forces throat ≪ 10⁻¹⁷ m at our scales         |
| MMP higher-dim  | LHC monopole search closes window on required magnetic monopoles  |
| ER=EPR / GJW    | Independent replication of Sycamore-class result fails on N>50    |
| Magnetic analogue| Phase-1 replica produces no measurable topology change at FE-predicted strength |
| Plasma / Heim   | Already killed (Tajmar EmDrive falsification, Landis Heim catalog)|

Many of these will fire. That's fine. Negative results published with
measurement are worth more than a hundred unmeasured affirmatives.

---

## §6  HARD CONSTRAINTS

The program runs from a rented apartment in Vestal NY with a six-year-old in
the home. Budget: zero free cash. Distribution: signal-only via @THRYXAGI.
Lab safety: Capt. Torres's brief (`docs/team_briefs/11_lab_safety_apartment_ops.md`)
is binding — see her hard NO list.

Anything that cannot run safely with Lucia in the home is deferred or moved to
a partner laboratory. Anything that needs paid floors before profit is killed.
Anything that requires "build an audience" or peopling does not exist in this
program.

---

## §7  HOW TO READ THIS REPOSITORY

Full layout and "where things go" guide: `STRUCTURE.md`. Quick map:

```
StarGate3d/
├── README.md  PLAN.md  STRUCTURE.md      <- start here
├── pyproject.toml                         pip install -e .
├── departments/                           org chart
├── docs/                                  specs + 11 team briefs
├── theories/                              theory ledger (1 filled, 12 TBD)
├── py/stargate/                           Python ground-truth core
│   ├── metrics/        integrators/       validation/   viz/
│   └── geodesics.py
├── tests/                                 pytest, 7/7 green
├── scripts/                               thin entry points
├── lab/                                   bench notebook + BOMs
└── out/                                   generated artifacts (plots, data)
```

Outside readers, start at `README.md → PLAN.md → docs/physics_spec.md`. To
verify Phase 0:

```
pip install -e .[dev]
pytest          # 7 passed
py scripts/raytrace_throat.py   # all 4 gates PASS, plot at out/phase0_raytrace.png
```

If your interest is the lab side, jump to `docs/materials_ledger.md` and
brief 03.

---

## §8  HUMANITY CLAUSE

If a real gate is possible, it belongs to everyone. All theory, simulator
code, materials lists, and lab notes here are open source from the first
commit. There will be no proprietary fork. The protocol for whatever works,
when it works, will be a single PDF with a parts list, a wiring diagram, a
calibration script, and the expected reading at every step — small enough that
a stranger with the same parts hits the same numbers.

That is the deliverable.

---

```
+==============================================================================+
| END OF DOCUMENT                                                              |
| FILE   : README.md                                                           |
| SHA    : (computed at commit)                                                |
| STATUS : RELEASED — PUBLIC RESEARCH                                          |
+==============================================================================+
```

— Anthony Snider (`lordbasilaiassistant-sudo`)
