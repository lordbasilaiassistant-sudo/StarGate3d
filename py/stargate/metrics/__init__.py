"""Spacetime metrics with conserved quantities for geodesic integration.

A metric class exposes:
    name:                identifier string
    r2(l):               areal radius squared at proper radial coordinate l
    r(l):                areal radius
    critical_b:          critical impact parameter (photon-sphere null orbit)
    photon_sphere_l:     proper-radial coord of unstable null circular orbit

New metrics drop in as one file in this directory; geodesics.py and the
integrator modules consume them duck-typed.
"""
from .morris_thorne import MorrisThorne

__all__ = ["MorrisThorne"]
