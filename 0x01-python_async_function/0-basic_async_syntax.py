#!/usr/bin/python3
""" The BAsics of async """

import asyncio
import random


""" Function to asynchronous coroutine that takes an integer argument """
async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay