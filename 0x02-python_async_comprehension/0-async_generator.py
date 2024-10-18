#!/usr/bin/env python3

"""0-async_generator
Coroutine that takes no arguments and generates random numbers.
"""


import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Coroutine loops, aynchronously waits and yields random number"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
