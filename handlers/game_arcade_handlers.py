from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, FSInputFile

from services import get_bot_choice, get_winner
from lexicon import LEXICON_ARCADE_GAMES_RU, LEXICON_RU, LEXICON_KNB_GAME_RU
from keyboards import game_genre_keyboard, choice_arcade_game, game_knb_keyboard
from data import users_data


router_ar_gm: Router = Router()


# Other handlers

@router_ar_gm.callback_query(Text(text=['button_back_games']))
async def process_back_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_RU['/games'],
        reply_markup=game_genre_keyboard
    )
    users_data[callback.from_user.id]['user_status'] = 'games'
    users_data[callback.from_user.id]['games_data'] = None


@router_ar_gm.callback_query(Text(text=['button_back_game']))
async def process_arcade_games_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'arcade_games'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_ARCADE_GAMES_RU['arcade_games_choice'],
        reply_markup=choice_arcade_game
    )
    users_data[callback.from_user.id]['games_data'] = None


@router_ar_gm.callback_query(Text(text=['arcade_games']))
async def process_arcade_games_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'arcade_games'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_ARCADE_GAMES_RU['arcade_games_choice'],
        reply_markup=choice_arcade_game
    )


@router_ar_gm.callback_query(Text(text=['rpg_games']))
async def process_arcade_games_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'rpg_games'
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_ARCADE_GAMES_RU['rpg_games_choice'],
        reply_markup=game_genre_keyboard
    )


# Knb game handlers

@router_ar_gm.callback_query(Text(text=['knb_game']))
async def process_knb_game_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'knb_game'
    users_data[callback.from_user.id]['games_data'] = {'knb_game': {'total_games': 0,
                                                                    'wins': 0}}
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_KNB_GAME_RU['knb_press_button'],
        reply_markup=game_knb_keyboard
    )


@router_ar_gm.callback_query(Text(text=['statistics_knb']))
async def process_statistics_knb_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=f"Всего игр сыграно:"
             f"{users_data[callback.from_user.id]['games_data']['knb_game']['total_games']}\n"
             f"Игр выиграно: {users_data[callback.from_user.id]['games_data']['knb_game']['wins']}",
        reply_markup=game_knb_keyboard
    )


@router_ar_gm.callback_query(Text(text=['rock', 'paper', 'scissors']))
async def process_game_button(callback: CallbackQuery):
    bot_choice = await get_bot_choice()
    winner = await get_winner(callback.data, bot_choice)
    if winner == 'nobody_won' or winner == 'bot_won':
        users_data[callback.from_user.id]['games_data']['knb_game']['total_games'] += 1
    else:
        users_data[callback.from_user.id]['games_data']['knb_game']['total_games'] += 1
        users_data[callback.from_user.id]['games_data']['knb_game']['wins'] += 1
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=f'{LEXICON_KNB_GAME_RU["bot_choice"]} '
             f'- {LEXICON_KNB_GAME_RU[bot_choice]}. '
             f'{LEXICON_KNB_GAME_RU[winner]}',
        reply_markup=game_knb_keyboard
    )
