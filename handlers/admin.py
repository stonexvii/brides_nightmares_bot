from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

import config
from middleware.admin import AdminMiddleware
from text.moderator_text import Minutes

admin_router = Router()
admin_router.message.middleware(AdminMiddleware())


@admin_router.message(Command('spam'))
async def command_spam(message: Message, command: CommandObject):
    if command.args and command.args.isdigit():
        config.ANTI_SPAM_MINUTES = int(command.args)
        await message.answer(
            text=f'Антиспам установлен на {Minutes.as_str(int(command.args))}',
        )
