#!/usr/bin/env python3

"""1-concurrent_coroutines
Executes multiple coroutines at the same time with async.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that spawns n number of coroutines using wait_random"""

    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    return sorted(delays)
