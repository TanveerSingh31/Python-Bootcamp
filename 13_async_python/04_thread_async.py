import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        # Explantation
        # loop.run_in_executor() -> executes the fn. using another thread in TPE
        # The result gets added to the event queue
        # Event loop then picks the result from the queue, and continues processing further
        result = await loop.run_in_executor(pool, check_stock, "Masala chai")
        print(result)


# Executing multiple main() -> method to check , if multiple blocking calls can be managed by the fn.
async def main_twice():
    await asyncio.gather(
        main(),
        main()
    )    

asyncio.run(main_twice())