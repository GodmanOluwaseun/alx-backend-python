#!/usr/bin/env python3

"""0-async_generator
Coroutine that takes no arguments and generates random numbers.
"""


import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[int, None]:
    """Coroutine loops, aynchronously waits and yields random number"""

    for i in range(10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
