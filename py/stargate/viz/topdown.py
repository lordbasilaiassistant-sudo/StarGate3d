"""Two-panel diagnostic plot: top-down (r cos phi, r sin phi) + (phi, l)."""
from __future__ import annotations
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from ..integrators import integrate_null


def plot_phase0_diagnostic(
    metric,
    impact_params=(0.3, 0.7, 0.99, 1.001, 1.2, 2.0, 3.0),
    *,
    l0: float = -30.0,
    save_to: str | Path | None = None,
    title: str = "Phase 0 sanity check  -  Morris-Thorne wormhole",
):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    cmap = plt.cm.viridis(np.linspace(0.05, 0.95, len(impact_params)))

    for color, b in zip(cmap, impact_params):
        sol, _ = integrate_null(metric, l0, b)
        l, phi, _ = sol.y
        r = np.sqrt(metric.r2(l))
        x, y_ = r * np.cos(phi), r * np.sin(phi)

        far, near = (l > 0), (l <= 0)
        ax1.plot(x[near], y_[near], "--", color=color, lw=1.4)
        ax1.plot(x[far], y_[far], "-", color=color, lw=1.4,
                 label=f"b={b:.3f}")
        ax2.plot(phi, l, color=color, lw=1.4, label=f"b={b:.3f}")

    th = np.linspace(0, 2 * np.pi, 256)
    bc = metric.critical_b
    ax1.plot(bc * np.cos(th), bc * np.sin(th), "k-", lw=2.2, label="throat")
    ax1.set_aspect("equal")
    ax1.set_xlim(-6, 6); ax1.set_ylim(-6, 6); ax1.grid(alpha=0.25)
    ax1.set_title("null geodesics, top-down\n"
                  "solid = our side (l>0)  -  dashed = far side (l<0)")
    ax1.set_xlabel("r cos phi"); ax1.set_ylabel("r sin phi")
    ax1.legend(fontsize=8, loc="upper right")

    ax2.axhline(0, color="k", lw=2.0, label="throat (l=0)")
    ax2.set_xlabel("phi (rad)"); ax2.set_ylabel("l (proper radial)")
    ax2.set_title("same geodesics in (phi, l)")
    ax2.grid(alpha=0.25)
    ax2.legend(fontsize=8, loc="upper right")

    plt.suptitle(title, fontsize=13, fontweight="bold")
    plt.tight_layout()

    if save_to is not None:
        save_to = Path(save_to)
        save_to.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_to, dpi=140, bbox_inches="tight")
        plt.close(fig)
        return save_to
    return fig
