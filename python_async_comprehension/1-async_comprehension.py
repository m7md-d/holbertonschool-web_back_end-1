#!/usr/bin/env python3
"""Async comprehension module"""

from importlib import import_module

async_generator = import_module('0-async_generator').async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using async comprehension
    over async_generator and returns them.
    
    Returns:
        list: A list of 10 random numbers from async_generator
    """
    return [i async for i in async_generator()]
