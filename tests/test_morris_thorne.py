"""Phase-0 validation gates as pytest assertions.

These run on every push and gate any change to the metric, geodesic RHS, or
integrator. If any of them flips red, do NOT trust the WGSL port until the
Python ground truth is green again.
"""
import numpy as np
import pytest

from stargate.metrics import MorrisThorne
from stargate.validation.morris_thorne_gates import (
    gate_1_hamiltonian_drift,
    gate_2_throat_traversal,
    gate_3_reflection,
    gate_4_photon_sphere_log_divergence,
    run_all,
)


@pytest.fixture
def metric():
    return MorrisThorne(b0=1.0)


def test_gate_1_hamiltonian_drift_machine_precision(metric):
    """Null Hamiltonian must be conserved to ~1e-14 with DOP853 + tight tol."""
    drift, ok = gate_1_hamiltonian_drift(metric)
    assert ok, f"|H| drift {drift:.3e} exceeded gate (1e-8)"
    assert drift < 1e-12, f"unexpected drift loss: {drift:.3e}"


def test_gate_2_subcritical_traverses_throat(metric):
    """A photon with b < b_c must reach l > 0."""
    assert gate_2_throat_traversal(metric)


def test_gate_3_supercritical_reflects(metric):
    """A photon with b > b_c must reflect (p_l flips sign at the turning pt)."""
    assert gate_3_reflection(metric)


def test_gate_4_photon_sphere_log_divergence(metric):
    """Per-decade |phi_max| increments approach ln(10) monotonically.

    This is the hard test: the unstable photon sphere at l=0 produces
    deflection that diverges as -log(b - b_c). If RK steps are wrong or the
    metric is wrong, the divergence rate or its monotonicity fails.
    """
    deltas, ok = gate_4_photon_sphere_log_divergence(metric)
    assert ok, (
        f"log-divergence signature wrong: deltas={deltas}, "
        f"deepest={deltas[-1]:.4f}, target={np.log(10.0):.4f}"
    )
    # Deepest decade should be within 0.01 of ln(10) — nice-to-have tightening
    # of the gate tol (0.02) so we notice subtle drift before the gate trips.
    assert abs(deltas[-1] - np.log(10.0)) < 0.01


def test_run_all_reports_pass(metric):
    """Sanity: the rolled-up report agrees with the individual gates."""
    report = run_all(metric)
    assert report["all_pass"]
    assert report["gate_1_hamiltonian_drift"]["pass"]
    assert report["gate_2_throat_traversal"]["pass"]
    assert report["gate_3_reflection"]["pass"]
    assert report["gate_4_photon_sphere_log_divergence"]["pass"]


def test_critical_b_matches_b0(metric):
    """For Morris-Thorne with shape r(l)=sqrt(b0^2+l^2), b_c = b0."""
    assert metric.critical_b == metric.b0
    assert metric.photon_sphere_l == 0.0


def test_metric_is_smooth_at_throat(metric):
    """r2 has its minimum at the throat and equals b0^2 there."""
    assert metric.r2(0.0) == metric.b0 ** 2
    # numerical derivative dr2/dl at l=0 should be 0 (throat = minimum)
    eps = 1e-6
    deriv = (metric.r2(eps) - metric.r2(-eps)) / (2 * eps)
    assert abs(deriv) < 1e-9
