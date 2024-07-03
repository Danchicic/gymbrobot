import asyncio
import datetime

from sqlalchemy import update, select

from database.base import get_session
from database.models import Workout
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def change_user_week():
    async with get_session() as session:
        now_week = datetime.datetime.now().isocalendar()[1]
        req = update(Workout).values(global_now_week=now_week, now_workout_week=now_week % 5)
        res = await session.execute(req)


async def change_week_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(change_user_week, 'cron', hour=11, minute=38)
    scheduler.start()
    await asyncio.Future()


async def main():
    await change_week_scheduler()


if __name__ == '__main__':
    asyncio.run(main())
