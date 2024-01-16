#!/usr/bin/env python3
"""async finction in python"""
import random
import asyncio


async def wait_random(max_delay=10):
    """the finction"""
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x