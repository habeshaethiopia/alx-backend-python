#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes
in an integer argument """
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time_sync(n: int, max_delay: int) -> float:
    """average run time"""
    st = time.time()
    await wait_n(n, max_delay)
    return (time.time() - st) / n


def measure_time(n: int, max_delay: int) -> float:
    """return the helper function"""
    return asyncio.run(measure_time_sync(n, max_delay))
