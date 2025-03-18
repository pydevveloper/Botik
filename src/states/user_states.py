from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    wait_name = State()
    wait_surname = State()
    menu = State()
    phone_number = State()