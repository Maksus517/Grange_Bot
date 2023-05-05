from aiogram.types import Message
from aiogram import Router

from services import chat_gpt


router_ii: Router = Router()


@router_ii.message()
async def process_i_i_answer(message: Message):
    try:
        bot_writes = await message.answer(text='Печатаю...')
        await bot_writes.edit_text(text=chat_gpt(message.text))
    except:
        await message.answer(text="Ой, что-то я закипел...")
