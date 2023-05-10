from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, CallbackQuery
import os

from lexicon import LEXICON_RU
from data import users_data
from filters import FilterMessageMp3
from services import message_to_mp3
from keyboards import support_keyboard, assist_assist_user_keyboard

router_sh = Router()


@router_sh.callback_query(Text(text=['message_mp3_answer']))
async def process_message_mp3_answer(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'message_mp3'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_RU['message_mp3_answer'],
        ephemeral=True,
        reply_markup=assist_assist_user_keyboard
    )


@router_sh.callback_query(Text(text=['button_no_message_mp3']))
async def process_message_mp3_press_back_button(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/assist_user'], reply_markup=support_keyboard)
    users_data[callback.from_user.id]['user_status'] = 'assist'


@router_sh.message(FilterMessageMp3(users_data))
async def process_send_mp3_answer(message: Message, bot: Bot):
    await users_data[message.from_user.id]['message_data'].delete()
    await message_to_mp3(message)
    await bot.send_audio(message.from_user.id, FSInputFile(f'voice from {message.from_user.id}.mp3'))
    await message.answer(text=LEXICON_RU['/assist_user'],
                         ephemeral=True,
                         reply_markup=support_keyboard)
    os.remove(f'voice from {message.from_user.id}.mp3')
