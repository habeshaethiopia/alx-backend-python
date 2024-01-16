#!/usr/bin/env python3
"""module to wait 10 sec"""
import asyncio
import random


async def async_generator():
    """generator for async"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
