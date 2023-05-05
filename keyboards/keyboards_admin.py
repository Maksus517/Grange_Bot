from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import LEXICON_ADMIN_RU


button_deleted_menu: KeyboardButton = KeyboardButton(text=LEXICON_ADMIN_RU['deleted_menu'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_ADMIN_RU['no_button_admin'])


admin_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_deleted_menu],
                                                                    [button_no]],
                                                          resize_keyboard=True)
