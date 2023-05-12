from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from keyboards import developers_keyboard, developers_assist_keyboard, process_comment_answer_keyboard
from lexicon import LEXICON_DEVELOPERS_RU, LEXICON_RU
from data import users_data, DataBase
from filters import FilterComment, FilterCommentWait

router_dl = Router()


@router_dl.callback_query(Text(text=['button_back_developers']))
async def process_back_answer(callback: CallbackQuery):
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_RU['/assist_user'],
        reply_markup=developers_keyboard
    )
    users_data[callback.from_user.id]['user_status'] = 'developers'


@router_dl.callback_query(Text(text=['button_back_to_comment']))
async def button_back_to_comment(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'comment_wait'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_DEVELOPERS_RU['comment_press_button'],
        reply_markup=process_comment_answer_keyboard
    )


@router_dl.callback_query(Text(text=['comment_user_developers'] or ['button_back_to_comment']))
async def process_comment_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'comment_wait'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_DEVELOPERS_RU['comment_press_button'],
        reply_markup=process_comment_answer_keyboard
    )


@router_dl.callback_query(Text(text=['button_comment_data_base']))
async def process_comment_data_base_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'comment'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_DEVELOPERS_RU['comment_data_base'],
        reply_markup=developers_assist_keyboard)


@router_dl.message(FilterComment(users_data))
async def process_send_comment_answer(message: Message):
    data_base: DataBase = DataBase(message)
    await data_base.insert_user_comment()
    users_data[message.from_user.id]['message_data'] = await message.answer(
        text=LEXICON_DEVELOPERS_RU['comment_save'],
        reply_markup=developers_keyboard
    )
    users_data[message.from_user.id]['user_status'] = 'developers'


@router_dl.message(FilterCommentWait(users_data))
async def process_error_comment(message: Message):
    await users_data[message.from_user.id]['message_data'].delete()
    users_data[message.from_user.id]['message_data'] = await message.answer(
        text=LEXICON_DEVELOPERS_RU['error_comment_developers'],
        reply_markup=process_comment_answer_keyboard
    )
