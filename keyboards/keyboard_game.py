from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import (LEXICON_RU, LEXICON_GAMES_RU, LEXICON_ARCADE_GAMES_RU,
                     LEXICON_KNB_GAME_RU, LEXICON_GUESS_NUMBER_RU)


# Games keyboard

button_arcade_games: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_GAMES_RU['arcade_games'],
                                                                 callback_data='arcade_games')

button_rpg_games: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_GAMES_RU['rpg_games'],
                                                              callback_data='rpg_games')

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')

button_back_games: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                               callback_data='button_back_games')

button_back_game: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                              callback_data='button_back_game')


game_genre_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_arcade_games,
                                                                                   button_rpg_games],
                                                                                  [button_no]])


# Arcade keyboard

button_kmb_game: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_ARCADE_GAMES_RU['knb_game'],
                                                             callback_data='knb_game')

button_guess_number_game: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_ARCADE_GAMES_RU['guess_number_game'],
                                                                      callback_data='guess_number_game')


choice_arcade_game: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_kmb_game],
                                                                                 [button_guess_number_game],
                                                                                 [button_no,
                                                                                  button_back_games]])

# Arcade knb keyboard

button_rock: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['rock'],
                                                         callback_data='rock')
button_scissors: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['scissors'],
                                                             callback_data='scissors')
button_paper: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['paper'],
                                                          callback_data='paper')
button_statistics_knb: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['statistics_knb'],
                                                                   callback_data='statistics_knb')
button_knb_again: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['button_knb_again'],
                                                              callback_data='button_knb_again')


game_knb_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_rock,
                                                                                 button_scissors,
                                                                                 button_paper],
                                                                                [button_back_game,
                                                                                 button_statistics_knb]])

game_knb_again_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_knb_again],
                                                                                      [button_back_game]])


# Arcade random number game

def choice_random_number_keyboard() -> InlineKeyboardMarkup:
    numbers_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_numbers: list[InlineKeyboardButton] = []

    for number in range(1, 50):
        buttons_numbers.append(
            InlineKeyboardButton(text=number,
                                 callback_data=number)
        )
    numbers_keyboard.row(*buttons_numbers, width=7)
    numbers_keyboard.row(InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                              callback_data='button_back_game'))
    return numbers_keyboard.as_markup()


button_random_again: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_GUESS_NUMBER_RU['button_guess_number_again'],
    callback_data='button_guess_number_again'
)
button_statistics_guess_number: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_GUESS_NUMBER_RU['statistics_guess_number'],
    callback_data='statistics_guess_number'
)

game_random_number_again_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_random_again],
                     [button_statistics_guess_number],
                     [button_back_game]]
)

statistics_guess_number_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_random_again],
                     [button_back_game]]
)
