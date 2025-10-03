import openai
import httpx

import os

import config
from .enums import AIRole, GPTRole, GPTModel

from classes.file_manager import FileManager
from classes.resources_paths import AI_PROMPTS_PATH


# from .enums import GPTRole, Extensions
# from .resource import ResourcePath


class GPTMessage:

    def __init__(self, prompt: str):
        self._prompt_name = prompt
        self.message_list = self._init_message()

    def _init_message(self) -> list[dict[str, str]]:
        message = {
            'role': GPTRole.SYSTEM.value,
            'content': self._load_prompt(),
        }
        return [message]

    def _load_prompt(self) -> str:
        prompt_path = os.path.join(AI_PROMPTS_PATH, self._prompt_name)
        prompt = FileManager.read_txt(prompt_path)
        return prompt

    def update(self, role: GPTRole, message: str):
        message = {
            'role': role.value,
            'content': message,
        }
        self.message_list.append(message)


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

    async def request(self, ai_role: AIRole, user_request) -> str:
        message_list = GPTMessage(ai_role.value)
        message_list.update(GPTRole.USER, user_request)
        response = await self._client.chat.completions.create(
            messages=message_list.message_list,
            model=self._model,
        )
        return response.choices[0].message.content

    async def voice_transcribe(self, voice, model: str = 'whisper-1'):
        msg_text = await self._client.audio.transcriptions.create(
            model=model,
            file=voice,
        )
        print(msg_text)
