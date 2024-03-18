#!/usr/bin/python3
"""
    The `wait_n` function executes multiple coroutines simultaneously and returns a
    sorted list of the delays.
    
    :param n: The parameter `n` in the `wait_n` function represents the number of
    coroutines you want to execute simultaneously. It determines how many coroutines
    will be created and executed concurrently using asyncio
    :type n: int
    :param max_delay: The `max_delay` parameter in the `wait_n` function represents
    the maximum delay in seconds that each coroutine should wait before completing.
    This value is used when calling the `wait_random` coroutine to generate a random
    delay between 0 and `max_delay` seconds
    :type max_delay: int
    :return: The `wait_n` function returns a sorted list of floats representing the
    delays returned by executing multiple coroutines concurrently using asyncio.
    """


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

"""Function to execute multiple coroutines at the same time"""
    
async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    for task in tasks:
        delay = await task
        delays.append(delay)
    return sorted(delays)