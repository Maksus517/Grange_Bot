from aiogram.types import Message
from aiogram import Router

from services import chat_gpt
from data import users_data
from filters import FilterChat


router_ai: Router = Router()


@router_ai.message(FilterChat(users_data))
async def process_i_i_answer(message: Message) -> None:
    if users_data[message.from_user.id]['message_data']:
        await users_data[message.from_user.id]['message_data'].delete()
        users_data[message.from_user.id]['message_data'] = None
    bot_writes = await message.answer(text='Печатаю...')
    try:
        await bot_writes.edit_text(text=chat_gpt(message.text))
    except Exception as ex:
        await bot_writes.edit_text(text='Ой, что-то я устал, пойду прилягу...')
        print(ex)
