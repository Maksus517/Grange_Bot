from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards import developers_keyboard, assist_keyboard
from lexicon import LEXICON_DEVELOPERS_RU, LEXICON_RU
from data import users_data, DataBase
from filters import FilterComment

router_dl = Router()


@router_dl.message(Text(text=LEXICON_RU['button_back']), FilterComment(users_data))
async def process_back_answer(message: Message):
    await message.answer(text=LEXICON_RU['/assist_user'], reply_markup=developers_keyboard)
    users_data[message.from_user.id]['user_status'] = None


@router_dl.message(Text(text=LEXICON_DEVELOPERS_RU['comment']))
async def process_comment_answer(message: Message):
    users_data[message.from_user.id]['user_status'] = 'comment'
    await message.answer(text=LEXICON_DEVELOPERS_RU['comment_answer'], reply_markup=assist_keyboard)


@router_dl.message(FilterComment(users_data))
async def process_send_comment_answer(message: Message):
    data_base: DataBase = DataBase(message)
    data_base.insert_user_comment()
    await message.answer(text=LEXICON_DEVELOPERS_RU['comment_save'], reply_markup=assist_keyboard)


