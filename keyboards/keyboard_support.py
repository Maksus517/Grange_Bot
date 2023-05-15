from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU, LEXICON_SUPPORT_RU


button_comment: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_SUPPORT_RU['comment'],
                                                            callback_data='comment_user_developers')

button_support_project: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_SUPPORT_RU['button_support_project'],
    url='https://yoomoney.ru/to/4100118199215599'
)

button_comment_data_base: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_SUPPORT_RU['button_comment_data_base'],
    callback_data='button_comment_data_base')

button_comment_to_mail: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_SUPPORT_RU['button_comment_to_mail'],
    url='mailto:maksim517@mail.ru'
)

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')

button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_back_developers')

button_back_to_comment: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                                    callback_data='button_back_to_comment')


support_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_comment],
                     [button_support_project],
                     [button_no]]
)

process_comment_answer_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_comment_data_base, button_comment_to_mail],
                     [button_back],
                     [button_no]]
)

developers_assist_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_back_to_comment]]
)
