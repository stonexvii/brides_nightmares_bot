import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from classes.file_manager import FileManager
from classes.resources_paths import TEXT_MESSAGES

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message):
    await message.answer(
        text=FileManager.read_txt(os.path.join(TEXT_MESSAGES, 'bot_start')),
    )


@command_router.message(Command('rules'))
async def command_start(message: Message):
    await message.answer(
        text=FileManager.read_txt(os.path.join(TEXT_MESSAGES, 'bot_rules')),
    )


@command_router.message(Command('help'))
async def command_start(message: Message):
    await message.answer(
        text=FileManager.read_txt(os.path.join(TEXT_MESSAGES, 'bot_help')),
    )
