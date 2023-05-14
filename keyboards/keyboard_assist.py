from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU, LEXICON_LANGUAGE_SMALL_RU, LEXICON_TRANSLATOR_RU
import googletrans


# -----Support_keyboard-----

button_message_mp3: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['message_mp3'],
                                                                callback_data='message_mp3_answer')

button_translator: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['translator'],
                                                               callback_data='translator')

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')


support_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_message_mp3],
                                                                               [button_translator],
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


# -----Translate keyboard-----

def choice_language_small_keyboard():
    small_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_small_language: list[InlineKeyboardButton] = []

    for callback_small, text_small in LEXICON_LANGUAGE_SMALL_RU.items():
        buttons_small_language.append(
            InlineKeyboardButton(text=text_small,
                                 callback_data=callback_small, width=4)
        )
    small_keyboard.row(*buttons_small_language, width=4)
    small_keyboard.row(
                       InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                            callback_data='button_no_message_mp3'),
                       InlineKeyboardButton(text=LEXICON_TRANSLATOR_RU['unwrap_language_translator'],
                                            callback_data='unwrap_language_translator')
                       )
    small_keyboard.row(button_no)
    return small_keyboard.as_markup()


def choice_language_keyboard():
    language_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_language: list[InlineKeyboardButton] = []

    for callback, text in googletrans.LANGUAGES.items():
        buttons_language.append(
            InlineKeyboardButton(text=text,
                                 callback_data=callback, width=5)
        )
    language_keyboard.row(*buttons_language, width=4)
    language_keyboard.row(
                       InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                            callback_data='button_no_message_mp3'),
                       InlineKeyboardButton(text=LEXICON_TRANSLATOR_RU['collapse_language_translator'],
                                            callback_data='collapse_language_translator')
                       )
    language_keyboard.row(button_no)
    return language_keyboard


