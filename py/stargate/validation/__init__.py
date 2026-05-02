"""Numerical validation gates.

Every metric ships a battery of fixtures that the integrator must pass before
its output is trusted. Currently:
    morris_thorne_gates  — the 4 Phase-0 gates (R1 + R4 lineage)

Future:
    schwarzschild_gates  — analytic deflection cross-check (R4 §6 T1)
    teo_gates            — rotating-wormhole frame-dragging consistency
"""
from . import morris_thorne_gates  # noqa: F401

__all__ = ["morris_thorne_gates"]
