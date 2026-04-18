#!/usr/bin/env python3
"""Async generator that yields random numbers"""

import asyncio
import random


async def async_generator():
    """
    Async generator that loops 10 time asynchronously waits 1 second each time
    and yields a random number between 0 and 10

    Yields:
        float: A random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
