import openai

import config
from .enums import GPTModel


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

    async def request(self, message_list: list[dict[str, str]]) -> str:
        response = await self._client.chat.completions.create(
            messages=message_list,
            model=self._model,
        )
        return response.choices[0].message.content
