import asyncio

from aiogram import Bot, Dispatcher

import config
import misc
from handlers import main_router


async def start_bot():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(misc.start_up)
    dp.shutdown.register(misc.shutdown)
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
