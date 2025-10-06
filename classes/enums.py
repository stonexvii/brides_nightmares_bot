from enum import Enum


class ResourcesPath(Enum):
    AI_PROMPTS_PATH = 'ai_gpt/prompts'
    TEXT_MESSAGES = 'text'
    AI_MODERATOR = 'ai_moderator'
    AI_WELCOME = 'ai_welcome'
    BOT_START = 'bot_start'
    BOT_RULES = 'bot_rules'
    BOT_HELP = 'bot_help'
