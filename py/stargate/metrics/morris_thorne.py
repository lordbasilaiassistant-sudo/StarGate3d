"""Morris-Thorne wormhole, equatorial slice (theta = pi/2).

Reference: Morris & Thorne, Am. J. Phys. 56, 395 (1988).

    ds^2 = -dt^2 + dl^2 + r(l)^2 dphi^2,    r(l) = sqrt(b0^2 + l^2)

l is the proper radial coordinate; l = 0 is the throat. l < 0 is the "other"
universe / mouth; l > 0 is "ours." The unstable photon sphere sits at l = 0
with critical impact parameter b_c = b0.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class MorrisThorne:
    b0: float = 1.0           # throat radius (units where everything is dimensionless)
    name: str = "morris_thorne"

    def r2(self, l):
        return self.b0 * self.b0 + l * l

    def r(self, l):
        return np.sqrt(self.r2(l))

    @property
    def critical_b(self) -> float:
        """Photons with b < b_c traverse; b > b_c reflect; b = b_c orbit."""
        return self.b0

    @property
    def photon_sphere_l(self) -> float:
        """Proper-radial coordinate of the unstable circular null orbit."""
        return 0.0
