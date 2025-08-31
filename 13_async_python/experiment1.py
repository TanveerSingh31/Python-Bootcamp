import asyncio
import time

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished")

def main2():
    print("main2 called")
    time.sleep(5)   # blocks event loop
    print("main2 ended")

async def main():
    # Schedule tasks but don’t wait yet
    asyncio.create_task(task("A", 2))
    asyncio.create_task(task("B", 1))
    asyncio.create_task(task("C", 3))

    # Block the event loop
    main2()

    # Give event loop time to run pending tasks
    await asyncio.sleep(0)

asyncio.run(main())