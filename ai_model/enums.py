from enum import Enum


class GPTRole(Enum):
    USER = 'user'
    CHAT = 'assistant'
    SYSTEM = 'system'


class AIRole(Enum):
    WELCOME = 'ai_welcome'
    MODERATOR = 'ai_moderator'


class GPTModel(Enum):
    GPT_3_TURBO = 'gpt-3.5-turbo'
    GPT_4_TURBO = 'gpt-4-turbo'
