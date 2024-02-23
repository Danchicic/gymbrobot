from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    """
    func to set a menu in telegram
    handlers to process commands: main_handlers
    :param bot:
    :return:
    """
    main_menu_commands = [
        BotCommand(command='start', description='start'),

    ]
    await bot.set_my_commands(main_menu_commands)
