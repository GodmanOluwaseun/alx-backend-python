#!/usr/bin/env python3

"""4-tasks
Alter wait_n, it executes multiple coroutines at the same time with async.
"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that spawns n number of coroutines using wait_random"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*tasks)

    return sorted(delays)
