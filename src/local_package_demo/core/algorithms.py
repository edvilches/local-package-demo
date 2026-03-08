"""
Numerical algorithms used by the library.
"""

import numpy as np


def compute_mean(data: list[float]) -> float:
    """
    Compute mean value of a dataset.
    """

    return float(np.mean(data))