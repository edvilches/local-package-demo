"""
Simple IO utilities.
"""

import json


def save_results(data: dict, filename: str):

    with open(filename, "w") as f:
        json.dump(data, f)


def load_results(filename: str) -> dict:

    with open(filename) as f:
        return json.load(f)
