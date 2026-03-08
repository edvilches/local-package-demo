"""
Signal processing pipeline.
"""

from ..utils.math_utils import normalize
from .algorithms import compute_mean
from ..config import DEFAULT_NORMALIZATION_VALUE


def process_signal(data: list[float]) -> float:
    """
    Example signal processing pipeline.
    """

    mean_value = compute_mean(data)

    normalized = normalize(mean_value, DEFAULT_NORMALIZATION_VALUE)

    return normalized
    