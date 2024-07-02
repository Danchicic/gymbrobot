from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.exc import IntegrityError

from sqlalchemy.ext.asyncio import AsyncSession

from lexicon import COMMAND_LEXICON
from FSM.BaseContext import FSMDefaultContext
from database.services import database_users

command_router: Router = Router()


# commands router file

@command_router.message(CommandStart())
async def hello_world(message: Message, state: FSMContext, session: AsyncSession):
    await state.set_state(FSMDefaultContext.get_workout)
    try:
        await database_users.insert_user_by_telegram_id(session, message.from_user.id)
    except IntegrityError as ex:
        await message.answer(text='You already registered user')
    await message.reply(text=COMMAND_LEXICON['start'])
