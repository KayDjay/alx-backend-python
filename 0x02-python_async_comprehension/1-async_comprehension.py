#!/usr/bin/env python3
""" Async Comprehensions """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    Asynchronously collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        list[float]: A list containing 10 random numbers.
    """
    return [num async for num in async_generator()]
