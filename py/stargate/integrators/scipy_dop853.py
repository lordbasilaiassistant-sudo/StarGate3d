"""scipy DOP853 (8th-order embedded RK) integrator for null geodesics."""
from __future__ import annotations
from scipy.integrate import solve_ivp

from ..geodesics import null_rhs, initial_null_state


def integrate_null(
    metric,
    l0: float,
    b: float,
    *,
    lam_max: float = 200.0,
    rtol: float = 1e-11,
    atol: float = 1e-13,
    max_step: float = 0.05,
):
    """Integrate one null geodesic. Returns (scipy_solution, L)."""
    state0, L = initial_null_state(metric, l0, b)
    sol = solve_ivp(
        lambda lam, y: null_rhs(metric, lam, y, L),
        (0.0, lam_max),
        state0,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=max_step,
        dense_output=True,
    )
    return sol, L
