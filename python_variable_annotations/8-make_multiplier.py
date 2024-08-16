#!/usr/bin/env python3
"""This module takes a float multiplier and returns
a function that multiplies a float by multiplier."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The multiplier to use for the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        it multiplied by the given multiplier.
    """
    def multiply_by(value: float) -> float:
        return value * multiplier

    return multiply_by
