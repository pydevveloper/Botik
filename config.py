import os

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings
from supabase import create_client, Client


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
    supabase_url: str
    supabase_key: str


bot_settings = BotSettings()
supabase: Client = create_client(bot_settings.supabase_url, bot_settings.supabase_key)
default = DefaultBotProperties(parse_mode='HTML', protect_content=False)
bot = Bot(token = bot_settings.token, default=default)
dp = Dispatcher()

