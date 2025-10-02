from aiogram.utils.keyboard import InlineKeyboardBuilder

from collections import namedtuple

from .callback_data import ModeratorCallback
from classes.inline_button import Button
from text.moderator_text import BUTTONS_TEXT


# Button = namedtuple('Button', ['text', 'callback'])


def ikb_moderator_menu(user_tg_id: int):
    keyboard = InlineKeyboardBuilder()
    buttons = [Button(text, callback, user_tg_id) for callback, text in BUTTONS_TEXT.items()]
    # buttons = [
    #     Button('Личные данные', ModeratorCallback(
    #         button='personal',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    #     Button('Нецензурные выражения', ModeratorCallback(
    #         button='explicit',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    #     Button('Политика', ModeratorCallback(
    #         button='politics',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    #     Button('Религия', ModeratorCallback(
    #         button='religion',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    #     Button('Уголовка', ModeratorCallback(
    #         button='criminal_themes',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    #     Button('Прочее', ModeratorCallback(
    #         button='other',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    #     Button('Опубликовать!', ModeratorCallback(
    #         button='post',
    #         user_tg_id=user_tg_id,
    #     ),
    #            ),
    # ]
    for button in buttons:
        keyboard.button(
            text=button.text,
            callback_data=button.callback,
        )
    keyboard.adjust(1)
    return keyboard.as_markup()
