from aiogram.utils.keyboard import InlineKeyboardBuilder

from classes.inline_button import Button
from text.moderator_text import BUTTONS_TEXT


def ikb_moderator_menu(user_tg_id: int):
    keyboard = InlineKeyboardBuilder()
    buttons = [Button(text, callback, user_tg_id) for callback, text in BUTTONS_TEXT.items()]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=button.callback,
        )
    keyboard.adjust(1)
    return keyboard.as_markup()
