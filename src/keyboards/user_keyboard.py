from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

buttons = {"photo": "📷пикча",
           "video": "🎥видосик",
           "memas": "🎃мемчик",
           "help": "О создателе"
           
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
    return kb_builder.as_markup(resize_keyboard=True, is_persistent=True)