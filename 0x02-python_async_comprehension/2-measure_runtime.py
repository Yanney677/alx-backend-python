#!/usr/bin/env python3
"""Task's 2 Module
"""

from  time import perf_counter
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing."""
    start_time = perf_counter()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = perf_counter()
    return end_time - start_time
