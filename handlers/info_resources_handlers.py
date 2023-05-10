from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from lexicon import LEXICON_RU, LEXICON_WIKI_RU, LEXICON_WEATHER_RU, LEXICON_JOKE_RU, LEXICON_INFO_RU
from services import get_wiki, get_weather, news_parser, joke
from data import users_data
from filters import FilterWiki, FilterOpenWeather, FilterWikiError, FilterNewsError
from keyboards import (info_keyboard, open_weather_keyboard, assist_keyboard, assist_joke_keyboard,
                       assist_wiki_keyboard, assist_leave_wiki_keyboard, news_press_button_keyboard,
                       news_next_prev_button_keyboard, news_prev_button_keyboard)

router_ih = Router()


# -----Other handlers-----

@router_ih.callback_query(Text(text=['button_back_info']))
async def process_back_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_INFO_RU['back_press_button'],
        reply_markup=info_keyboard
    )
    users_data[callback.from_user.id]['user_status'] = 'info'
    users_data[callback.from_user.id]['data_list'] = []


@router_ih.callback_query(Text(text=['button_no_info']))
async def process_stop_info_press_button(callback: CallbackQuery):
    if callback.from_user.id in users_data:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=LEXICON_RU['no_text']
        )
        users_data[callback.from_user.id]['user_status'] = 'chat'
        users_data[callback.from_user.id]['data_list'] = []
    else:
        await callback.answer(text='Отправьте команду /start')


# -----Wikipedia handlers-----

@router_ih.callback_query(Text(text=['wikipedia']))
async def process_wiki_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'wiki'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_WIKI_RU['wiki_press_button'],
        reply_markup=assist_keyboard
    )


@router_ih.callback_query(Text(text=['button_again_wiki']))
async def process_again_wiki_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'wiki'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_WIKI_RU['wiki_press_button'],
        reply_markup=assist_keyboard
    )


@router_ih.callback_query(Text(text=['button_leave_here_wiki']))
async def process_leave_here_wiki_press_button(callback: CallbackQuery):
    await callback.message.edit_text(text=callback.message.text,
                                     reply_markup=None)
    users_data[callback.from_user.id]['message_data'] = await callback.message.answer(
        text=LEXICON_WIKI_RU['leave_here_wiki_press_button'],
        reply_markup=assist_wiki_keyboard
    )


@router_ih.message(FilterWiki(users_data))
async def process_wiki_answer(message: Message):
    await users_data[message.from_user.id]['message_data'].delete()
    wait_wiki = await message.answer(text=LEXICON_WIKI_RU['wiki_answer_state'])
    try:
        users_data[message.from_user.id]['message_data'] = await wait_wiki.edit_text(
            text=get_wiki(message.text),
            reply_markup=assist_leave_wiki_keyboard
        )
        users_data[message.from_user.id]['user_status'] = 'state_wiki'
    except Exception as ex:
        users_data[message.from_user.id]['message_data'] = await wait_wiki.edit_text(
            text=f"{LEXICON_WIKI_RU['wiki_answer_no_found']} {message.text}...\n"
                 f"{LEXICON_WIKI_RU['leave_here_wiki_press_button']}",
            reply_markup=assist_wiki_keyboard
        )
        users_data[message.from_user.id]['user_status'] = 'state_wiki'
        print(ex)


@router_ih.message(FilterWikiError(users_data))
async def process_wiki_error_answer(message: Message):
    await users_data[message.from_user.id]['message_data'].delete()
    users_data[message.from_user.id]['message_data'] = await message.answer(
        text=LEXICON_WIKI_RU['wiki_error_answer'],
        reply_markup=assist_wiki_keyboard
    )


# -----Weather handlers-----

@router_ih.callback_query(Text(text=['open_weather']))
async def process_open_weather_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'open_weather'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_WEATHER_RU['open_weather_press_button'],
        reply_markup=open_weather_keyboard
    )


@router_ih.callback_query(Text(text=['button_leave_here_open_weather']))
async def process_leave_here_open_weather_press_button(callback: CallbackQuery):
    await callback.message.edit_text(text=callback.message.text,
                                     reply_markup=None)
    users_data[callback.from_user.id]['message_data'] = await callback.message.answer(
        text=LEXICON_WEATHER_RU['leave_here_open_weather'],
        reply_markup=open_weather_keyboard
    )


