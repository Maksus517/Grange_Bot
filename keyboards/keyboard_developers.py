from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU, LEXICON_DEVELOPERS_RU


button_comment: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_DEVELOPERS_RU['comment'],
                                                            callback_data='comment_user_developers')

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')

button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_back_developers')


developers_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_comment],
                                                                                  [button_no]])

developers_assist_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_back]])
