#!/usr/bin/env python3
"""test_utils.py"""
from unittest import TestCase
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from typing import (
    Dict,
    Union,
    Tuple,
    Sequence,
    Mapping,
)


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

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        exception: Exception,
    ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test get_json"""
        attrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=mock(**attrs)) as mock_request:
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize"""

    def test_memoize(self) -> None:
        """Test memoize"""

        class TestClass:
            """Test class"""

            def __init__(self) -> None:
                self._a = 0

            @memoize
            def a(self) -> int:
                """a method"""
                self._a += 1
                return self._a

            with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
            ) as memo_fxn:
                test_class = TestClass()
                self.assertEqual(test_class.a_property(), 42)
                self.assertEqual(test_class.a_property(), 42)
                memo_fxn.assert_called_once()
