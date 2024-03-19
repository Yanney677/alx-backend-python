#!/usr/bin/env python3
"""Task 4's Module
"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the generate wait_random n times"""
    tasks = [] # Create tasks using task_wait_random
    delays = [] #  Create a list to store task results

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task # Await the task to get the result
        delays.append(delay)

    return delays # Return the list of delays
