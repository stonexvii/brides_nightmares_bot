from aiogram.fsm.state import State, StatesGroup


class UserDialog(StatesGroup):
    input_data = State()
    timer = State()
