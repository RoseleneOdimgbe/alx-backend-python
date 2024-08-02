#!/usr/bin/env python3

"""This function adds annotations for the function below


```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This is the function that takes a list of sequences and
    returns a list of tuples
    where each tuple contains a sequence and its length

    Args:
        lst (Iterable[Sequence]): This is the list of sequences

    Returns:
        List[Tuple[Sequence, int]]: The list of tuples where
        each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
