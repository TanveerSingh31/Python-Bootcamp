import asyncio

async def getData():
    print("Fn start")
    await asyncio.sleep(2)
    print("Fn end...")


asyncio.run(getData())