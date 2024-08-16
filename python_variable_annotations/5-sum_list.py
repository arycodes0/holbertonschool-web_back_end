#!/usr/bin/env python3
"""This module takes a list of floats and returns their sum."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate and return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers to be summed.

    Returns:
        float: The sum of all floats in the input_list.
    """
    return sum(input_list)
