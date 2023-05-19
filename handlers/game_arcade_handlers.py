from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from services import get_bot_choice, get_winner, get_random_number
from lexicon import LEXICON_ARCADE_GAMES_RU, LEXICON_RU, LEXICON_KNB_GAME_RU, LEXICON_GUESS_NUMBER_RU
from keyboards import (game_genre_keyboard, choice_arcade_game, game_knb_keyboard,
                       game_knb_again_keyboard, choice_random_number_keyboard, game_random_number_again_keyboard,
                       statistics_guess_number_keyboard)
from data import users_data
from filters import FilterKnbGame, FilterGuessNumbersGame


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
        text=f"Всего игр сыграно: "
             f"{users_data[callback.from_user.id]['games_data']['knb_game']['total_games']}\n"
             f"Игр выиграно: {users_data[callback.from_user.id]['games_data']['knb_game']['wins']}",
        reply_markup=game_knb_keyboard
    )


@router_ar_gm.callback_query(Text(text=['button_knb_again']))
async def process_knb_again_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_KNB_GAME_RU['knb_press_button'],
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
        reply_markup=game_knb_again_keyboard
    )


@router_ar_gm.message(FilterKnbGame(users_data))
async def process_kmb_game_error_answer(message: Message) -> None:
    await users_data[message.from_user.id]['message_data'].delete()
    users_data[message.from_user.id]['message_data'] = await message.answer(
        text=LEXICON_KNB_GAME_RU['kmb_game_error'],
        reply_markup=game_knb_keyboard
    )


# Guess the number

@router_ar_gm.callback_query(Text(text=['guess_number_game']))
async def process_guess_number_game_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['user_status'] = 'guess_number_game'
    users_data[callback.from_user.id]['games_data'] = {'guess_number_game': {'secret_number': None,
                                                                             'attempts': 5,
                                                                             'total_games': 0,
                                                                             'wins': 0}}
    users_data[callback.from_user.id]['games_data']['guess_number_game']['secret_number'] = await get_random_number()
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_GUESS_NUMBER_RU['guess_number_press_button'],
        reply_markup=choice_random_number_keyboard()
    )


@router_ar_gm.callback_query(Text(text=['button_guess_number_again']))
async def process_again_guess_number_game_press_button(callback: CallbackQuery) -> None:
    users_data[callback.from_user.id]['games_data']['guess_number_game']['secret_number'] = await get_random_number()
    users_data[callback.from_user.id]['games_data']['guess_number_game']['attempts'] = 5
    users_data[callback.from_user.id]['message_data'] = await callback.message.edit_text(
        text=LEXICON_GUESS_NUMBER_RU['guess_number_press_button'],
        reply_markup=choice_random_number_keyboard()
    )


@router_ar_gm.callback_query(Text(text=['statistics_guess_number']))
async def process_statistics_guess_number_press_button(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        text=f"Всего игр сыграно: "
        f"{users_data[callback.from_user.id]['games_data']['guess_number_game']['total_games']}\n"
        f"Игр выиграно: {users_data[callback.from_user.id]['games_data']['guess_number_game']['wins']}",
        reply_markup=statistics_guess_number_keyboard
    )


@router_ar_gm.callback_query(FilterGuessNumbersGame(users_data))
async def process_guess_number_answer(callback: CallbackQuery) -> None:
    if int(callback.data) == int(users_data[callback.from_user.id]
                                 ['games_data']['guess_number_game']['secret_number']):
        await callback.message.edit_text(text='😎 Ура!!! Вы угадали число!',
                                         reply_markup=game_random_number_again_keyboard)
        users_data[callback.from_user.id]['games_data']['guess_number_game']['total_games'] += 1
        users_data[callback.from_user.id]['games_data']['guess_number_game']['wins'] += 1
    elif int(callback.data) > int(users_data[callback.from_user.id]
                                  ['games_data']['guess_number_game']['secret_number']):
        await callback.message.edit_text(text=f'Мое число меньше {callback.data}',
                                         reply_markup=choice_random_number_keyboard())
        users_data[callback.from_user.id]['games_data']['guess_number_game']['attempts'] -= 1
    elif int(callback.data) < int(users_data[callback.from_user.id]
                                  ['games_data']['guess_number_game']['secret_number']):
        await callback.message.edit_text(text=f'Мое число больше {callback.data}',
                                         reply_markup=choice_random_number_keyboard())
        users_data[callback.from_user.id]['games_data']['guess_number_game']['attempts'] -= 1

    if int(users_data[callback.from_user.id]['games_data']['guess_number_game']['attempts']) == 0:
        await callback.message.edit_text(
                text=f"❗️ К сожалению, у вас больше не осталось "
                f"попыток. 😔 Вы проиграли...\nМое число "
                f"было {users_data[callback.from_user.id]['games_data']['guess_number_game']['secret_number']}",
                reply_markup=game_random_number_again_keyboard)
        users_data[callback.from_user.id]['games_data']['guess_number_game']['total_games'] += 1


@router_ar_gm.message(FilterGuessNumbersGame(users_data))
async def process_guess_number_error_answer(message: Message) -> None:
    await users_data[message.from_user.id]['message_data'].delete()
    users_data[message.from_user.id]['message_data'] = await message.answer(
        text=LEXICON_KNB_GAME_RU['guess_number_error'],
        reply_markup=game_random_number_again_keyboard
    )
