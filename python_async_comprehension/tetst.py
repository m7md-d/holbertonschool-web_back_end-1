#!/usr/bin/env python3
import asyncio
from typing import AsyncGenerator


async def m() ->AsyncGenerator[float, None]:
    number = 10
    for i in range(10):
        yield  float(number-= 1)
async def yazeed():
    async for value in m():
        print(value)
if __name__ == "__main__":
    asyncio.run(yazeed())