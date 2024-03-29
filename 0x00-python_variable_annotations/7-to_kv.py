#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a type-annotated function abcd"""
    return (k, float(v**2))
