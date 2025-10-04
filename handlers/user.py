import asyncio
import random

from aiogram import Router, Bot, F
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import config
from ai_gpt import ai_client
from ai_gpt.enums import AIRole

user_router = Router()


@user_router.message(F.text)
async def text_messages(message: Message, bot: Bot, state: FSMContext):
    await bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING,
    )
    response = await ai_client.request(AIRole.MODERATOR, message.text)
    verdict, content = response.split('\n', 1)

    await message.answer(
        text=content.strip(),
    )
    if verdict == 'Correct':
        await asyncio.sleep(random.randint(5, 10))
        await bot.send_message(
            chat_id=config.CHANNEL_ID,
            text=message.text,
        )
