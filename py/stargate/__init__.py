"""StarGate Research Program — Python ground-truth and verification core.

This package is the offline, high-precision reference. The browser simulator
(WebGPU/WGSL) and any future Rust/WASM core must reproduce the same numerical
results to within published tolerances. CI cross-checks against this code.

Submodules:
    metrics       — pluggable spacetime metrics (Morris-Thorne, Ellis, Teo, ...)
    geodesics     — Hamilton's equations RHS and conserved quantities
    integrators   — pluggable ODE integrators (DOP853, Yoshida-4, ...)
    validation    — numerical fixture gates (Reyes R1 + Lindqvist R4)
    viz           — matplotlib offline plots
"""
__version__ = "0.1.0"
