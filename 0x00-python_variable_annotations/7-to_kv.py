#!/usr/bin/env python3
"""a type-annotated function"""

from typing import Union


def to_kv(k: str, v: Union[int | float]) -> tuple:
    """a type-annotated function"""
    return (k, v**2)
