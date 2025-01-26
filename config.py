from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings



class EnvSettings(BaseSettings):
    """
    Environment settings.
    """

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


class BotSettings(EnvSettings):
    token: str


bot_settings = BotSettings()
default = DefaultBotProperties(parse_mode='HTML', protect_content=False)
bot = Bot(token = bot_settings.token, default=default)
dp = Dispatcher()