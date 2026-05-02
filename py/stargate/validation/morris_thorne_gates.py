"""Phase-0 validation gates for the Morris-Thorne integrator.

Source: Reyes R1 brief sec 3 + Lindqvist R4 brief sec 6.

Gate 1.  |H| residual along all trajectories stays below tol (default 1e-8).
Gate 2.  A photon with b < b_c traverses the throat (l crosses 0).
Gate 3.  A photon with b > b_c reflects (p_l flips sign).
Gate 4.  Total winding diverges as -log(b - b_c) near the photon sphere:
         per-decade increments of |phi_max| approach ln(10) = 2.3026
         monotonically from below.

If any of these regress, the integrator and/or metric implementation is
broken — independent of how good the rendered image looks.
"""
from __future__ import annotations
import numpy as np

from ..integrators import integrate_null
from ..geodesics import null_hamiltonian


DEFAULT_L0 = -30.0
DEFAULT_TOL_H = 1e-8
DEFAULT_TOL_LOG = 0.02


def gate_1_hamiltonian_drift(
    metric,
    impact_params=(0.3, 0.7, 0.99, 1.001, 1.2, 2.0, 3.0),
    *,
    l0: float = DEFAULT_L0,
    tol: float = DEFAULT_TOL_H,
):
    """All trajectories must conserve null H to better than `tol`."""
    max_drift = 0.0
    for b in impact_params:
        sol, L = integrate_null(metric, l0, b)
        for i in range(sol.y.shape[1]):
            H = null_hamiltonian(metric, sol.y[:, i], L)
            max_drift = max(max_drift, abs(H))
    return float(max_drift), max_drift < tol


def gate_2_throat_traversal(metric, *, b: float = 0.5, l0: float = DEFAULT_L0):
    """Photons with b < b_c must cross the throat (reach l > 0)."""
    sol, _ = integrate_null(metric, l0, b)
    return bool(np.any(sol.y[0] > 0.5))


def gate_3_reflection(metric, *, b: float = 1.5, l0: float = DEFAULT_L0):
    """Photons with b > b_c must reflect (p_l sign flip)."""
    sol, _ = integrate_null(metric, l0, b)
    return bool(np.any(np.diff(np.sign(sol.y[2]))))


def gate_4_photon_sphere_log_divergence(
    metric,
    *,
    l0: float = DEFAULT_L0,
    decades=(0.1, 0.01, 0.001, 0.0001),
    tol: float = DEFAULT_TOL_LOG,
):
    """Per-decade |phi_max| increments approach ln(10) monotonically."""
    deflections = []
    for db in decades:
        sol, _ = integrate_null(metric, l0, metric.critical_b + db)
        deflections.append(float(np.max(np.abs(sol.y[1]))))
    deltas = np.diff(deflections)
    target = np.log(10.0)
    monotone = bool(np.all(np.diff(deltas) > 0))
    deepest_ok = abs(deltas[-1] - target) < tol
    return deltas, monotone and deepest_ok


def run_all(metric):
    """Run all four gates, return a structured report (used by scripts/CI)."""
    drift, g1 = gate_1_hamiltonian_drift(metric)
    g2 = gate_2_throat_traversal(metric)
    g3 = gate_3_reflection(metric)
    deltas, g4 = gate_4_photon_sphere_log_divergence(metric)
    return {
        "gate_1_hamiltonian_drift": {"value": drift, "pass": g1},
        "gate_2_throat_traversal": {"pass": g2},
        "gate_3_reflection": {"pass": g3},
        "gate_4_photon_sphere_log_divergence": {
            "deltas": [float(d) for d in deltas],
            "deepest_delta": float(deltas[-1]),
            "target_ln10": float(np.log(10.0)),
            "pass": g4,
        },
        "all_pass": all((g1, g2, g3, g4)),
    }
