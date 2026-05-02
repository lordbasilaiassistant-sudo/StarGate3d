"""Phase 0 sanity check — Morris-Thorne null-geodesic raytrace.

Thin orchestrator over the `stargate` package. All the math lives in
`py/stargate/`; this script wires the metric to the validation gates and
saves a diagnostic plot. Run with:

    pip install -e .
    py scripts/raytrace_throat.py

Or set PYTHONPATH=py and run directly.
"""
from __future__ import annotations
import sys
from pathlib import Path

# Make `py/` importable when run directly without `pip install -e .`
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "py"))

import numpy as np
from stargate.metrics import MorrisThorne
from stargate.validation.morris_thorne_gates import run_all
from stargate.viz import plot_phase0_diagnostic


def main() -> int:
    metric = MorrisThorne(b0=1.0)

    report = run_all(metric)
    g1, g2, g3, g4 = (
        report["gate_1_hamiltonian_drift"],
        report["gate_2_throat_traversal"],
        report["gate_3_reflection"],
        report["gate_4_photon_sphere_log_divergence"],
    )

    print("=== Phase 0 validation gates ===")
    print(f"[1] |H| residual           {g1['value']:.3e}    "
          f"{'PASS' if g1['pass'] else 'FAIL'}")
    print(f"[2] b<b0 traverses                                  "
          f"{'PASS' if g2['pass'] else 'FAIL'}")
    print(f"[3] b>b0 reflects                                   "
          f"{'PASS' if g3['pass'] else 'FAIL'}")
    print(f"[4] log-div  delta={g4['deepest_delta']:.4f} vs "
          f"ln(10)={g4['target_ln10']:.4f}    "
          f"{'PASS' if g4['pass'] else 'FAIL'}")

    print("\n  Per-decade phi increments (expect ln(10)):")
    for d in g4["deltas"]:
        print(f"    {d:7.4f}")

    out = ROOT / "out" / "phase0_raytrace.png"
    plot_phase0_diagnostic(metric, save_to=out)
    print(f"\nplot saved -> {out}")

    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
