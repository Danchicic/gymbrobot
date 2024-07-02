from aiogram.filters.state import State, StatesGroup


class FSMDefaultContext(StatesGroup):
    get_workout = State()
    view_workout = State()
