from aiofiles.os import remove
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, URLInputFile, FSInputFile, CallbackQuery, ReplyKeyboardRemove

from config import bot
from src.keyboards.regestration_kb import rg_kb, buttons1
from src.keyboards.user_keyboard import botik_keyboard, buttons, inline_keyboard
from src.states.user_states import User

user_router = Router()

@user_router.message(CommandStart())
async def command_start(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Пожалуйста зарегестрируйтесь",
        reply_markup=rg_kb()
    )

@user_router.message(F.text == buttons1["regestration"])
async def two_stand(message: Message, state: FSMContext):
    await state.set_state(
        User.wait_name
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Введите Имя:",
        reply_markup=ReplyKeyboardRemove()
    )

@user_router.message(User.wait_name)
async def twotwo_stand(message: Message, state: FSMContext):
    name=message.text
    await state.update_data(name_key=name)
    await state.set_state(
        User.menu
    )

    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAIFdGem9Ix-nCdmvQG6glrtEf3wH3nfAAIFAAPANk8T-WpfmoJrTXU2BA'
    )

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=URLInputFile("https://a.d-cd.net/44WavBDpaCxUcIZcigmwW6YIMTM-1920.jpg"),
        caption=f"Привет, {name}! Это мой фан-бот. Крч у тя внизу кнопки потыкай и разберись сам.",
        has_spoiler=False,
        reply_markup=botik_keyboard()
    )

@user_router.message(F.text == buttons["photo"], User.menu)
async def three_stand(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=URLInputFile(
            "https://i.ytimg.com/vi/OsFQakVNkkc/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgXihOMA8=&amp;rs=AOn4CLDpc_ePYz5GWJfI0tijAffHP0F-ng"),
        caption=("Хотел пикчу? ДЕРЖИ!")
    )

@user_router.message(F.text == buttons["memas"], User.menu)
async def five_stand(message: Message, state: FSMContext):
    name=await state.get_value("name_key")
    data=await state.get_data()
    print(data["name_key"])
    await bot.send_photo(
        chat_id= message.from_user.id,
        photo=URLInputFile(
            "https://sun9-69.userapi.com/impf/c305110/v305110120/6b0/PwawWP94k3o.jpg?size=538x448&quality=96&sign=437beb13bf20e3b3c6e5d0968de92804&type=album"),
        caption=(f"Получи мемасик, {name}"),
        reply_markup=inline_keyboard()
    )

@user_router.message(F.text == buttons["video"], User.menu)
async def six_stand(message: Message):
    await bot.send_video(
        chat_id=message.from_user.id,
        video=FSInputFile("sad/raketka.mp4"),
        caption="Ваяяя Ракетка шальнаяяя"
    )

@user_router.message(F.text == buttons["help"], User.menu)
async def seven_stand(message: Message):
    await bot.send_message(
        chat_id= message.from_user.id,
        text="Привет! меня зовут Андрей, я из Омска и пишу этого бота для изучения питона и aiogram, спасибо что зашёл!"
    )

@user_router.message(F.text == buttons["korea"], User.menu)
async def korea_mem(message: Message):
    await bot.send_audio(
        chat_id=message.from_user.id,
        audio=FSInputFile("ne_rikrol/rkbb.mp3")
    )
