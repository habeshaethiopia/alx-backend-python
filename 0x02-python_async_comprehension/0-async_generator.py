#!/usr/bin/env python3
"""module to wait 10 sec"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """generator for async"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
