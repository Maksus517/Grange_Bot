from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram.types import Message, FSInputFile, CallbackQuery
import os

from lexicon import LEXICON_RU, LEXICON_TRANSLATOR_RU
from data import users_data
from filters import FilterMessageMp3, FilterLanguageChoiceOne, FilterLanguageChoiceTwo, FilterTranslator
from services import message_to_mp3, text_translator
from keyboards import (support_keyboard, assist_assist_user_keyboard, send_mp3_keyboard,
                       choice_language_small_keyboard, choice_language_keyboard)


router_sh = Router()


# -----Message_to_mp3-----

@router_sh.callback_query(Text(text=['message_mp3_answer']))
async def process_message_mp3_answer(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'message_mp3'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_RU['message_mp3_answer'],
        ephemeral=True,
        reply_markup=assist_assist_user_keyboard
    )


@router_sh.callback_query(Text(text=['button_no_message_mp3']))
async def process_message_mp3_press_back_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_RU['/assist_user'],
        reply_markup=support_keyboard
    )
    users_data[callback.from_user.id]['user_status'] = 'assist'


@router_sh.callback_query(Text(text=['button_leave_here_mp3']))
async def process_leave_mp3_press_button(callback: CallbackQuery, bot: Bot) -> None:
    await bot.send_audio(
        callback.from_user.id, FSInputFile(f'voice from {callback.from_user.id}.mp3'),
        reply_markup=None)
    await users_data[callback.from_user.id]['message_data'].delete()
    await callback.message.answer(text=LEXICON_RU['/assist_user'],
                                  reply_markup=support_keyboard)
    os.remove(f'voice from {callback.from_user.id}.mp3')


@router_sh.callback_query(Text(text=['button_delete_mp3']))
async def process_leave_mp3_press_button(callback: CallbackQuery) -> None:
    await users_data[callback.from_user.id]['message_data'].delete()
    await callback.message.answer(text=LEXICON_RU['/assist_user'],
                                  reply_markup=support_keyboard)
    os.remove(f'voice from {callback.from_user.id}.mp3')


@router_sh.message(FilterMessageMp3(users_data))
async def process_send_mp3_answer(message: Message, bot: Bot) -> None:
    await users_data[message.from_user.id]['message_data'].delete()
    await message_to_mp3(message)
    users_data[message.from_user.id]['message_data'] = await bot.send_audio(
        message.from_user.id, FSInputFile(f'voice from {message.from_user.id}.mp3'),
        reply_markup=send_mp3_keyboard
    )


# ----Translator-----

@router_sh.callback_query(Text(text=['translator']))
async def process_translator_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'language_choice_one'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['translator_press_button'],
        reply_markup=choice_language_small_keyboard()
    )


@router_sh.callback_query(FilterLanguageChoiceOne(users_data))
async def process_language_choice_one(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['data_list'] = [callback.data]
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['language_choice_one'],
        reply_markup=choice_language_small_keyboard())
    users_data[callback.from_user.id]['user_status'] = 'language_choice_two'
    print(users_data[callback.from_user.id]['data_list'])


@router_sh.callback_query(FilterLanguageChoiceTwo(users_data))
async def process_language_choice_two(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['data_list'].append(callback.data)
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['input_text_translator'])
    users_data[callback.from_user.id]['user_status'] = 'translator'
    print(users_data[callback.from_user.id]['data_list'])


@router_sh.message(FilterTranslator(users_data))
async def process_translation_answer(message: Message) -> None:
    await users_data[message.from_user.id]['message_data'].delete()
    await message.answer(text=text_translator(message.text,
                                              users_data[message.from_user.id]['data_list'][0],
                                              users_data[message.from_user.id]['data_list'][1]))
    users_data[message.from_user.id]['user_status'] = 'assist'
    await message.answer()


