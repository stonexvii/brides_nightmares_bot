import os

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from classes.enums import ResourcesPath
from classes.file_manager import FileManager

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message):
    await message.answer(
        text=FileManager.read_txt(os.path.join(ResourcesPath.TEXT_MESSAGES.value, 'bot_start')),
    )


@command_router.message(Command('rules'))
async def command_start(message: Message):
    await message.answer(
        text=FileManager.read_txt(os.path.join(ResourcesPath.TEXT_MESSAGES.value, 'bot_rules')),
    )


@command_router.message(Command('help'))
async def command_start(message: Message):
    await message.answer(
        text=FileManager.read_txt(os.path.join(ResourcesPath.TEXT_MESSAGES.value, 'bot_help')),
    )
