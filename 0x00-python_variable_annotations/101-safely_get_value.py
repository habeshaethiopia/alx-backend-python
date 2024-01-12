#!/usr/bin/env python3
"""annotation"""
from typing import Mapping, Any, Union


def safely_get_value(
    dct: Mapping, key: Any, default: Union[~T, NoneType] = None
) -> Union[Any, ~T]:
    """the function"""
    if key in dct:
        return dct[key]
    else:
        return default
