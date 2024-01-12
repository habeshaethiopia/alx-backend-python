#!/usr/bin/env python3
"""the module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """making annotate"""
    return [(i, len(i)) for i in lst]
