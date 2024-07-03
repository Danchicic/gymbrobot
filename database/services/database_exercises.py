import asyncio
import datetime

from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.base import get_session, init_models, engine
from exeptions.user_exceptions import WrongDayName
from database.models import Exercises, Days, User, Workout

from .database_users import get_user_by_telegram_id


async def create_user_exercises(session: AsyncSession, exercises: dict):
    user_exercises_objects = []
    for name, max_weight in exercises.items():
        user_exercises_objects.append(
            Exercises(
                name=name,
                max_weight=max_weight
            )
        )
    async with session.begin():
        session.add_all(user_exercises_objects)
        await session.commit()
    return user_exercises_objects


async def select_user_day(_session: AsyncSession, day: str) -> Days:
    async with _session.begin():
        req = select(Days).where(Days.name == day)
        res = await _session.execute(req)
        day_object = res.scalar()
        if day_object is None:
            raise WrongDayName(f"Wrong day name\nYour input: {day}")
        return day_object


async def create_user_workout(session: AsyncSession, user_exercises: dict, telegram_id: int):
    user: User = await get_user_by_telegram_id(session, telegram_id)
    workout_day: Days = await select_user_day(session, user_exercises['day'].lower())
    exercises = await create_user_exercises(session, user_exercises['exercises'])
    print("exes", exercises)
    async with session.begin():
        user_workout_objects = [
            Workout(
                user=user.id,
                day=workout_day.id,
                exercise=exercise.id,
                now_workout_week=0,
                date_create=datetime.datetime.now(),
                date_update=datetime.datetime.now()

            )
            for exercise in exercises
        ]
        print("wow got them", user_workout_objects)
        session.add_all(user_workout_objects)
        await session.commit()
