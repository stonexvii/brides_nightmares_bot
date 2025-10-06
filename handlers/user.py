import asyncio
import random

from aiogram import Router, Bot, F
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from datetime import datetime

import config
from ai_gpt import ai_client
from ai_gpt.gpt_client import GPTMessage
from ai_gpt.enums import GPTRole

user_router = Router()


@user_router.message(F.text)
async def text_messages(message: Message, bot: Bot, state: FSMContext):
    await bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    message_list = GPTMessage()
    response = await ai_client.request(GPTRole.USER, message.text, message_list)
    if response.startswith('Correct') or response.startswith('Incorrect'):
        print(response)
        result, response = response.split(':\n', 1)
        await state.update_data(
            {
                'messages': message_list,
                'attempts': 1,
                'last_message': datetime.now(),
            },
        )
        print(message_list)
        if result == 'Correct':
            await asyncio.sleep(random.randint(5, 10))
            await bot.send_message(
                chat_id=config.CHANNEL_ID,
                text=message.text,
            )
            await state.clear()
    await message.answer(
        text=response.strip(),
    )
