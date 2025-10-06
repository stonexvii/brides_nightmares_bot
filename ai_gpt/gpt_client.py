import openai
import json

import config
from classes.enums import ResourcesPath
from classes.file_manager import FileManager
from .enums import GPTRole, GPTModel


class GPTMessage:

    def __init__(self, message_list: list[dict[str, str]] | None = None):
        self.message_list = self._init_message() if message_list is None else message_list

    @staticmethod
    def _init_message() -> list[dict[str, str]]:
        message = {
            'role': GPTRole.SYSTEM.value,
            'content': FileManager.read_txt(ResourcesPath.AI_PROMPTS_PATH.value, ResourcesPath.AI_MODERATOR.value),
        }
        return [message]

    def update(self, role: GPTRole, message: str):
        message = {
            'role': role.value,
            'content': message,
        }
        self.message_list.append(message)

    def to_json(self):
        return json.dumps(self.message_list, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        print(data)
        return data


class ChatGPT:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model: GPTModel = GPTModel.GPT_4_TURBO):
        self._gpt_token = config.OPENAI_TOKEN
        self._proxy = config.PROXY
        self._client = self._create_client()
        self._model = model.value

    def _create_client(self):
        gpt_client = openai.AsyncOpenAI(
            api_key=self._gpt_token,
            base_url=self._proxy,
        )
        return gpt_client

    async def request(self, ai_role: GPTRole, user_request: str, message_list: GPTMessage | None = None) -> str:
        message_list = GPTMessage() if message_list is None else message_list
        message_list.update(ai_role, user_request)
        response = await self._client.chat.completions.create(
            messages=message_list.message_list,
            model=self._model,
        )
        ai_response = response.choices[0].message.content
        message_list.update(GPTRole.CHAT, ai_response)
        return ai_response

    # async def voice_transcribe(self, voice, model: str = 'whisper-1'):
    #     msg_text = await self._client.audio.transcriptions.create(
    #         model=model,
    #         file=voice,
    #     )
    #     print(msg_text)
