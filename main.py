from aiogram import Bot, Dispatcher

import asyncio

from handlers import main_router
import config
import misc


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
