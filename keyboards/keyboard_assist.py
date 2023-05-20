from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU, LEXICON_LANGUAGE_SMALL_RU, LEXICON_TRANSLATOR_RU, LEXICON_LANGUAGE_RU


# -----Support_keyboard-----

button_message_mp3: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['message_mp3'],
                                                                callback_data='message_mp3_answer')

button_translator: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['translator'],
                                                               callback_data='translator')

button_calculator: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['calculator'],
                                                               callback_data='calculator')

button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')


assist_user_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_message_mp3],
                                                                                   [button_translator],
                                                                                   [button_calculator],
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

def choice_language_small_keyboard() -> InlineKeyboardMarkup:
    small_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_small_language: list[InlineKeyboardButton] = []

    for callback_small, text_small in LEXICON_LANGUAGE_SMALL_RU.items():
        buttons_small_language.append(
            InlineKeyboardButton(text=text_small,
                                 callback_data=callback_small)
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


def choice_language_keyboard() -> InlineKeyboardMarkup:
    language_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons_language: list[InlineKeyboardButton] = []

    for callback, text in LEXICON_LANGUAGE_RU.items():
        buttons_language.append(
            InlineKeyboardButton(text=text,
                                 callback_data=callback)
        )
    language_keyboard.row(*buttons_language, width=4)
    language_keyboard.row(
                       InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                            callback_data='button_no_message_mp3'),
                       InlineKeyboardButton(text=LEXICON_TRANSLATOR_RU['collapse_language_translator'],
                                            callback_data='collapse_language_translator')
                       )
    language_keyboard.row(button_no)
    return language_keyboard.as_markup()


again_translator_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON_TRANSLATOR_RU['again_translator_button'],
    callback_data='again_translator_button'
)

again_translator_press_button: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[again_translator_button],
                                                                                            [button_back],
                                                                                            [button_no]])


# Calculator keyboard


def calculator_keyboard() -> InlineKeyboardMarkup:
    calculator_keyboard_build: InlineKeyboardBuilder = InlineKeyboardBuilder()
    calculator_keyboard_build.row(
        InlineKeyboardButton(text=' ', callback_data='no'),
        InlineKeyboardButton(text='c', callback_data='c'),
        InlineKeyboardButton(text='<-', callback_data='<-'),
        InlineKeyboardButton(text='/', callback_data='/')
    )
    calculator_keyboard_build.row(
        InlineKeyboardButton(text='7', callback_data='7'),
        InlineKeyboardButton(text='8', callback_data='8'),
        InlineKeyboardButton(text='9', callback_data='9'),
        InlineKeyboardButton(text='*', callback_data='*')
    )
    calculator_keyboard_build.row(
        InlineKeyboardButton(text='4', callback_data='4'),
        InlineKeyboardButton(text='5', callback_data='5'),
        InlineKeyboardButton(text='6', callback_data='6'),
        InlineKeyboardButton(text='-', callback_data='-')
    )
    calculator_keyboard_build.row(
        InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='2', callback_data='2'),
        InlineKeyboardButton(text='3', callback_data='3'),
        InlineKeyboardButton(text='+', callback_data='+')
    )
    calculator_keyboard_build.row(
        InlineKeyboardButton(text=' ', callback_data='no'),
        InlineKeyboardButton(text='0', callback_data='0'),
        InlineKeyboardButton(text=',', callback_data=','),
        InlineKeyboardButton(text='=', callback_data='=')
    )
    return calculator_keyboard_build.as_markup()

