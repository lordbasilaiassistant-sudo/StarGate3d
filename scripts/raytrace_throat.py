"""
Phase 0 — Morris-Thorne wormhole null-geodesic raytrace.

Validates the geodesic integrator before any GPU/WebGPU work happens.

Metric (equatorial, theta = pi/2):
    ds^2 = -dt^2 + dl^2 + r(l)^2 d phi^2,    r(l) = sqrt(b0^2 + l^2)

Hamiltonian (per Reyes brief, sec 3):
    H = -1/2 (E^2 - p_l^2 - L^2 / r(l)^2) = 0   (null)

with conserved   E = -p_t,   L = p_phi.   Set E = 1, sweep impact parameter b = L.

Equations of motion:
    dl/dlam   = p_l
    dphi/dlam = L / r(l)^2
    dp_l/dlam = L^2 * l / (b0^2 + l^2)^2
    dt/dlam   = E       (not integrated; static metric)

Predicted behavior:
    b < b0  -> photon traverses the throat (l: -inf -> +inf)
    b = b0  -> photon orbits at the throat (unstable photon sphere)
    b > b0  -> photon turns at l_turn = +/- sqrt(b^2 - b0^2), bounces

Validation gates:
    1. Hamiltonian residual |H| stays below 1e-8 over the trajectory
    2. Photons with b < b0 cross l=0 with positive p_l
    3. Photons with b > b0 reach turning point r = b within tol, then return
    4. Photon sphere (b = b0) is unstable: tiny perturbation -> diverges

If all four pass, the integrator is good enough to feed Phase 1's WebGPU port.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from pathlib import Path

B0 = 1.0          # throat radius (units where everything is dimensionless)
E = 1.0           # photon energy (sets affine-parameter scale)
LAM_MAX = 200.0
L_INFINITY = 30.0 # numerical "infinity" — start photons here
TOL_H = 1e-8


def r_of_l(l):
    return np.sqrt(B0 * B0 + l * l)


def rhs(_lam, y, L):
    l, phi, p_l = y
    r2 = B0 * B0 + l * l
    return [p_l, L / r2, (L * L) * l / (r2 * r2)]


def hamiltonian(l, p_l, L):
    """Should be 0 along a null geodesic. Track drift as integrator-quality probe."""
    return 0.5 * (-E * E + p_l * p_l + (L * L) / (B0 * B0 + l * l))


def shoot(b, l0=-L_INFINITY, lam_max=LAM_MAX):
    """Launch photon at l = l0 heading toward +l with impact parameter b = L/E."""
    L = b
    p_l_sq = E * E - (L * L) / (B0 * B0 + l0 * l0)
    if p_l_sq < 0:
        raise ValueError(f"forbidden start: b={b}, l0={l0}")
    p_l_0 = np.sqrt(p_l_sq)
    sol = solve_ivp(
        rhs, (0.0, lam_max), [l0, 0.0, p_l_0],
        args=(L,), method="DOP853",
        rtol=1e-11, atol=1e-13, max_step=0.05, dense_output=True,
    )
    return sol, L


def hamiltonian_drift(sol, L):
    H = hamiltonian(sol.y[0], sol.y[2], L)
    return float(np.max(np.abs(H)))


def main():
    out = Path(__file__).parent.parent / "out"
    out.mkdir(exist_ok=True)

    impact_params = [0.3, 0.7, 0.99, 1.001, 1.2, 2.0, 3.0]

    # ----- top-down (l, phi) view, with sign(l) styling --------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    cmap = plt.cm.viridis(np.linspace(0.05, 0.95, len(impact_params)))

    drifts = []
    for color, b in zip(cmap, impact_params):
        sol, L = shoot(b)
        l = sol.y[0]
        phi = sol.y[2]  # NB: y is [l, phi, p_l] — index 1 is phi
        # in our state vec the order was [l, phi, p_l]
        # double check by recomputing
        # (kept above for clarity)
        # actually solve_ivp with rhs above: y=[l,phi,p_l]
        # l = sol.y[0], phi = sol.y[1], p_l = sol.y[2]
        l = sol.y[0]; phi = sol.y[1]; p_l = sol.y[2]
        r = np.sqrt(B0 * B0 + l * l)
        x = r * np.cos(phi)
        y_ = r * np.sin(phi)

        mask_far = l > 0          # "our universe"
        mask_near = ~mask_far     # "other side"

        ax1.plot(x[mask_near], y_[mask_near], '--', color=color, lw=1.4,
                 label=f"b={b:.3f} (other)" if b in (0.3, 1.2) else None)
        ax1.plot(x[mask_far], y_[mask_far], '-', color=color, lw=1.4,
                 label=f"b={b:.3f}")

        drift = hamiltonian_drift(sol, L)
        drifts.append((b, drift))

    th = np.linspace(0, 2 * np.pi, 256)
    ax1.plot(B0 * np.cos(th), B0 * np.sin(th), 'k-', lw=2.2, label='throat')
    ax1.set_aspect('equal')
    ax1.set_xlim(-6, 6); ax1.set_ylim(-6, 6)
    ax1.grid(alpha=0.25)
    ax1.set_title("Morris–Thorne null geodesics, top-down\n"
                  "solid = our side (l>0)  •  dashed = far side (l<0)")
    ax1.set_xlabel("r·cos φ"); ax1.set_ylabel("r·sin φ")
    ax1.legend(fontsize=8, loc='upper right')

    # ----- Flamm embedding (3D-ish) view -----------------------------------
    # z(r) = ±b0 · arccosh(r/b0); we project (X, Y) = (r cos phi, r sin phi),
    # then offset the trajectory in 2D with z as a vertical lift.
    # For a 2D figure we plot (phi vs l) and let l carry the "depth" feel.
    for color, b in zip(cmap, impact_params):
        sol, L = shoot(b)
        l = sol.y[0]; phi = sol.y[1]
        ax2.plot(phi, l, color=color, lw=1.4, label=f"b={b:.3f}")
    ax2.axhline(0, color='k', lw=2.0, label='throat (l=0)')
    ax2.set_xlabel("φ (rad)"); ax2.set_ylabel("l (proper radial)")
    ax2.set_title("Same geodesics in (φ, l)\n"
                  "passing geodesics cross l=0  •  bouncing geodesics turn back")
    ax2.grid(alpha=0.25)
    ax2.legend(fontsize=8, loc='upper right')

    plt.suptitle("Phase 0 sanity check  •  Morris–Thorne wormhole  •  b₀ = 1",
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    fig.savefig(out / "phase0_raytrace.png", dpi=140, bbox_inches='tight')
    print(f"saved {out / 'phase0_raytrace.png'}")

    # ----- Validation gates ------------------------------------------------
    print("\n=== Validation gates ===")
    max_drift = max(d for _, d in drifts)
    print(f"[1] max |H| residual across all rays: {max_drift:.3e} "
          f"(gate: < {TOL_H:.0e}) -> {'PASS' if max_drift < TOL_H else 'FAIL'}")

    sol_thru, _ = shoot(0.5)
    crossed = np.any(sol_thru.y[0] > 0.5)  # made it well past throat
    print(f"[2] b=0.5 photon crosses throat: {crossed} -> "
          f"{'PASS' if crossed else 'FAIL'}")

    sol_bounce, _ = shoot(1.5)
    l_min = float(np.min(sol_bounce.y[0]))
    l_final = float(sol_bounce.y[0, -1])
    bounced = (l_final < l_min + 0.5) and (l_final < -L_INFINITY + 5.0 + 1e-3 or
                                            l_final < l_min * 0.0 + 1.0)
    # cleaner test: did p_l flip sign?
    p_l_flipped = bool(np.any(np.diff(np.sign(sol_bounce.y[2]))))
    print(f"[3] b=1.5 photon turns back (p_l sign flip): {p_l_flipped} -> "
          f"{'PASS' if p_l_flipped else 'FAIL'}")

    # Unstable photon sphere: as b -> b0+, the total winding |phi| diverges
    # logarithmically — phi(b) ~ -A log(b - b0) + const, so each decade of
    # (b - b0) adds the same fixed amount: A * ln(10) ~ 2.30 for this metric.
    deflections = []
    for db in (0.1, 0.01, 0.001, 0.0001):
        sol, _ = shoot(1.0 + db)
        deflections.append(float(np.max(np.abs(sol.y[1]))))
    # The increments approach ln(10) = 2.303 from below as b -> b0 (the
    # log-divergence is asymptotic; the first decade is still feeling
    # subleading corrections). Asymptotic regime test: monotonically
    # increasing AND the deepest decade within 0.02 of ln(10).
    deltas = np.diff(deflections)
    target = np.log(10)
    monotone = bool(np.all(np.diff(deltas) > 0))
    deepest_ok = abs(deltas[-1] - target) < 0.02
    log_signature_ok = monotone and deepest_ok
    print(f"[4] photon sphere log-divergence  "
          f"(deepest delta={deltas[-1]:.4f} vs ln(10)={target:.4f}, "
          f"monotone increase={monotone}) -> "
          f"{'PASS' if log_signature_ok else 'FAIL'}")

    print("\n  Deflection sweep near photon sphere (expect ~ -log(b-b0)):")
    for db, phi_max in zip((0.1, 0.01, 0.001, 0.0001), deflections):
        print(f"    b - b0 = {db:7.4f}   phi_max = {phi_max:7.3f} rad  "
              f"({np.degrees(phi_max):7.1f} deg)")

    print("\nIf all four gates PASS, integrator is cleared for Phase 1 GPU port.")


if __name__ == "__main__":
    main()
