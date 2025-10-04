from aiogram.filters.callback_data import CallbackData


class ModeratorCallback(CallbackData, prefix='MC'):
    button: str
    user_tg_id: int = 0
