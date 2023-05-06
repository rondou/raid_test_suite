import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiofile import async_open
from pathlib import Path


async def clear():
    p = Path(".") / '.cache'
    while len([i for i in p.iterdir()]) > 20:
        for f in p.iterdir():
            f.unlink(missing_ok=False)
            break


async def test():
    loop = asyncio.get_event_loop()

    p = Path(".") / '.cache'
    p.mkdir(parents=True, exist_ok=True)

    tag = str(loop.time())
    filename = p / (tag + '.txt')
    async with async_open(str(filename), 'a') as afp:
        await afp.write(tag)
    

async def start():
    aio_sch = AsyncIOScheduler(timezone='Asia/Taipei')
    aio_sch.add_job(test, 'interval', seconds=1, max_instances=2)
    aio_sch.add_job(clear, 'interval', seconds=1, max_instances=5)
    aio_sch.start()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(start())
    loop.run_forever()