#!/usr/bin/env python3
"""Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time"""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function to create asycoio task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
