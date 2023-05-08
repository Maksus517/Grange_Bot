from aiogram.types import Message, CallbackQuery
from aiogram import Router

from services import chat_gpt
from filters import FilterChat
from data import users_data


router_ii: Router = Router()


@router_ii.message(FilterChat(users_data))
async def process_i_i_answer(message: Message):
    try:
        bot_writes = await message.answer(text='Печатаю...')
        await bot_writes.edit_text(text=chat_gpt(message.text))
    except Exception as ex:
        await bot_writes.edit_text(text='Ой, что-то я устал, пойду прилягу...')
        print(ex)
