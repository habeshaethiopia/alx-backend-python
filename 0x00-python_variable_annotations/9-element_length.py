#!/usr/bin/env python3
"""the module"""
from typing import Iterator, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """making annotate"""
    return [(i, len(i)) for i in lst]

    {
        "lst": typing.Iterable[typing.Sequence],
        "return": typing.List[typing.Tuple[typing.Sequence, int]],
    }
