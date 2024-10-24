#!/usr/bin/env python3

"""
This module contains a type-annotated function that takes a string `k`
and an integer or float `v` as args and returns a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This returns a tuple containing the string `k`
    and the square of the float `v`

    Args:
        k (str): This is a string
        v (Union[int, float]): This is an int or float

    Returns:
        Tuple[str, float]: The tuple containing the string `k` and the square
        of the float `v`
    """
    return (k, v ** 2)
