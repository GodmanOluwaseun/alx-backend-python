#!/usr/bin/env python3

"""2-measure_runtime
Measures time taken to run async coroutines.
"""


import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures and returns time taken to run async coroutines."""

    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    stop = time()

    total_time = stop - start
    return total_time
