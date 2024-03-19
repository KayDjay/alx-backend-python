#!/usr/bin/python3
""" The basics of async """

import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronously waits for a random amount of time within
    a specified maximum delay.

    Parameters:
        max_delay (int): The maximum amount of time to wait, in seconds.
        Defaults to 10.

    Returns:
        float: A float value representing the randomly chosen delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
