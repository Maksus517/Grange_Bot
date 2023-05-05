from aiogram.types import Message
from aiogram import Router

from services import chat_gpt


router_ii: Router = Router()


@router_ii.message()
async def process_i_i_answer(message: Message):
    await message.answer(text=chat_gpt(message.text))
