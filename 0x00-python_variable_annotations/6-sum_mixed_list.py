#!/usr/bin/env python3

"""
This is a type-annotated function sum_mixed_list which takes a
list `mxd_lst` of integers and floats and returns their
sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This returns the sum of a list of integers and floats as a float

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats

    Returns:
        float: This is the sum of the list of integers and floats
    """
    return sum(mxd_lst)
