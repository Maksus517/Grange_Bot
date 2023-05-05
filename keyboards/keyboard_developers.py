from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import LEXICON_RU, LEXICON_DEVELOPERS_RU


button_comment: KeyboardButton = KeyboardButton(text=LEXICON_DEVELOPERS_RU['comment'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_no_info'])


developers_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_comment],
                                                                         [button_no]],
                                                               resize_keyboard=True)