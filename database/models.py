from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger
from .base import Base
from sqlalchemy.orm import validates


class User(Base):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger)


class Days(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(10))


class Exercises(Base):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)


class Workout(Base):
    user = Column(ForeignKey(User, ondelete="CASCADE"))
    day = Column(ForeignKey(Days, ondelete="CASCADE"))
    exercise = Column(ForeignKey(Exercises, ondelete="CASCADE"))
    max_weight = Column(Integer)
    now_week = Column(Integer)

    @validates("now_week")
    async def validate_now_week(self, key, week):
        if week in (0, 1, 2, 3):
            return True
