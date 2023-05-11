from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU


# -----Support_keyboard-----

button_message_mp3: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['message_mp3'],
                                                                callback_data='message_mp3_answer')

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')


support_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_message_mp3],
                                                                               [button_no]])


# -----message_to_mp3_keyboard-----

button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_no_message_mp3')
button_leave_here_mp3: InlineKeyboardButton = InlineKeyboardButton(text='📌 Закрепить файл',
                                                                   callback_data='button_leave_here_mp3')

button_delete_mp3: InlineKeyboardButton = InlineKeyboardButton(text='🗑 Удалить файл',
                                                               callback_data='button_delete_mp3')

assist_assist_user_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_back]])

send_mp3_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_leave_here_mp3],
                                                                                [button_delete_mp3]])
