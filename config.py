import dotenv
import os

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')
PROXY = os.getenv('PROXY')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
MODERATOR_ID = int(os.getenv('MODERATOR_ID'))
ANTI_SPAM_MINUTES = 5
ANTI_SPAM_ATTEMPTS = 5
