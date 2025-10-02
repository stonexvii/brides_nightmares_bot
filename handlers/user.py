from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from datetime import datetime

import config
from fsm.states import CallbackState
from keyboards.inline_keyboards import ikb_moderator_menu

user_router = Router()


@user_router.message(F.text)
async def all_messages(message: Message, bot: Bot, state: FSMContext):
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
