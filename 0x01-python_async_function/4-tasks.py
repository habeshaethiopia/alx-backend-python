#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes
in an integer argument (max_delay, with a default
value of 10) named wait_random that waits for a random
delay between 0 and max_delay (included and float value)
seconds and eventually returns int
"""
import asyncio
import typing

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """function that wait random delay"""
    return sorted([await task_wait_random(max_delay) for _ in range(n)])
