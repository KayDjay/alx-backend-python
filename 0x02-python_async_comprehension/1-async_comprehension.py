#!/usr/bin/env python3
""" Async Comprehensions """

import asyncio

async_generator = __import__('0-async_generator').async_generator


# async def async_comprehension() -> List[float]:
#     """
#     Asynchronously generates a list of 10 random floating-point numbers between
#     0 and 10 using async_generator.

#     Returns:
#         List[float]: A list containing 10 random floating-point numbers.
#     """
#     return [i async for i in async_generator()][:10]


async def async_comprehension() -> list[float]:
    """
    Asynchronously collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        list[float]: A list containing 10 random numbers.
    """
    return [num async for num in async_generator()][:10]

async def main():
    """
    Asynchronous main function to print the result of async_comprehension.
    """
    print(await async_comprehension())

asyncio.run(main())