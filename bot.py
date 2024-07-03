import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from sqlalchemy import select

import handlers
from config import config
from database.base import init_models, get_session, async_session
from database.models import Workout
from middleware.database_connection import DBMiddleware
from services.scheduler import change_week_scheduler

# main file of bot

token = config.tg_bot.token

# logger initializing
logger = logging.getLogger(__name__)


# configuration and turn on bot
async def main():
    # configurate logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=token, default=DefaultBotProperties(parse_mode='HTML'))

    dp: Dispatcher = Dispatcher()
    dp.include_router(handlers.router_main)
    dp.update.middleware(DBMiddleware())

    await change_week_scheduler()

    # set main menu
    # await set_main_menu(bot)
    await init_models()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
