from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_ADMIN_RU


button_deleted_menu: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_ADMIN_RU['deleted_menu'],
                                                                 callback_data='admin_deleted_menu')
button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_ADMIN_RU['no_button_admin'],
                                                       callback_data='no_button_admin')


admin_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_deleted_menu],
                                                                             [button_no]])
