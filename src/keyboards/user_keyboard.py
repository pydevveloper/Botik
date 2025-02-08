from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

buttons = {"photo": "📷пикча",
           "video": "🎥видосик",
           "memas": "🎃мемчик",
           "help": "О создателе🔰",
           "korea": "Просто красная кнопка⭕",
            "hinx": "Доп. Информация✔"
           }

def botik_keyboard():
    kb_builder = ReplyKeyboardBuilder()

    button = KeyboardButton(text=buttons["photo"])
    kb_builder.add(button)

    button = KeyboardButton(text=buttons["video"])
    kb_builder.add(button)
    
    button = KeyboardButton(text=buttons["memas"])
    kb_builder.row(button)
    
    button = KeyboardButton(text=buttons["help"])
    kb_builder.add(button)

    button = KeyboardButton(text=buttons["korea"])
    kb_builder.row(button)

    return kb_builder.as_markup(resize_keyboard=True, is_persistent=True)

def inline_keyboard():
    inb_builder = InlineKeyboardBuilder()

    button = InlineKeyboardButton(text=buttons["hinx"], url="https://sun9-69.userapi.com/impf/c305110/v305110120/6b0/PwawWP94k3o.jpg?size=538x448&quality=96&sign=437beb13bf20e3b3c6e5d0968de92804&type=album")
    inb_builder.add(button)
    return inb_builder.as_markup(resize_keyboard=True, is_persistent=True)