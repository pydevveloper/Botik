from aiogram import Router
from aiogram.types import Message

from config import bot

trash_router = Router()

@trash_router.message()
async def last_stand(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Я не знаю эту команду!"
    )