#!/usr/bin/env python3
"""the module for async generator"""
import asyncio
import typing

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """return the async generator"""
    return [i async for i in async_generator()]
