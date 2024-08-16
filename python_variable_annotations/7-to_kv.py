#!/usr/bin/env python3
"""This module takes a string and an int
or float as arg and returns a tuple."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a given int or float.

    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): The value to be squared for the
        second element of the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is
        the string k, and the second element is the square of v,
        as a float.
    """
    return (k, float(v ** 2))
