#!/usr/bin/env python3
"""This module takes a list of int and floats
and returns their sum as a float."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate and return the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of int and
        floats to be summed.

    Returns:
        float: The sum of all elements in the mxd_lst as a float.
    """
    return sum(mxd_lst)
