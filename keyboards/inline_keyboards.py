from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_data import ModeratorCallback


def ikb_moderator_rework():
    keyboard = InlineKeyboardBuilder()
    buttons = [
        ('Исправить и отправить', ModeratorCallback(
            button='accept',
        ),
         ),
        ('Отмена', ModeratorCallback(
            button='cancel',
        ),
         ),
    ]
    for button in buttons:
        keyboard.button(
            text=button[0],
            callback_data=button[1],
        )
    keyboard.adjust(1)
    return keyboard.as_markup()
