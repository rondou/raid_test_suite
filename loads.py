import asyncio
import shutil

from pathlib import Path
from aiofile import async_open


async def create_and_write(p):
    loop = asyncio.get_event_loop()

    t = asyncio.current_task()
    temp_filename = p / (t.get_name() + '.txt')
    start = loop.time()
    async with async_open(str(temp_filename), 'a') as afp:
        await afp.write(t.get_name())

    end = loop.time() - start
    print(t.get_name())
    print(end)


async def main():
    loop = asyncio.get_event_loop()
    p = Path(".") / '.cache'
    p.mkdir(parents=True, exist_ok=False)
    start = loop.time()
    async with asyncio.TaskGroup() as tg:
        for _ in range(0, 4000):
            tg.create_task(create_and_write(p))

    end = loop.time() - start
    print('Total time is ', end)

    shutil.rmtree(str(p))


if __name__ == '__main__':
    asyncio.run(main())
