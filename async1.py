"""
Introduction to coroutine
-------------------------------
- how to write coroutine?
- how to execute coroutine?

"""
import asyncio
import time


async def main():   # `main` is `coroutine`
    print(f"started at {time.strftime('%X')}")
    print("hello")
    await asyncio.sleep(1)  # a running function is suspended in middle
    print("world")
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

