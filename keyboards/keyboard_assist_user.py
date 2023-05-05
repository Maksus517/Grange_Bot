from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import LEXICON_RU


button_message_mp3: KeyboardButton = KeyboardButton(text=LEXICON_RU['message_mp3'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_no_info'])


support_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_message_mp3],
                                                                      [button_no]],
                                                            resize_keyboard=True)


button_back: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_back'])


assist_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_back]],
                                                           resize_keyboard=True)
