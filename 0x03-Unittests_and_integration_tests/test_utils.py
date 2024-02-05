#!/usr/bin/env python3
"""test_utils.py"""
from unittest import TestCase
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from typing import Any, Dict, List, Tuple, Union


class TestAccessNestedMap(TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple, expected: Union[int, Dict]
    ):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
