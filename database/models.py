import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger, DateTime
from .base import Base
from sqlalchemy.orm import validates


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger, unique=True)


class Days(Base):
    __tablename__ = 'days'

    id = Column(Integer, primary_key=True)
    name = Column(String(10))


class Exercises(Base):
    __tablename__ = 'exercises'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=False)
    max_weight = Column(Integer)


class Workout(Base):
    __tablename__ = 'workout'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user = Column(ForeignKey('user.id', ondelete="CASCADE"))
    day = Column(ForeignKey('days.id', ondelete="CASCADE"))
    exercise = Column(ForeignKey('exercises.id', ondelete="CASCADE"))
    now_workout_week = Column(Integer)
    global_now_week = Column(Integer, default=datetime.datetime.now().isocalendar()[1])
    date_create = Column(DateTime, nullable=False, autoincrement=True)
    date_update = Column(DateTime, nullable=False, autoincrement=True)

    @validates("now_week")
    def validate_now_week(self, key, week):
        if week in (0, 1, 2, 3):
            return week
