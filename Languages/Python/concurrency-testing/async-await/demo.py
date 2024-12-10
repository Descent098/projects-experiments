import random
import asyncio # Used to make managing async functions easier

async def get_data():
    print("get_data() running")
    await asyncio.sleep(random.randint(1,15))
    print("get_data() done")
    return "data"

async def do_background_tasks():
    print("do_background_tasks() running")
    ... # Do stuff in the background
    print("do_background_tasks() done")

async def main():
    # A TaskGroup is an easy way to start multiple async functions
    async with asyncio.TaskGroup() as tg:
        a = tg.create_task(get_data())
        tg.create_task(do_background_tasks())

    print(a.result())

if __name__ == "__main__":
    asyncio.run(main())