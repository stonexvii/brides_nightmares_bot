from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

import config
from classes.enums import ResourcesPath
from classes.file_manager import FileManager
from middleware.admin import AdminMiddleware
from text.moderator_text import Minutes

admin_router = Router()
admin_router.message.middleware(AdminMiddleware())


@admin_router.message(Command('help'))
async def admin_help(message: Message):
    await message.answer(
        text=f'/set_time\n/set_message\n/set_prompt'
    )


@admin_router.message(Command('set_time'))
async def set_antispam_time(message: Message, command: CommandObject):
    msg_text = 'Для команды set_time аргумент - целое число'
    if command.args and command.args.isdigit():
        config.ANTI_SPAM_MINUTES = int(command.args)
        msg_text = f'Антиспам установлен на {Minutes.as_str(int(command.args))}'
    await message.answer(
        text=msg_text,
    )


@admin_router.message(Command('set_message'))
async def set_txt_files(message: Message, command: CommandObject):
    files = [
        ResourcesPath.BOT_START.value,
        ResourcesPath.BOT_RULES.value,
        ResourcesPath.BOT_HELP.value,
    ]
    msg_txt = 'Возможные аргументы для set_message:\n' + '\n'.join(files)
    if command.args:
        filename, content = command.args.split('\n', 1)
        if filename in files:
            FileManager.write_txt(ResourcesPath.TEXT_MESSAGES.value, filename, data=content)
            msg_txt = f'{filename} обновлен!'
    await message.answer(
        text=msg_txt,
    )


@admin_router.message(Command('set_prompt'))
async def set_prompt(message: Message, command: CommandObject):
    files = [
        ResourcesPath.AI_WELCOME.value,
        ResourcesPath.AI_MODERATOR.value,
    ]
    msg_txt = 'Возможные аргументы для set_prompt:\n' + '\n'.join(files)
    if command.args:
        filename, content = command.args.split('\n', 1)
        if filename in files:
            FileManager.write_txt(ResourcesPath.AI_PROMPTS_PATH.value, filename, data=content)
            msg_txt = f'Промпт {filename} обновлен!'
    await message.answer(
        text=msg_txt,
    )
