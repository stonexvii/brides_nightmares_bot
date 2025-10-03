import asyncio

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from openai import OpenAI
from datetime import datetime
import io
import config
from fsm.states import CallbackState
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
    destination_path = f"voice.ogg"
    file_obj = io.BytesIO()
    file = await bot.download_file(file_path, file_obj)
    client = OpenAI()
    # msg_text = client.audio.transcriptions.create(
    #     a
    #     model='gpt-4o-transcribe',
    #     file=file_obj,
    # )
    # print('SLEEP')
    # await asyncio.sleep(5)
    # print('WAKE UP')
    # model = whisper.load_model("base")
    # result = model.transcribe('voice.ogg')

    # The transcribed text is available in the 'text' key of the result dictionary
    await message.answer(msg_text.text)
    # await bot.send_message(
    #     chat_id=config.MODERATOR_ID,
    #     text=message.text,
    #     entities=message.entities,
    #     reply_markup=ikb_moderator_menu(message.from_user.id),
    # )
    # await state.set_state(CallbackState.timer)
    # await state.set_data(
    #     {
    #         'message_time': datetime.now(),
    #     },
    # )


@user_router.message(F.text)
async def text_messages(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(
        chat_id=config.MODERATOR_ID,
        text=message.text,
        entities=message.entities,
        reply_markup=ikb_moderator_menu(message.from_user.id),
    )
    # await state.set_state(CallbackState.timer)
    # await state.set_data(
    #     {
    #         'message_time': datetime.now(),
    #     },
    # )
