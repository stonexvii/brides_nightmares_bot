from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import config
from fsm.states import UserDialog
from keyboards.callback_data import ModeratorCallback
from text.moderator_text import ModeratorText

callback_router = Router()


@callback_router.callback_query(ModeratorCallback.filter(F.button == 'other'))
async def other_choice(callback: CallbackQuery, callback_data: ModeratorCallback, bot: Bot, state: FSMContext):
    await state.set_state(UserDialog.input_data)
    await state.set_data(
        {
            'user_tg_id': callback_data.user_tg_id,
            'message_id': callback.message.message_id,
            'user_text': callback.message.text,
        },
    )
    await callback.answer(
        text=ModeratorText.OTHER,
        show_alert=True,
    )


@callback_router.callback_query(ModeratorCallback.filter())
async def moderator_check(callback: CallbackQuery, callback_data: ModeratorCallback, bot: Bot):
    if callback_data.button == 'post':
        await bot.send_message(
            chat_id=config.CHANNEL_ID,
            text=callback.message.text,
            entities=callback.message.entities,
        )
        msg_text = ModeratorText.SUCCESS
    else:
        await bot.send_message(
            chat_id=callback_data.user_tg_id,
            text=ModeratorText.as_text(callback_data.button, callback.message.text),
            entities=callback.message.entities,
        )
        msg_text = ModeratorText.FAILURE
    await callback.answer(
        text=msg_text,
        show_alert=True,
    )
    await bot.delete_message(
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
    )
