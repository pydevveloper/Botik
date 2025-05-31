import asyncio
import logging
import sys

from config import dp, bot
from src.middlewares.test_middleware import TestMiddleware
from src.routers.last_stand import trash_router
from src.routers.user_router_file import user_router

async def start():
    user_router.message.middleware(TestMiddleware())
    dp.include_routers(user_router)
    user_router.include_router(trash_router)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())
