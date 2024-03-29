from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram.types import Message, FSInputFile, CallbackQuery
import os

from lexicon import LEXICON_RU, LEXICON_TRANSLATOR_RU, LEXICON_CRYPTO_CURRENCIES_RU
from data import users_data
from filters import (FilterMessageMp3, FilterLanguageChoiceOne, FilterLanguageChoiceTwo,
                     FilterTranslator, FilterCalculatorAssist, FilterCryptoCurrenciesAssist, FilterCurrenciesAssist)
from services import message_to_mp3, text_translator, get_ticker, get_rates_cbrf, convert_usd_to_rub
from keyboards import (assist_user_keyboard, assist_assist_user_keyboard, send_mp3_keyboard,
                       choice_language_small_keyboard, choice_language_keyboard, again_translator_press_button,
                       calculator_keyboard, crypto_currencies_keyboard, cbrf_currencies_keyboard,
                       crypto_currencies_keyboard_2)


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
        reply_markup=assist_user_keyboard
    )
    users_data[callback.from_user.id]['user_status'] = 'assist'


@router_sh.callback_query(Text(text=['button_leave_here_mp3']))
async def process_leave_mp3_press_button(callback: CallbackQuery, bot: Bot) -> None:
    await bot.send_audio(
        callback.from_user.id, FSInputFile(f'voice from {callback.from_user.id}.mp3'),
        reply_markup=None)
    await users_data[callback.from_user.id]['message_data'].delete()
    await callback.message.answer(text=LEXICON_RU['/assist_user'],
                                  reply_markup=assist_user_keyboard)
    os.remove(f'voice from {callback.from_user.id}.mp3')


@router_sh.callback_query(Text(text=['button_delete_mp3']))
async def process_leave_mp3_press_button(callback: CallbackQuery) -> None:
    await users_data[callback.from_user.id]['message_data'].delete()
    await callback.message.answer(text=LEXICON_RU['/assist_user'],
                                  reply_markup=assist_user_keyboard)
    os.remove(f'voice from {callback.from_user.id}.mp3')


@router_sh.message(FilterMessageMp3(users_data))
async def process_send_mp3_answer(message: Message, bot: Bot) -> None:
    await users_data[message.from_user.id]['message_data'].delete()
    mp3_wait = await message.answer(text='Пожалуйста подождите...')
    await message_to_mp3(message)
    await mp3_wait.delete()
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


@router_sh.callback_query(Text(text=['unwrap_language_translator']), FilterLanguageChoiceOne(users_data))
async def process_unwrap_language_press_button_one(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['translator_press_button'],
        reply_markup=choice_language_keyboard()
    )


@router_sh.callback_query(Text(text=['collapse_language_translator']), FilterLanguageChoiceOne(users_data))
async def process_collapse_language_press_button_one(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['translator_press_button'],
        reply_markup=choice_language_small_keyboard()
    )


@router_sh.callback_query(FilterLanguageChoiceOne(users_data))
async def process_language_choice_one(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'language_choice_two'
    users_data[callback.from_user.id]['data_list'] = [callback.data]
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['language_choice_one'],
        reply_markup=choice_language_small_keyboard()
    )


@router_sh.callback_query(Text(text=['unwrap_language_translator']), FilterLanguageChoiceTwo(users_data))
async def process_unwrap_language_press_button_two(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['language_choice_one'],
        reply_markup=choice_language_keyboard()
    )


@router_sh.callback_query(Text(text=['collapse_language_translator']), FilterLanguageChoiceTwo(users_data))
async def process_collapse_language_press_button_two(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['language_choice_one'],
        reply_markup=choice_language_small_keyboard()
    )


@router_sh.callback_query(FilterLanguageChoiceTwo(users_data))
async def process_language_choice_two(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['data_list'].append(callback.data)
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['input_text_translator'])
    users_data[callback.from_user.id]['user_status'] = 'translator'


@router_sh.message(FilterTranslator(users_data))
async def process_translation_answer(message: Message) -> None:
    try:
        await users_data[message.from_user.id]['message_data'].delete()
        await message.answer(text=text_translator(message.text,
                                                  users_data[message.from_user.id]['data_list'][0],
                                                  users_data[message.from_user.id]['data_list'][1]))
        users_data[message.from_user.id]['user_status'] = 'assist'
        await message.answer(text=LEXICON_TRANSLATOR_RU['again_translator_press_button'],
                             reply_markup=again_translator_press_button)
    except Exception as ex:
        await message.answer(text=LEXICON_TRANSLATOR_RU['again_translator_error'],
                             reply_markup=again_translator_press_button)
        print(ex)


