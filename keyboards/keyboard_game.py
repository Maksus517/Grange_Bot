from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU, LEXICON_GAMES_RU


button_arcade_games: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_GAMES_RU['arcade_games'],
                                                                 callback_data='arcade_games')

button_rpg_games: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_GAMES_RU['rpg_games'],
                                                              callback_data='rpg_games')

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')


game_genre_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_arcade_games,
                                                                                   button_rpg_games],
                                                                                  [button_no]])
