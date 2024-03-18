#!/usr/bin/python3
""" To execute multiple coroutines at the same time """

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