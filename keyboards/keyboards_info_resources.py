from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon import LEXICON_RU


button_wiki: KeyboardButton = KeyboardButton(text=LEXICON_RU['wiki'])
button_open_weather: KeyboardButton = KeyboardButton(text=LEXICON_RU['open_weather'])
button_news: KeyboardButton = KeyboardButton(text=LEXICON_RU['news'])
button_joke: KeyboardButton = KeyboardButton(text=LEXICON_RU['joke'])
button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_no_info'])


info_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_wiki, button_news],
                                                                   [button_open_weather, button_joke],
                                                                   [button_no]],
                                                         resize_keyboard=True)

button_ow_1: KeyboardButton = KeyboardButton(text='Москва')
button_ow_2: KeyboardButton = KeyboardButton(text='Санкт-Петербург')
button_ow_3: KeyboardButton = KeyboardButton(text='Новосибирск')
button_ow_4: KeyboardButton = KeyboardButton(text='Екатеринбург')
button_ow_5: KeyboardButton = KeyboardButton(text='Казань')
button_ow_6: KeyboardButton = KeyboardButton(text='Нижний Новгород')
button_ow_7: KeyboardButton = KeyboardButton(text='Челябинск')
button_ow_8: KeyboardButton = KeyboardButton(text='Красноярск')
button_ow_9: KeyboardButton = KeyboardButton(text='Самара')
button_ow_10: KeyboardButton = KeyboardButton(text='Уфа')
button_ow_11: KeyboardButton = KeyboardButton(text='Ростов-на-Дону')
button_ow_12: KeyboardButton = KeyboardButton(text='Омск')
button_ow_13: KeyboardButton = KeyboardButton(text='Краснодар')
button_ow_14: KeyboardButton = KeyboardButton(text='Воронеж')
button_ow_15: KeyboardButton = KeyboardButton(text='Волгоград')
button_ow_16: KeyboardButton = KeyboardButton(text='Пермь')
button_back: KeyboardButton = KeyboardButton(text=LEXICON_RU['button_back'])


open_weather_keyboard: ReplyKeyboardMarkup = \
    ReplyKeyboardMarkup(keyboard=[[button_ow_1, button_ow_2, button_ow_3, button_ow_4],
                                  [button_ow_5, button_ow_6, button_ow_7, button_ow_8],
                                  [button_ow_9, button_ow_10, button_ow_11, button_ow_12],
                                  [button_ow_13, button_ow_14, button_ow_15, button_ow_16],
                                  [button_back]])

