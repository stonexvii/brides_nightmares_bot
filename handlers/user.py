from aiogram import Router, Bot, F
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from ai_model.ai_dialog import AIDialog
from fsm.states import UserDialog

user_router = Router()


@user_router.message(F.text)
async def text_messages(message: Message, bot: Bot, state: FSMContext):
    await bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    ai_dialog = AIDialog(message.from_user.id)
    json_response = await ai_dialog.send_message(message.text)
    await state.set_state(UserDialog.input_data)
    await state.update_data(
        {
            'dialog': ai_dialog,
        }
    )
    await ai_dialog.answer(bot, state, json_response)
