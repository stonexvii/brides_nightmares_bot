import json

from aiogram import Bot
from aiogram.fsm.context import FSMContext

import config
from classes.enums import ResourcesPath
from classes.file_manager import FileManager
from keyboards.inline_keyboards import ikb_moderator_rework
from .ai_client import ChatGPT
from .enums import GPTRole


class AIDialog:
    ADMIN_ID = config.ADMIN_ID
    CHANNEL_ID = config.CHANNEL_ID

    def __init__(self, user_tg_id: int):
        self.user_id = user_tg_id
        self.message_list = self._init_message()

    @staticmethod
    def _init_message() -> list[dict[str, str]]:
        message = {
            'role': GPTRole.SYSTEM.value,
            'content': FileManager.read_txt(ResourcesPath.AI_PROMPTS_PATH.value, ResourcesPath.AI_MODERATOR.value),
        }
        return [message]

    async def send_message(self, message: str):
        self.update(GPTRole.USER, message)
        response = await ChatGPT().request(self.message_list)
        json_data = json.loads(response)
        self.update(GPTRole.CHAT, response)
        return json_data

    def update(self, role: GPTRole, message: str):
        message = {
            'role': role.value,
            'content': message,
        }
        self.message_list.append(message)

    async def answer(self, bot: Bot, state: FSMContext, response: dict[str, str]):
        if response['status'] == 'CORRECT':
            await bot.send_message(
                chat_id=self.CHANNEL_ID,
                text=response['content'],
            )
            await bot.send_message(
                chat_id=self.user_id,
                text=response['comment'],
            )
            await state.clear()
        elif response['status'] == 'INCORRECT_CAN':
            await bot.send_message(
                chat_id=self.user_id,
                text=response['comment'],
                reply_markup=ikb_moderator_rework(),
            )
        elif response['status'] == 'INCORRECT_NO':
            await bot.send_message(
                chat_id=self.user_id,
                text=response['comment'],
            )
        elif response['status'] == 'INFO':
            await bot.send_message(
                chat_id=self.user_id,
                text=response['comment'],
            )
        elif response['status'] == 'ADMIN':
            await bot.send_message(
                chat_id=self.ADMIN_ID,
                text=response['comment'] + '\n\n' + response['content'],
            )
            await state.clear()

    def to_json(self):
        return json.dumps(self.message_list, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return data
