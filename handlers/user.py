import asyncio
import random

from aiogram import Router, Bot, F
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from datetime import datetime

import config
from fsm.states import UserDialog
# from ai_model import ai_client
from ai_model.ai_dialog import AIDialog
from ai_model.enums import GPTRole

user_router = Router()


@user_router.message(F.text)
async def text_messages(message: Message, bot: Bot, state: FSMContext):
    await bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    ai_dialog = AIDialog(message.from_user.id)
    await ai_dialog.send_message(message.text)
    await state.set_state(UserDialog.input_data)
    await state.update_data(
        {
            'dialog': ai_dialog,
        }
    )
    # message_list = GPTMessage()
    # response = await ai_client.request(GPTRole.USER, message.text, message_list)
    # message_list.update(GPTRole.CHAT, response)
    #
    # if response.startswith('Correct') or response.startswith('Incorrect'):
    #     result, response = response.split(':', 1)
    #     await state.set_state(UserDialog.input_data)
    #     await state.update_data(
    #         {
    #             'user_tg_id': message.from_user.id,
    #             'message_list': message_list,
    #             'attempts': 1,
    #             'last_message': datetime.now(),
    #         },
    #     )
    #     if result == 'Correct':
    #         # await asyncio.sleep(random.randint(5, 10))
    #         await bot.send_message(
    #             chat_id=config.CHANNEL_ID,
    #             text=message.text,
    #         )
    #         await state.clear()
    # await message.answer(
    #     text=response.strip().capitalize(),
    # )
