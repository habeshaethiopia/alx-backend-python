#!/usr/bin/env python3
"""async finction in python"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """the finction"""
    x = random.uniform(0, max_delay)
    return await asyncio.sleep(x, result=x)
