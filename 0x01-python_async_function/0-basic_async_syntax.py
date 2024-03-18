#!/usr/bin/python3
"""
    The function `wait_random` is an asynchronous coroutine that takes an
    integer argument and returns a random float after a delay.

    :param max_delay: The `max_delay` parameter in the `wait_random` function
    is an integer that specifies the maximum delay in seconds for the
    asynchronous coroutine to wait before returning a random float value,
     defaults to 10
     :type max_delay: int (optional)
    :return: The `wait_random` coroutine returns a float value representing the
    delay that was randomly generated and waited for before returning.
    """

import asyncio
import random

""" Function to asynchronous coroutine that takes an integer argument """


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
