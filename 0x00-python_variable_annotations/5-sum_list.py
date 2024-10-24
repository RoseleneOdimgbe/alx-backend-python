#!/usr/bin/env python3

"""
This module contains a function that sums the elements of a list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This sums the elements of a list of floats

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: This is the sum of the elements of the list
    """
    return sum(input_list)
