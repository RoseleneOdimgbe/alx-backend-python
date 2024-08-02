#!/usr/bin/env python3

"""The type-annotated function safe_first_element"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    The function that takes a sequence lst of any type

    Args:
        lst (Sequence[Any]): the sequence of any type

    Returns:
        Union[Any, None]: this returns the first element of the list if
        it exists, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