@router_sh.callback_query(Text(text=['again_translator_button']))
async def process_again_translator_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'language_choice_one'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_TRANSLATOR_RU['translator_press_button'],
        reply_markup=choice_language_small_keyboard()
    )


# Calculator handlers

@router_sh.callback_query(Text(text=['no']))
async def process_calculator_no_press_button(callback: CallbackQuery) -> None:
    try:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text='Это не кнопка...',
            reply_markup=calculator_keyboard()
        )
    except:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text='Не жмите сюда, говорю же, это не кнопка...',
            reply_markup=calculator_keyboard()
        )


@router_sh.callback_query(Text(text=['calculator', 'C']))
async def process_calculator_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'calculator'
    users_data[callback.from_user.id]['data_list'] = []
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text='0',
        reply_markup=calculator_keyboard()
    )


@router_sh.callback_query(FilterCalculatorAssist(users_data) and Text(text=['<-']))
async def process_calculator_delete_data(callback: CallbackQuery) -> None:
    try:
        del users_data[callback.from_user.id]['data_list'][-1]
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=''.join(users_data[callback.from_user.id]['data_list']),
            reply_markup=calculator_keyboard()
        )
    except:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text='0',
            reply_markup=calculator_keyboard()
        )


@router_sh.callback_query(Text(text=['=']))
async def process_calculator_press_button(callback: CallbackQuery) -> None:
    try:
        users_data[callback.from_user.id]['user_status'] = 'calculator'
        result = eval(''.join(users_data[callback.from_user.id]['data_list']))
        if type(result) == float:
            result = round(result, 2)
        users_data[callback.from_user.id]['data_list'] = [num for num in str(result)]
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=''.join(users_data[callback.from_user.id]['data_list']),
            reply_markup=calculator_keyboard()
        )
    except ZeroDivisionError:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text='Делить на 0 нельзя...',
            reply_markup=calculator_keyboard()
        )
        users_data[callback.from_user.id]['data_list'] = []


@router_sh.callback_query(FilterCalculatorAssist(users_data))
async def process_calculator_data_append(callback: CallbackQuery) -> None:

    if users_data[callback.from_user.id]['data_list']:
        if callback.data in ['+', '-', '*', '/'] and \
                users_data[callback.from_user.id]['data_list'][-1] in ['+', '-', '*', '/']:
            users_data[callback.from_user.id]['data_list'][-1] = callback.data
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text=''.join(users_data[callback.from_user.id]['data_list']),
                reply_markup=calculator_keyboard()
            )
        else:
            users_data[callback.from_user.id]['data_list'].append(callback.data)
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text=''.join(users_data[callback.from_user.id]['data_list']),
                reply_markup=calculator_keyboard()
            )
    else:
        if callback.data not in ['0', '+', '.', '*', '/']:
            users_data[callback.from_user.id]['data_list'].append(callback.data)
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text=''.join(users_data[callback.from_user.id]['data_list']),
                reply_markup=calculator_keyboard()
            )
        elif callback.data == '0':
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text='00',
                reply_markup=calculator_keyboard()
            )
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text='0',
                reply_markup=calculator_keyboard()
            )
        elif callback.data == '.':
            users_data[callback.from_user.id]['data_list'].append('0')
            users_data[callback.from_user.id]['data_list'].append(callback.data)
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text=''.join(users_data[callback.from_user.id]['data_list']),
                reply_markup=calculator_keyboard()
            )
        else:
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text=callback.data,
                reply_markup=calculator_keyboard()
            )
            users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
                text='0',
                reply_markup=calculator_keyboard()
            )


# exchange_rate

@router_sh.callback_query(Text(text=['exchange_rate']))
async def process_currencies_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'currencies'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_CRYPTO_CURRENCIES_RU['currencies_press_button'],
        reply_markup=cbrf_currencies_keyboard()
    )


@router_sh.callback_query(Text(text=['crypto_currencies']))
async def process_crypro_currencies_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'crypto_currencies'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_CRYPTO_CURRENCIES_RU['crypro_currencies_press_button'],
        reply_markup=crypto_currencies_keyboard()
    )


@router_sh.callback_query(Text(text=['conversion_currencies']))
async def process_crypro_conversion_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=convert_usd_to_rub(users_data[callback.from_user.id]['message_data'].text),
        reply_markup=crypto_currencies_keyboard()
    )


@router_sh.callback_query(FilterCryptoCurrenciesAssist(users_data))
async def process_crypro_currencies_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=get_ticker(callback.data),
        reply_markup=crypto_currencies_keyboard_2()
    )


@router_sh.callback_query(FilterCurrenciesAssist(users_data))
async def process_crypro_currencies_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=get_rates_cbrf(callback.data),
        reply_markup=cbrf_currencies_keyboard()
    )
