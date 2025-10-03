import io
import os
import asyncio
import random

from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.enums import ChatAction

import config
from ai_gpt import ai_client
from ai_gpt.enums import AIRole
from keyboards.inline_keyboards import ikb_moderator_menu

user_router = Router()


@user_router.message(F.voice)
async def voice_messages(message: Message, bot: Bot, state: FSMContext):
    print('CATCH')
    for key, item in dict(message).items():
        if item:
            print(key, item)
    file_info = await bot.get_file(message.voice.file_id)
    file_path = file_info.file_path
    file_obj = io.BytesIO()
    voice_mp3 = f'voice_files/voice-{message.voice.file_unique_id}.ogg'
    await bot.download_file(file_path, voice_mp3)
    # result = await chat_gpt.voice_transcribe(file_obj)
    # print(result)

    # await state.set_state(CallbackState.timer)
    # await state.set_data(
    #     {
    #         'message_time': datetime.now(),
    #     },
    # )


@user_router.message(F.text)
async def text_messages(message: Message, bot: Bot, state: FSMContext):
    # await bot.send_message(
    #     chat_id=config.MODERATOR_ID,
    #     text=message.text,
    #     entities=message.entities,
    #     reply_markup=ikb_moderator_menu(message.from_user.id),
    # )
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
    # await state.set_state(CallbackState.timer)
    # await state.set_data(
    #     {
    #         'message_time': datetime.now(),
    #     },
    # )
