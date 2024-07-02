from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


async def insert_user_by_telegram_id(session: AsyncSession, telegram_id: int):
    async with session.begin():
        req = insert(User)
        await session.execute(req, {"telegram_id": telegram_id})


async def get_user_by_telegram_id(session: AsyncSession, telegram_id: int):
    async with session.begin():
        req = select(User).where(User.telegram_id == telegram_id)
        res = await session.execute(req)
        return res.scalar()
