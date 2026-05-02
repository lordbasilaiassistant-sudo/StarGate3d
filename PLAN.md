# Plan

Build order: cheap test → simulator → theory ledger → buildable analogue.
Same loop as everything else: validate before building, no teams for
unvalidated ideas, kill on evidence.

## Phase 0 — The 20-line test (this week)

Before anything else, prove the simulator core works.

- Pick a Morris–Thorne metric with a fixed throat radius `b0`.
- Trace one light ray from outside the throat, through it, out the other side.
- Plot it. Does it look like the picture in Morris & Thorne (1988)?
- If yes → build the rest. If no → fix the integrator before adding any UI.

`scripts/raytrace_throat.py` — single file, scipy ODE, matplotlib plot. No
WebGL, no scene graph, no engine. Just the math.

Kill criteria: if we can't reproduce the standard wormhole-lensing image in a
weekend, we don't have the physics handle yet and shouldn't be building a
3D world around it.

## Phase 1 — Simulator (weeks 2–6)

Goal: a browser scene where the user walks up to a wormhole mouth and looks
through it. Light is integrated through the real metric, not faked.

Stack:
- **Three.js + WebGPU** for rendering. Free hosting on GitHub Pages.
- **Custom raymarched fragment shader** that walks geodesics in curved
  spacetime per pixel. Reference: Riazuelo's "Voyage au coeur d'un trou noir"
  approach, adapted from Schwarzschild to Morris–Thorne.
- **WASM physics core** (Rust or C++) for the geodesic integrator if the
  shader is too slow.
- Scene 1: Morris–Thorne wormhole. Scene 2: rotating Teo wormhole. Scene 3:
  Ellis drainhole. Scene 4: Maldacena–Milekhin–Popov stabilized throat.

User can:
- Translate/orient at the mouth.
- Step through.
- Toggle exotic-matter density visualization (where would it have to live, and
  how much).
- See the failure modes — what happens when the throat closes, when ANEC is
  violated, when you exceed the energy budget.

## Phase 2 — Theory ledger (parallel)

`theories/` directory. One markdown file per portal mechanism. Each file:

- Mechanism (1 paragraph)
- Required ingredients (with units)
- Simulator scene that demonstrates it
- Lab analogue, if any
- Materials and rough cost for tabletop version
- Current experimental status (real citations)
- Kill criteria (what evidence ends this line)
- Open questions

Initial entries to write:

1. `morris-thorne.md` — classical traversable wormhole
2. `casimir-stabilized.md` — Maldacena/Milekhin/Popov route
3. `er-epr.md` — wormhole-via-entanglement (Sycamore experiment, scaling)
4. `magnetic-metamaterial.md` — Prat-Camps replication path (cheapest, real)
5. `acoustic-analogue.md` — phonon-horizon experiments
6. `bec-analogue.md` — Bose-Einstein condensate gates
7. `optical-metamaterial.md` — Pendry-style EM cloaks → EM wormholes
8. `alcubierre.md` — warp metric, included for completeness
9. `krasnikov-tube.md` — alternative to wormhole topology
10. `vacuum-engineering.md` — dynamical Casimir, squeezed vacuum

Each gets a simulator scene and a cost line. After 10 are filled, rank by
(buildable cost) × (probability of producing something traversable) and pick
the top 1–3 to push hard.

## Phase 3 — Buildable analogue (after ranking)

Almost certainly the magnetic-metamaterial path first. It's the only one with
a confirmed working benchtop demo and a published BOM under $5k.

Steps:
1. Replicate Prat-Camps (2015) with cheaper materials. Validate with a
   gauss-meter that field lines vanish on one side and reappear on the other.
2. Scale: bigger shells, stronger source, see if you can pass an object whose
   detection mechanism is purely magnetic (a Hall sensor on a stick) "through"
   the gate in the sense that the sensor reads the same field as if it had
   moved continuously when in fact it teleported the field-line topology.
3. Probe: can the analogue be extended to other fields (electrostatic,
   gravimetric)? Where does the math break?
4. Document everything. This is where most projects stop being real and start
   being claims. We post raw measurements.

Constraint: renter, no permanent installs, no >120V wall mods, no licensed
materials, no anything that would put a child in the apartment at risk. Lucia
is six. Heather Moore IG is unreliable. Hard limit on gauss field strength
inside living space.

## Phase 4 — Hand-off (always)

Everything that works gets a one-page reproducer with:
- Parts list with current vendor links
- Wiring/assembly diagram
- Calibration script
- Expected reading at each step

So a stranger with the same parts hits the same numbers. That's how you go
from "Anthony built a thing in his basement" to "humanity has a gate
prototype."

## Distribution & Funding (per global rules)

- Repo is public on GitHub from day 1. No commercial gate.
- Documentation site on GitHub Pages (free).
- Simulator is a static SPA on GitHub Pages or Cloudflare Pages (free).
- If the project shows real progress, apply to: NSF unsolicited proposals,
  Breakthrough Initiatives, FQXi grants, Emergent Ventures (Tyler Cowen),
  Astera Institute, Nat Friedman / Patrick Collison's various funds. None
  before there's a working simulator and at least one replicated bench
  experiment.
- No socials, no peopling, no podcasts. Tweet only on real signals via
  @THRYXAGI: simulator launch, lab replication confirmed, theory killed.

## What This Plan Refuses To Do

- Build before validating. Phase 0 first, every time.
- Promise a working gate. The honest answer is "we don't know yet."
- Pretend the math is settled. ANEC, quantum inequalities, and the Ford-Roman
  bounds may forbid macroscopic traversability. We engage with that, we don't
  hand-wave around it.
- Burn cash on equipment before the simulator says it's worth burning.

## First Action After Init

`scripts/raytrace_throat.py` — the 20-line test. Reproduce Morris-Thorne
lensing. If that plot looks right, we keep going.
