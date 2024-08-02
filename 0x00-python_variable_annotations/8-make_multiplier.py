#!/usr/bin/env python3

"""
This module contains a type-annotated function `make_multiplier` that
takes a float `multiplier` as arg and returns a function that multiplies
a float by `multiplier`.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This returns a function that multiplies a float by `multiplier`

    Args:
        multiplier (float): this is the value to multiply by

    Returns:
        Callable[[float], float]: this is a function that multiplies a float by
        `multiplier`
    """
    def multiplier_fn(n: float) -> float:
        """
        This returns the product of `n` and `multiplier`.

        Args:
            n (float): this is the value to multiply

        Returns:
            float: this is the product of `n` and `multiplier`
        """
        return n * multiplier
    return multiplier_fn
