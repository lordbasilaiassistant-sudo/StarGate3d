"""ODE integrators for null geodesics.

The R1/R4 briefs disagreed on integrator choice (R1: symplectic for closed
orbits and long traversals; R4: RK4 in 8D phase space because the geodesic
equation is not separable canonically once metrics go off-diagonal). The
`physics_spec.md` resolution: ship multiple, gate everything on the
Hamiltonian-residual check.

Currently shipped:
    scipy_dop853  — high-order embedded RK (8/5/3) via scipy.integrate.solve_ivp
                    Used as the offline ground-truth reference.

Future:
    yoshida4      — 4th-order symplectic for closed light-ring scenes
    rk4_jax       — for batched GPU/TPU runs
"""
from .scipy_dop853 import integrate_null

__all__ = ["integrate_null"]
