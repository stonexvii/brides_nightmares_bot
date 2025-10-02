from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command

import config
from keyboards.inline_keyboards import ikb_moderator_menu
from text import bot_messages

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message):
    await message.answer(
        text=bot_messages.START,
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



