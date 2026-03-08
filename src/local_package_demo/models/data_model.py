from dataclasses import dataclass


@dataclass
class SignalResult:
    """
    Container for processed signal results.
    """

    raw_mean: float
    normalized_value: float