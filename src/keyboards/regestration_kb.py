from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

buttons1 = {
    "regestration": "Регестрация®",
    "contact": "Отправить контакт"
}

def rg_kb():
    rk_builder = ReplyKeyboardBuilder()

    button1 = KeyboardButton(text= buttons1["contact"], request_contact=True)
    rk_builder.add(button1)

    return rk_builder.as_markup(resize_keyboard=True, is_persistent=True)