@router_ih.callback_query(FilterOpenWeather(users_data))
async def process_city_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=get_weather(callback.data),
        reply_markup=open_weather_keyboard
    )


@router_ih.message(FilterOpenWeather(users_data))
async def process_open_weather_answer(message: Message):
    await users_data[message.from_user.id]['message_data'].delete()
    try:
        users_data[message.from_user.id]['message_data'] = await message.answer(
            text=LEXICON_WEATHER_RU['open_weather_state']
        )
        await users_data[message.from_user.id]['message_data'].edit_text(text=get_weather(message.text),
                                                                         reply_markup=open_weather_keyboard)
        users_data[message.from_user.id]['user_status'] = 'open_weather'
    except Exception as ex:
        await users_data[message.from_user.id]['message_data'].edit_text(text=LEXICON_WEATHER_RU['city_no_found'],
                                                                         reply_markup=open_weather_keyboard)
        users_data[message.from_user.id]['user_status'] = 'open_weather'
        print(ex)


# -----News handlers-----

@router_ih.callback_query(Text(text=['news']))
async def process_news_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['user_status'] = 'news'
    users_data[callback.from_user.id]['counter'] = 0
    users_data[callback.from_user.id]['data_list'] = list(news_parser())
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
        reply_markup=news_press_button_keyboard
    )


@router_ih.callback_query(Text(text=['button_news_next']))
async def process_news_press_next_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['counter'] += 1
    if users_data[callback.from_user.id]['counter'] == 14:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_prev_button_keyboard
        )
    else:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_next_prev_button_keyboard
        )


@router_ih.callback_query(Text(text=['button_news_prev']))
async def process_news_press_prev_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['counter'] -= 1
    if users_data[callback.from_user.id]['counter'] == 0:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_press_button_keyboard
        )
    else:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_next_prev_button_keyboard
        )


@router_ih.callback_query(Text(text=['button_leave_here_news']))
async def process_news_press_leave_here_button(callback: CallbackQuery):
    await callback.message.edit_text(text=callback.message.text,
                                     reply_markup=None)
    if users_data[callback.from_user.id]['counter'] == 0:
        users_data[callback.from_user.id]['counter'] += 1
        users_data[callback.from_user.id]['message_data'] = await callback.message.answer(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_next_prev_button_keyboard
        )
    elif users_data[callback.from_user.id]['counter'] == 14:
        users_data[callback.from_user.id]['message_data'] = await callback.message.answer(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_prev_button_keyboard
        )
    else:
        users_data[callback.from_user.id]['message_data'] = await callback.message.answer(
            text=users_data[callback.from_user.id]['data_list'][users_data[callback.from_user.id]['counter']],
            reply_markup=news_next_prev_button_keyboard
        )


@router_ih.message(FilterNewsError(users_data))
async def process_wiki_error_answer(message: Message):
    await users_data[message.from_user.id]['message_data'].delete()
    users_data[message.from_user.id]['user_status'] = 'chat'
    users_data[message.from_user.id]['data_list'] = []


# -----Joke handlers-----

@router_ih.callback_query(Text(text=['joke']))
async def process_joke_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['data_list'] = joke
    users_data[callback.from_user.id]['user_status'] = 'joke'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=users_data[callback.from_user.id]['data_list'][0],
        reply_markup=assist_joke_keyboard)
    del users_data[callback.from_user.id]['data_list'][0]


@router_ih.callback_query(Text(text=['button_joke_again']))
async def process_joke_again_press_button(callback: CallbackQuery):
    if users_data[callback.from_user.id]['data_list']:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=users_data[callback.from_user.id]['data_list'][0],
            reply_markup=assist_joke_keyboard)
        del users_data[callback.from_user.id]['data_list'][0]
    else:
        users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
            text=LEXICON_JOKE_RU['joke_no_found'],
            reply_markup=info_keyboard)


@router_ih.callback_query(Text(text=['button_leave_here_joke']))
async def process_leave_here_joke_press_button(callback: CallbackQuery):
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=callback.message.text,
        reply_markup=None)
    del users_data[callback.from_user.id]['data_list'][0]
    users_data[callback.from_user.id]['message_data'] = await callback.message.answer(
        text=users_data[callback.from_user.id]['data_list'][0],
        reply_markup=assist_joke_keyboard
    )
    del users_data[callback.from_user.id]['data_list'][0]
