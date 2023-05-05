from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
import os

from lexicon import LEXICON_RU
from data import users_data
from filters import FilterMessageMp3, FilterOpenAi
from services import message_to_mp3
from keyboards import support_keyboard, assist_keyboard

router_sh = Router()


@router_sh.message(Text(text=LEXICON_RU['message_mp3']))
async def process_message_mp3_answer(message: Message):
    users_data[message.from_user.id]['user_status'] = 'message_mp3'
    await message.answer(text=LEXICON_RU['message_mp3_answer'], ephemeral=True,
                         reply_markup=assist_keyboard)


@router_sh.message(Text(text=LEXICON_RU['button_back']), FilterMessageMp3(users_data))
async def process_back_answer(message: Message):
    await message.answer(text=LEXICON_RU['/assist_user'], reply_markup=support_keyboard)
    users_data[message.from_user.id]['user_status'] = None


@router_sh.message(Text(text=LEXICON_RU['button_back']), FilterOpenAi(users_data))
async def process_back_answer(message: Message):
    await message.answer(text=LEXICON_RU['/assist_user'], reply_markup=support_keyboard)
    users_data[message.from_user.id]['user_status'] = None


# Модуль текст в мп3
@router_sh.message(FilterMessageMp3(users_data))
async def process_send_mp3_answer(message: Message, bot: Bot):
    await message_to_mp3(message)
    await bot.send_audio(message.from_user.id, FSInputFile(f'voice from {message.from_user.id}.mp3'),
                         reply_markup=assist_keyboard)
    os.remove(f'voice from {message.from_user.id}.mp3')


# Модуль выхода
@router_sh.message(Text(text=LEXICON_RU['button_no_info']))
async def process_stop_info_answer(message: Message):
    if message.from_user.id in users_data:
        await message.answer(text=LEXICON_RU['no_text'], reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text='Отправьте команду /start')
