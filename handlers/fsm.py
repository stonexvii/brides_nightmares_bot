from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ai_model.ai_dialog import AIDialog
from fsm.states import UserDialog

fsm_router = Router()


@fsm_router.message(UserDialog.input_data)
async def user_dialog(message: Message, bot: Bot, state: FSMContext):
    ai_dialog: AIDialog = await state.get_value('dialog')
    json_response = await ai_dialog.send_message(message.text)
    await ai_dialog.answer(bot, state, json_response)
    await state.update_data(
        {
            'ai_dialog': ai_dialog,
        },
    )
