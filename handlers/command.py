from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command

from ai_gpt import ai_client
from ai_gpt.enums import AIRole
import config
from keyboards.inline_keyboards import ikb_moderator_menu
from text import bot_messages

command_router = Router()


# @command_router.channel_post()
# async def channel_post_catch(message: Message):
#     for key, item in dict(message).items():
#         if item:
#             print(key, item)


@command_router.message(Command('start'))
async def command_start(message: Message):
    welcome_message = await ai_client.request(AIRole.WELCOME, f'Привет, меня зовут {message.from_user.full_name}')
    await message.answer(
        text=welcome_message,
    )


@command_router.message(Command('rules'))
async def command_start(message: Message):
    await message.answer(
        text=bot_messages.RULES,
    )


@command_router.message(Command('help'))
async def command_start(message: Message):
    await message.answer(
        text=bot_messages.HELP,
    )
