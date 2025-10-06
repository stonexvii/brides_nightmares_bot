import json

import config
from .ai_client import ChatGPT
from classes.enums import ResourcesPath
from classes.file_manager import FileManager
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
        self.update(GPTRole.CHAT, json_data)
        return json_data

    def update(self, role: GPTRole, message: str):
        message = {
            'role': role.value,
            'content': message,
        }
        self.message_list.append(message)

    def analyze_response(self, response: dict[str, str]):
        if response['status'] == 'CORRECT':
            result = {
                'chat_id': self.CHANNEL_ID,
                'text': response['content']
            }

    def to_json(self):
        return json.dumps(self.message_list, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return data
