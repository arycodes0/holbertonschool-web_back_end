#!/usr/bin/env python3
"""This module takes an iterable of sequences and returns a list of tuples."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate and return a list of tuples, where each tuple
    contains an element from the input iterable
    and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequences (e.g., lists, strings, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where
        each tuple contains a sequence from the input
        iterable and its length.
    """
    return [(i, len(i)) for i in lst]
