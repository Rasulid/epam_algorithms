import asyncio


async def f():
    while True:
        print("f() function")
        await asyncio.sleep(1)
        print("f() function is called")


async def g():
    while True:
        print("g() function")
        await asyncio.sleep(1)
        print("g() function is called")


async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(g())
    task2 = loop.create_task(f())
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
