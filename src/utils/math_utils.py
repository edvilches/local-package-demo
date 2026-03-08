"""
Mathematical helper functions.
"""


def normalize(value: float, max_value: float) -> float:
    """
    Normalize a value between 0 and 1.
    """

    return value / max_value