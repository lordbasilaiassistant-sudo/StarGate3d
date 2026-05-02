# Lab Notebook

```
+==============================================================================+
|  LAB OPERATIONS                                                              |
|  DOC ID: SG3D-LAB-001     REV: 0.1     DATE: 2026-05-01                      |
|  PHASE: pre-build (no parts ordered yet)                                     |
+==============================================================================+
```

This directory holds everything that happens at the bench. Order BOMs, parts
arrival, build photos (when committed by drlor only), gauss-meter readings,
calibration logs, raw measurement files. Numbers are committed as CSVs;
analysis lives in `py/stargate/` modules that read them.

## File conventions

```
lab/
├── README.md                    <-- this
├── boms/
│   └── phase1_magnetic_wormhole.md     pending Vance R3 finalization
├── notebook/
│   └── YYYY-MM-DD-<slug>.md            one entry per session
├── data/
│   └── YYYY-MM-DD-<slug>.csv           raw measurements with metadata header
└── photos/
    └── YYYY-MM-DD-<slug>.jpg           reproducible setup shots
```

## Notebook entry template

```markdown
# YYYY-MM-DD  <Slug>

**Apparatus:**   <which build, in which configuration>
**Operator:**    drlor
**Witness:**     <name or `solo`> — required per Torres §4 if hazard run
**Goal:**        <one sentence>
**Outcome:**     <one sentence — write this AFTER, not before>

## Setup
Photo refs, deltas from previous run, calibration check.

## Procedure
Numbered steps, exactly what was done.

## Measurements
Link to data/<filename>.csv. Headline numbers inline with units.

## Observations
Anything unexpected. What instrument did the surprise come from.

## Next
What changes for the next run.
```

## Active builds

(none yet — Phase-1 mu-metal magnetic-wormhole BOM is being finalized)

## Hard NOs (per Capt. Torres R11)

See `docs/team_briefs/11_lab_safety_apartment_ops.md` §4. Summary of what
does NOT enter this apartment regardless of motivation:

- HV pulse capacitors > 10 J / > 100 V
- Class 3B+ lasers, RF > 100 mW
- Uncontained LN₂ in shared living space
- BEC laser-cooling apparatus (university lab only)
- UHV bake-out (high-temp + electrical)

## Pre-run checklist (every hazard run)

```
[ ]  Lucia's location confirmed (away or in green-zone bedroom with door closed)
[ ]  Phone witness reachable and informed of run window
[ ]  Hazard zone marked (sign on door)
[ ]  Fire extinguisher within reach
[ ]  Dead-man timer set (audible alarm if no check-in within N minutes)
[ ]  Camera or audio recording the run (single-operator runs)
[ ]  Pre-run measurements logged (instrument zero, baseline)
[ ]  Post-run secure-and-store plan written before starting
```
