#!/usr/bin/env python3

"""0-basic_async_syntax.py
This defines a coroutine that accepts an int as maxdelay, and awaits
a random delay <= maxdelay.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async coroutine that waits for a random delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
