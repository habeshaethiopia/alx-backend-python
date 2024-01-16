#!/usr/bin/env python3
"""module to measure a runtime"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime():
    """measure the runtime"""
    st=time.time()
    await asyncio.gather(*(async_comprehension()for i in range(4)))
    return time.time()-st


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)

