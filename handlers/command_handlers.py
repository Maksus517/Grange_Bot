from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon import LEXICON_RU
from keyboards import info_keyboard, support_keyboard, developers_keyboard
from data import users_data, DataBase

router_ch: Router = Router()


@router_ch.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in users_data:
        users_data[message.from_user.id] = {'user_name': message.from_user.first_name,
                                            'user_status': None, 'user_premium': False}
        data_base: DataBase = DataBase(message)
        data_base.insert_user_data()
    await message.answer(text=f"<b>Привет, {message.from_user.first_name}! "
                              f"Я многофункциональный бот.</b>\n\n"
                              f"Можете просто написать мне или воспользоваться:\n\n"
                              f"{LEXICON_RU['/start']}")


@router_ch.message(Command(commands=['help']))
async def process_help_command(message: Message):
    if message.from_user.id in users_data:
        await message.answer(text=LEXICON_RU['/help'])
    else:
        await message.answer(text='Отправьте команду /start')


@router_ch.message(Command(commands=['info_resources']))
async def process_info_command(message: Message):
    if message.from_user.id in users_data:
        await message.answer(text=LEXICON_RU['/info_resources'], reply_markup=info_keyboard)
    else:
        await message.answer(text='Отправьте команду /start')


@router_ch.message(Command(commands=['assist_user']))
async def process_support_command(message: Message):
    if message.from_user.id in users_data:
        await message.answer(text=LEXICON_RU['/assist_user'], reply_markup=support_keyboard)
    else:
        await message.answer(text='Отправьте команду /start')


@router_ch.message(Command(commands=['developers']))
async def process_developers_command(message: Message):
    if message.from_user.id in users_data:
        await message.answer(text=LEXICON_RU['/developers'], reply_markup=developers_keyboard)
    else:
        await message.answer(text='Отправьте команду /start')
