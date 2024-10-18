#!/usr/bin/env python3

"""1-async_comprehension
Collect 10 random numbers using async_generator, and returns them.
"""


import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collectst 10 random float numbers and returns them."""

    numbers = [i async for i in async_generator()]
    return numbers
