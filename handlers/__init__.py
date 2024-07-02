from aiogram import Router

from .commands_handler import command_router
from . import workout_handler

# union routers
router_main: Router = Router()
router_main.include_router(command_router)
router_main.include_router(workout_handler.router)
