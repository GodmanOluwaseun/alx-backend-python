#!/usr/bin/env python3

"""2-measure_runtime
Measures total time for executing Async coroutines and returns the time.
"""


import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures runtime of coroutines & returns average time for each"""

    start = time()
    asyncio.run(wait_n(n, max_delay))
    stop = time()

    total_time = stop - start
    time_n = total_time / n
    return time_n
