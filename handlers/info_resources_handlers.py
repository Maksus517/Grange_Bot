from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
import random

from lexicon import LEXICON_RU, LEXICON_INFO_RU
from services import get_wiki, get_weather, news_parser, joke
from data import users_data
from filters import FilterWiki, FilterOpenWeather
from keyboards import info_keyboard, open_weather_keyboard, assist_keyboard

router_ih = Router()


@router_ih.message(Text(text=LEXICON_RU['button_back']), FilterWiki(users_data))
async def process_back_answer(message: Message):
    await message.answer(text=LEXICON_RU['/info_resources'], reply_markup=info_keyboard)
    users_data[message.from_user.id]['user_status'] = None


@router_ih.message(Text(text=LEXICON_RU['button_back']), FilterOpenWeather(users_data))
async def process_back_answer(message: Message):
    await message.answer(text=LEXICON_RU['/info_resources'], reply_markup=info_keyboard)
    users_data[message.from_user.id]['user_status'] = None


# Кнопка выхода
@router_ih.message(Text(text=LEXICON_RU['button_no_info']))
async def process_stop_info_answer(message: Message):
    if message.from_user.id in users_data:
        await info_resources.edit_text(text=LEXICON_RU['no_text'], reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text='Отправьте команду /start')


# Блок википедии
@router_ih.message(Text(text=LEXICON_RU['wiki']))
async def process_wiki_answer(message: Message):
    users_data[message.from_user.id]['user_status'] = 'wiki'
    await message.answer(text=LEXICON_INFO_RU['wiki_answer'], reply_markup=assist_keyboard)


@router_ih.message(FilterWiki(users_data))
async def process_send_wiki_answer(message: Message):
    await message.answer(text='Пожалуйста подождите')
    await message.answer(text=get_wiki(message.text), reply_markup=assist_keyboard)


# Блок погоды
@router_ih.message(Text(text=LEXICON_RU['open_weather']))
async def process_open_weather_answer(message: Message):
    users_data[message.from_user.id]['user_status'] = 'open_weather'
    await message.answer(text=LEXICON_INFO_RU['open_weather_answer'], reply_markup=open_weather_keyboard)


@router_ih.message(FilterOpenWeather(users_data))
async def process_send_open_weather_answer(message: Message):
    await message.answer(text=get_weather(message.text), reply_markup=open_weather_keyboard)


# Блок новостей
@router_ih.message(Text(text=LEXICON_RU['news']))
async def process_news_answer(message: Message):
    news = news_parser()
    for _ in range(4):
        await message.answer(text=next(news))


# Блок Анекдотов
@router_ih.message(Text(text=LEXICON_RU['joke']))
async def process_joke_answer(message: Message):
    await message.answer(text=random.choice(joke), reply_markup=info_keyboard)
