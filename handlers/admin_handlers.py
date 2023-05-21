from aiogram import Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Text

from lexicon import LEXICON_ADMIN_RU
from filters import IsAdmin
from keyboards import admin_keyboard
from config_data import load_config
from data import users_data
import os

router_ah = Router()

admin_config = load_config()
admin_list = admin_config.tg_bot.admin_ids


@router_ah.message(Command(commands=['admin']), IsAdmin(admin_list))
async def process_admin_answer(message: Message) -> None:
    users_data[message.from_user.id]['message_data'] = await message.answer(
        text=LEXICON_ADMIN_RU['/admin'],
        reply_markup=admin_keyboard
    )


@router_ah.callback_query(Text(text=['admin_deleted_menu']), IsAdmin(admin_list))
async def del_deleted_menu_answer(callback: CallbackQuery, bot: Bot) -> None:
    await bot.delete_my_commands()
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text='Кнопка "menu" удалена',
        reply_markup=admin_keyboard
    )


@router_ah.callback_query(Text(text=['no_button_admin']), IsAdmin(admin_list))
async def process_stop_answer(callback: CallbackQuery) -> None:
    if callback.from_user.id in users_data:
        await callback.message.edit_text(text=LEXICON_ADMIN_RU['no_text'], reply_markup=None)
    else:
        await callback.message.edit_text(text='Отправьте команду /start')


@router_ah.callback_query(Text(text=['reload_bot']), IsAdmin(admin_list))
async def process_reload_server_press_button(callback: CallbackQuery) -> None:
    os.system('sudo systemctl restart Grange_Bot')
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text='Команда на перезагрузку бота, отправлена на сервер',
        reply_markup=admin_keyboard
    )
