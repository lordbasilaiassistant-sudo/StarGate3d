"""Hamilton's equations for null geodesics in axisymmetric metrics.

State vector (equatorial, theta = pi/2):
    y = [l, phi, p_l]
Conserved: E (energy, fixed to 1) and L = p_phi (angular momentum / impact param).

Equations (per Reyes R1 brief, sec 3):
    dl/dlam   = p_l
    dphi/dlam = L / r(l)^2
    dp_l/dlam = L^2 * l / (b0^2 + l^2)^2     (Morris-Thorne form via dr2/dl)

A null geodesic preserves
    H = (1/2) (-E^2 + p_l^2 + L^2 / r(l)^2) = 0.
Drift in H is a direct probe of integrator quality.

This module is metric-agnostic via duck-typing on `metric.r2(l)`. For metrics
beyond Morris-Thorne the derivative `d r^2 / dl` will need to be supplied
(e.g., via `metric.dr2_dl(l)`); we will extend the interface there.
"""
from __future__ import annotations
import numpy as np

E_DEFAULT = 1.0


def null_rhs(metric, _lam, state, L):
    """RHS for null geodesic in (l, phi, p_l) phase space."""
    l, _phi, p_l = state
    r2 = metric.r2(l)
    # For Morris-Thorne with r^2 = b0^2 + l^2, d r^2 / dl = 2 l, so the
    # canonical force on p_l reduces to L^2 * l / r^4.
    # Generalization: dp_l/dlam = (L^2 / 2) * (d r^2 / dl) / r^4
    dr2_dl = getattr(metric, "dr2_dl", None)
    if dr2_dl is None:
        # default Morris-Thorne style: r^2 = b0^2 + l^2 → dr2/dl = 2 l
        force = (L * L) * l / (r2 * r2)
    else:
        force = 0.5 * (L * L) * dr2_dl(l) / (r2 * r2)
    return [p_l, L / r2, force]


def null_hamiltonian(metric, state, L, E=E_DEFAULT):
    """H along the trajectory. Should be 0 for a null geodesic."""
    l, _phi, p_l = state
    return 0.5 * (-E * E + p_l * p_l + (L * L) / metric.r2(l))


def initial_null_state(metric, l0, b, E=E_DEFAULT):
    """Construct (state0, L) for a null geodesic at l0 with impact parameter b.

    Photon launched heading toward +l. Raises ValueError if l0 sits inside a
    classically forbidden region (turning point would already have been
    reached before lam = 0).
    """
    L = b * E
    p_l_sq = E * E - (L * L) / metric.r2(l0)
    if p_l_sq < 0:
        raise ValueError(
            f"forbidden start: b={b}, l0={l0} (turning point inside |l0|)"
        )
    return np.array([l0, 0.0, np.sqrt(p_l_sq)]), L
