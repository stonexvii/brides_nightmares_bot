from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from datetime import datetime, timedelta

import config
from fsm.states import CallbackState
from keyboards.inline_keyboards import ikb_moderator_menu
from text.moderator_text import ModeratorText

fsm_router = Router()


@fsm_router.message(CallbackState.timer)
async def check_spam(message: Message, bot: Bot, state: FSMContext):
    current_time = datetime.now()
    message_time = await state.get_value('message_time')
    elapsed_time = current_time - message_time
    if elapsed_time < timedelta(minutes=config.ANTI_SPAM_MINUTES):
        await message.answer(
            text=ModeratorText.elapsed_time(elapsed_time),
        )
    else:
        await bot.send_message(
            chat_id=config.MODERATOR_ID,
            text=message.text,
            entities=message.entities,
            reply_markup=ikb_moderator_menu(message.from_user.id),
        )
        await state.set_state(CallbackState.timer)
        await state.set_data(
            {
                'message_time': datetime.now(),
            },
        )


@fsm_router.message(CallbackState.input_data)
async def other_reason(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(
        chat_id=data['user_tg_id'],
        text=ModeratorText.as_text(message.text, data['user_text']),
    )
    for message_id in (data['message_id'], message.message_id):
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message_id,
        )
    await state.clear()
