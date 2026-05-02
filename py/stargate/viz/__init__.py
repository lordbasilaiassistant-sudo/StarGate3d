"""Offline matplotlib visualizations. The browser simulator owns the live view;
this module produces static figures used in PRs, CI artifacts, and docs.
"""
from .topdown import plot_phase0_diagnostic

__all__ = ["plot_phase0_diagnostic"]
