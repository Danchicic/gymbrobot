import datetime

from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from FSM.BaseContext import FSMDefaultContext
from exeptions.user_exceptions import WrongDayName

from database.services.database_exercises import create_user_workout
from keyboards import K
from services import unparse_user_workout
import traceback

router: Router = Router()


# commands router file

@router.message(StateFilter(FSMDefaultContext.get_workout))
async def get_user_workout(message: Message, state: FSMContext, session: AsyncSession):
    async for exercises_data in unparse_user_workout(message.text):
        try:
            ans = await create_user_workout(session, exercises_data, telegram_id=message.from_user.id)
        except WrongDayName as ex:
            await message.answer(text=f"{ex}\nTry one more time")
            return

        except Exception as ex:
            try:
                await message.answer(text=f'Your input are incorrect\ndebug info:{ex}')
            except Exception:
                with open(f'../logs/{datetime.datetime.now()}') as f:
                    f.write(ex)
            finally:
                return
    await message.answer(
        text='<i>Your workout successfully added!</i>\nYou can view your periodization on buttons down',
        reply_markup=K.create_reply_kb(['View today workout'])
    )
    await state.set_state(FSMDefaultContext.view_workout)


@router.message(StateFilter(FSMDefaultContext.view_workout))
async def view_user_periodization_workout(message: Message, session: AsyncSession):
    pass
