```
+==============================================================================+
|  REPOSITORY STRUCTURE                                                        |
|  DOC ID: SG3D-STRUCT-001     REV: 0.1     DATE: 2026-05-01                   |
+==============================================================================+
```

Where to put things. Where to find things. Read this once before contributing.

## Top-level layout

```
StarGate3d/
├── README.md                  Mission, status, basis in prior art
├── PLAN.md                    Phased roadmap, kill criteria, hard constraints
├── STRUCTURE.md               <-- this file
├── pyproject.toml             Python package + pytest config
├── .gitignore
│
├── departments/               Company structure
│   └── org_chart.md           Three branches × 20 departments
│
├── docs/                      Specs and briefs
│   ├── physics_spec.md        What the simulator must compute (9 modules / 13 scenes)
│   ├── materials_ledger.md    BOMs, vendors, hard NO list
│   └── team_briefs/           Specialist research briefs (R1–R11)
│       ├── 01_theoretical_gr.md
│       ├── 02_qft_exotic_matter.md
│       ├── 03_materials_metamaterials.md
│       ├── 04_computational_gpu.md
│       ├── 05_analogue_gravity.md
│       ├── 06_plasma_mhd.md
│       ├── 07_quantum_info_eRepr.md
│       ├── 08_cryo_vacuum.md
│       ├── 09_sensors_instrumentation.md
│       ├── 10_higher_dim_brane.md
│       └── 11_lab_safety_apartment_ops.md
│
├── theories/                  Theory ledger — one entry per portal mechanism
│   ├── README.md              Format, ranking criteria, index
│   └── morris-thorne.md       Filled template; others TBD per index
│
├── py/                        Python ground-truth and verification core
│   └── stargate/
│       ├── __init__.py
│       ├── geodesics.py       Hamilton's equations, conserved quantities
│       ├── metrics/           Pluggable spacetime metrics
│       │   ├── __init__.py
│       │   └── morris_thorne.py
│       ├── integrators/       Pluggable ODE integrators
│       │   ├── __init__.py
│       │   └── scipy_dop853.py
│       ├── validation/        Numerical fixture gates (tested in CI)
│       │   ├── __init__.py
│       │   └── morris_thorne_gates.py
│       └── viz/               Offline matplotlib plots
│           ├── __init__.py
│           └── topdown.py
│
├── tests/                     pytest fixtures, run on every push
│   ├── conftest.py
│   └── test_morris_thorne.py  4 validation gates + sanity tests
│
├── scripts/                   Thin entry points; no logic of their own
│   └── raytrace_throat.py     Phase-0 orchestrator (calls stargate.*)
│
├── lab/                       Lab notebook, build instructions, BOMs in flight
│   └── README.md
│
└── out/                       Generated artifacts (plots, exported data)
    └── phase0_raytrace.png
```

## Where things go

| Want to add...                              | Put it in...                        |
|---------------------------------------------|-------------------------------------|
| A new spacetime metric (Ellis, Teo, MMP)    | `py/stargate/metrics/<slug>.py`     |
| A new integrator (Yoshida, JAX-batched)     | `py/stargate/integrators/<slug>.py` |
| A new validation gate (Schwarzschild, Müller)| `py/stargate/validation/<slug>.py`  |
| A pytest assertion for any of the above     | `tests/test_<slug>.py`              |
| A new theory entry                          | `theories/<slug>.md` (use template) |
| A specialist research brief                 | `docs/team_briefs/NN_<slug>.md`     |
| A new department / role                     | edit `departments/org_chart.md`     |
| Lab BOM line / parts arrival / measurement  | append to `lab/`                    |
| Anything you'd run from the command line    | `scripts/<slug>.py`                 |

## Future placeholders

These directories are not yet created — they are reserved names so we don't
collide later when the agents that own them spin up.

| Path                    | Owner | Purpose                                     |
|-------------------------|-------|---------------------------------------------|
| `rs/`                   | E2    | Rust/WASM physics core (when shader-only insufficient) |
| `web/`                  | E1    | Three.js + WebGPU frontend, GH Pages target |
| `web/shaders/wgsl/`     | E2    | WGSL geodesic-march shaders                 |
| `data/`                 | O3    | arxiv watch dumps, theory-card metadata     |
| `theories/_ranking.md`  | R1    | Auto-generated rank table                   |

## Conventions

- **Branches:** work on feature branches; merge to `main` only after `pytest`
  is green.
- **Imports:** within `stargate/`, use relative imports (`from ..geodesics
  import ...`). External callers use `from stargate.X import Y`.
- **Citations:** every claim of fact in a brief, theory entry, or doc cites
  arXiv ID or DOI. Unverified claims are explicitly flagged `[unverified]` —
  never silently laundered.
- **Numerics:** anything that ships a number ships a tolerance and a
  validation fixture. Numbers without bounds become folklore.
- **Comments in code:** default is none. Add only when *why* is non-obvious.
  Module/file docstrings explain *what* and *where in the science* the file
  comes from; line comments are for genuine surprises.
