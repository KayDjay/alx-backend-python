#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronously measures the total runtime of calling async_comprehension
    4 times concurrently.

    Returns:
        float: The total runtime of calling async_comprehension 4 times.
    """
    # Record the starting time
    start_time = perf_counter()

    # Execute four instances of async_comprehension concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = perf_counter()
    return end_time - start_time
