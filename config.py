import dotenv
import os

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
MODERATOR_ID = int(os.getenv('MODERATOR_ID'))
# MODERATOR_ID=1954334266
ANTI_SPAM_MINUTES = 5
