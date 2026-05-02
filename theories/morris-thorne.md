# Morris–Thorne Wormhole

**Status:**  ACTIVE
**Owner:**   R1 (Reyes — theoretical GR)
**Sim scene:** S1 (per `docs/physics_spec.md`)
**Last reviewed:** 2026-05-01

## §1  Mechanism

A static, spherically symmetric, non-singular Lorentzian solution to Einstein's
equations connecting two asymptotically-flat regions through a "throat." The
1988 paper (Morris & Thorne, *Am. J. Phys.* **56**, 395) proved such geometries
satisfy the field equations for *any* desired traversability profile — but only
if the matter that sources them violates the Null Energy Condition.

## §2  Required ingredients

- Throat radius `b₀` (free).
- Shape function `b(r)` with `b(b₀) = b₀` and a flare-out condition.
- Stress-energy tensor with `ρ + p_r < 0` at the throat (NEC violation).
- For a 1 m throat with the standard shape `b(r) = b₀² / r`, the local NEC
  violation integrated over the throat surface needs ~ −10⁴¹ J·s · c⁻¹ of
  exotic stress-energy ("negative Casimir-equivalent" if you want a unit you
  can hold). [Ford-Roman QI tightens this further — see §6.]

## §3  Predictions the simulator must make

- **Lensing pattern at the mouth.** A photon shot at impact parameter `b < b₀`
  traverses the throat; `b > b₀` reflects; `b = b₀` orbits unstably.
- **Logarithmic deflection-angle divergence** at the photon sphere — total
  winding `|Δφ| ~ −log(b − b₀)`, with per-decade increment → ln(10).
  ✅ Reproduced numerically by `scripts/raytrace_throat.py` (Phase 0,
  2026-05-01, deepest decade 2.298 vs ln(10)=2.303).
- **Two-sky view through the throat** — the "other side" appears compressed
  into a circular window on the user's sky.
- **No event horizon, no time dilation discontinuity** as you cross l=0.

## §4  Lab analogue (if any)

None directly — Morris–Thorne is a pure GR construction. The closest analogue
is the Prat-Camps 2015 magnetic wormhole (`magnetic-metamaterial.md`), which
mimics the *topological* effect (field-line topology change without a
detectable path between mouths) for magnetostatics, not for spacetime.

## §5  Materials & rough cost

For the simulator scene: free (geodesic integrator + Three.js/WebGPU).
For an actual gate: `[unverified]` — NEC-violating matter at macroscopic scale
has no known production method. The MMP route (`mmp-stabilized.md`) provides
the only known *theoretically consistent* construction, but at planetary mass
budgets and requiring physics beyond the Standard Model.

## §6  Current experimental status

- **Pure GR side:** the math is settled and uncontested (Morris-Thorne 1988,
  arXiv:gr-qc/9802046 Hochberg-Visser NEC theorem).
- **Energy-condition wall:** Ford-Roman quantum inequality (arXiv:gr-qc/9410043,
  arXiv:gr-qc/9510071) restricts how much negative-energy density you can
  concentrate, and over what timescale. For Morris-Thorne in 4D, the
  consequence (Pfenning-Ford arXiv:gr-qc/9711030) is that the throat must be
  thinner than √(l_P · r₀) — for a 1 m throat, **~4×10⁻¹⁸ m**. This kills any
  4D-local construction at any human scale.
- **Loopholes:** semiclassical / higher-dimensional Casimir energy (MMP,
  arXiv:1807.04726, arXiv:2008.06618), modified gravity, brane projections
  (`mmp-stabilized.md`).

## §7  Kill criterion

This entry stays ACTIVE as a **simulator scene and pedagogical baseline**
regardless — it's the canonical wormhole geometry and the entry point for
every subsequent metric. As a *buildable construct*, it is already effectively
killed by Ford-Roman QI; the line is preserved by routing physical
buildability claims through the higher-dim / MMP entries.

A definitive close on this entry as a *physical mechanism* would require:

- A proven, distinct workaround to ANEC at macroscopic scale, or
- A no-go theorem strengthening Ford-Roman to forbid all currently-named
  loopholes (see Fewster-Roman 2024 review, arXiv:2405.05963).

## §8  Open questions

- Is there a sharper version of the Ford-Roman bound that closes the
  semiclassical loophole? (Fewster-Roman 2024 hints toward yes.)
- Does any non-trivial topology of `b(r)` evade the standard energy-condition
  proofs? Hochberg-Visser 1998 says no for the static case; what about
  dynamical?
- Could a proper-time-bounded "puff" of NEC-violating stress (instead of
  static) thread a throat for long enough to traverse, while still respecting
  the QI? (Open; relevant to any "transient" gate proposal.)
