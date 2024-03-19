#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronously measures the total runtime of calling async_comprehension
    4 times concurrently.

    Returns:
        float: The total runtime of calling async_comprehension 4 times.
    """
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime


if __name__ == "__main__":
    print(asyncio.run(measure_runtime()))
