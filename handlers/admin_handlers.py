from aiogram import Router, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, Text

from lexicon import LEXICON_ADMIN_RU
from filters import IsAdmin
from keyboards import admin_keyboard
from config_data import load_config
from data import users_data

router_ah = Router()

admin_config = load_config()
admin_list = admin_config.tg_bot.admin_ids


@router_ah.message(Command(commands=['admin']), IsAdmin(admin_list))
async def process_admin_answer(message: Message):
    await message.answer(text=LEXICON_ADMIN_RU['/admin'], reply_markup=admin_keyboard)


@router_ah.message(Text(text=LEXICON_ADMIN_RU['deleted_menu']), IsAdmin(admin_list))
async def del_deleted_menu_answer(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "menu" удалена',
                         reply_markup=admin_keyboard)


@router_ah.message(Text(text=LEXICON_ADMIN_RU['no_button_admin']), IsAdmin(admin_list))
async def process_stop_answer(message: Message):
    if message.from_user.id in users_data:
        await message.answer(text=LEXICON_ADMIN_RU['no_text'], reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text='Отправьте команду /start')
