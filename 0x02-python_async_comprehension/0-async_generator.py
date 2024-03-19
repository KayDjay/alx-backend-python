#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random


async def async_generator():
    """
    Asynchronously generates random floating-point numbers between 0 and 10.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
