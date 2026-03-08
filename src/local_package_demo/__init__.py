"""
local_package_demo

Example scientific library.
"""

from .core.processing import process_signal
from .core.algorithms import compute_mean

__all__ = [
    "process_signal",
    "compute_mean",
]
