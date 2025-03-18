from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

buttons1 = {
    "regestration": "Регестрация®"
}

def rg_kb():
    rk_builder = ReplyKeyboardBuilder()

    button = KeyboardButton(text = buttons1["regestration"])
    rk_builder.add(button)

    return rk_builder.as_markup(resize_keyboard=True, is_persistent=True)