from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, URLInputFile, FSInputFile

from config import bot
from src.keyboards.user_keyboard import botik_keyboard, buttons

user_router = Router()


@user_router.message(CommandStart())
async def command_start(message: Message):
    await bot.send_message(
        chat_id=5467907359,
        text="Не издевайся над моим ботом!"
    )

    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=URLInputFile("https://a.d-cd.net/44WavBDpaCxUcIZcigmwW6YIMTM-1920.jpg"),
        caption="Привет! Это мой фан-бот. Крч у тя внизу кнопки потыкай и разберись сам.",
        has_spoiler=False,
        reply_markup=botik_keyboard()
    )

@user_router.message(F.text == buttons["photo"])
async def three_stand(message: Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=URLInputFile(
            "https://i.ytimg.com/vi/OsFQakVNkkc/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgXihOMA8=&amp;rs=AOn4CLDpc_ePYz5GWJfI0tijAffHP0F-ng"),
        caption=("Хотел пикчу? ДЕРЖИ!")
    )

@user_router.message(F.text == buttons["memas"])
async def five_stand(message: Message):
    await bot.send_photo(
        chat_id= message.from_user.id,
        photo=URLInputFile(
            "https://sun9-69.userapi.com/impf/c305110/v305110120/6b0/PwawWP94k3o.jpg?size=538x448&quality=96&sign=437beb13bf20e3b3c6e5d0968de92804&type=album"),
        caption=("Получи мемасик")
    )

@user_router.message(F.text == buttons["video"])
async def six_stand(message: Message):
    await bot.send_video(
        chat_id=message.from_user.id,
        video=FSInputFile("sad/raketka.mp4"),
        caption="Ваяяя Ракетка шальнаяяя"
    )

@user_router.message(F.text == buttons["help"])
async def seven_stand(message: Message):
    await bot.send_message(
        chat_id= message.from_user.id,
        text="Привет! меня зовут Андрей, я из Омска и пишу этого бота для изучения питона и aiogram, спасибо что зашёл!"
    )

@user_router.message()
async def re_last_stand(message: Message):
    await bot.send_message(
        chat_id=5467907359,
        text="Я ЗАПРЕЩАЮ ВАМ ПИСАТЬ ТО, ЧТО БОТ НЕ УМЕЕТ ВЫПОЛНЯТЬ, И ОСКОРБЛЯТЬ ТОЖЕ НЕЛЬЗЯ!!!!!!"
    )

@user_router.message()
async def last_stand(message: Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Я не знаю эту команду!"
    )
