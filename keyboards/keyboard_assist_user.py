from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU


button_message_mp3: KeyboardButton = KeyboardButton(text=LEXICON_RU['message_mp3'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_no_info'])


support_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_message_mp3],
                                                                      [button_no]],
                                                            resize_keyboard=True)


button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_back')

button_again_wiki: InlineKeyboardButton = InlineKeyboardButton(text='Ещё!',
                                                               callback_data='button_again_wiki')


assist_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_back]])

assist_wiki_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_again_wiki],
                                                                                   [button_back]])