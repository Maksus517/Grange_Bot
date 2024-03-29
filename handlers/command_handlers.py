from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile

from lexicon import LEXICON_RU
from keyboards import info_keyboard, support_keyboard, assist_user_keyboard, game_genre_keyboard
from data import users_data, DataBase


router_ch: Router = Router()


@router_ch.message(CommandStart())
async def process_start_command(message: Message) -> None:
    if message.from_user.id not in users_data:
        users_data[message.from_user.id] = {'user_name': message.from_user.first_name,
                                            'user_status': 'chat',
                                            'counter': 0,
                                            'message_data': None,
                                            'data_list': [],
                                            'game_data': {}}
        data_base: DataBase = DataBase(message)
        await data_base.insert_user_data()
    users_data[message.from_user.id]['user_status'] = 'chat'
    photo: FSInputFile = FSInputFile('start_bot.jpg')
    users_data[message.from_user.id]['message_data'] = await message.answer_photo(
        photo=photo,
        caption=f"<b>Привет, {message.from_user.first_name}! "
                f"Я многофункциональный бот.</b>\n\n"
                f"Я отвечаю на любые вопросы.\n"
                f"Можете мне написать или воспользоваться командами:\n\n"
                f"{LEXICON_RU['/start']}"
    )


@router_ch.message(Command(commands=['help']))
async def process_help_command(message: Message) -> None:
    if users_data[message.from_user.id]['message_data']:
        await users_data[message.from_user.id]['message_data'].delete()
    if message.from_user.id in users_data:
        users_data[message.from_user.id]['user_status'] = 'chat'
        photo: FSInputFile = FSInputFile('help_bot.gif')
        users_data[message.from_user.id]['message_data'] = await message.answer_photo(
            photo=photo,
            caption=LEXICON_RU['/help'])
    else:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text='Отправьте команду /start'
        )


@router_ch.message(Command(commands=['games']))
async def process_game_command(message: Message) -> None:
    if users_data[message.from_user.id]['message_data']:
        await users_data[message.from_user.id]['message_data'].delete()
    if message.from_user.id in users_data:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text=LEXICON_RU['/games'],
            reply_markup=game_genre_keyboard
        )
        users_data[message.from_user.id]['user_status'] = 'games'
    else:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text='Отправьте команду /start'
        )


@router_ch.message(Command(commands=['info_resources']))
async def process_info_command(message: Message) -> None:
    if users_data[message.from_user.id]['message_data']:
        await users_data[message.from_user.id]['message_data'].delete()
    if message.from_user.id in users_data:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text=LEXICON_RU['/info_resources'],
            reply_markup=info_keyboard
        )
        users_data[message.from_user.id]['user_status'] = 'info'
    else:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text='Отправьте команду /start'
        )


@router_ch.message(Command(commands=['assist_user']))
async def process_support_command(message: Message) -> None:
    if users_data[message.from_user.id]['message_data']:
        await users_data[message.from_user.id]['message_data'].delete()
    if message.from_user.id in users_data:
        users_data[message.from_user.id]['user_status'] = 'assist'
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text=LEXICON_RU['/assist_user'],
            reply_markup=assist_user_keyboard
        )
    else:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text='Отправьте команду /start'
        )


@router_ch.message(Command(commands=['support']))
async def process_developers_command(message: Message) -> None:
    if users_data[message.from_user.id]['message_data']:
        await users_data[message.from_user.id]['message_data'].delete()
    if message.from_user.id in users_data:
        users_data[message.from_user.id]['user_status'] = 'support'
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text=LEXICON_RU['/support'],
            reply_markup=support_keyboard
        )
    else:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text='Отправьте команду /start'
        )
