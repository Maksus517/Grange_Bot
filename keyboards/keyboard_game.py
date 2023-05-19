from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU, LEXICON_GAMES_RU, LEXICON_ARCADE_GAMES_RU, LEXICON_KNB_GAME_RU


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


choice_arcade_game: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_kmb_game,
                                                                                  button_guess_number_game],
                                                                                 [button_no,
                                                                                  button_back_games]])

# Arcade knb keyboard

button_rock: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['rock'],
                                                         callback_data='rock')
button_scissors: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['scissors'],
                                                             callback_data='scissors')
button_paper: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['paper'],
                                                          callback_data='paper')
button_statistics_knb = InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_KNB_GAME_RU['statistics_knb'],
                                                                    callback_data='statistics_knb')


game_knb_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_rock,
                                                                                 button_scissors,
                                                                                 button_paper],
                                                                                [button_back_game,
                                                                                 button_statistics_knb]])
