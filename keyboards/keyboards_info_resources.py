from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU


button_wiki: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['wiki'],
                                                         callback_data='wikipedia')
button_open_weather: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['open_weather'],
                                                                 callback_data='open_weather')
button_news: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['news'],
                                                         callback_data='news')
button_joke: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['joke'],
                                                         callback_data='joke')
button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')


info_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_wiki, button_open_weather],
                                                                            [button_news, button_joke],
                                                                            [button_no]])


button_ow_1: InlineKeyboardButton = InlineKeyboardButton(text='Москва',
                                                         callback_data='Москва')
button_ow_2: InlineKeyboardButton = InlineKeyboardButton(text='Санкт-Петербург',
                                                         callback_data='Санкт-Петербург')
button_ow_3: InlineKeyboardButton = InlineKeyboardButton(text='Новосибирск',
                                                         callback_data='Новосибирск')
button_ow_4: InlineKeyboardButton = InlineKeyboardButton(text='Екатеринбург',
                                                         callback_data='Екатеринбург')
button_ow_5: InlineKeyboardButton = InlineKeyboardButton(text='Казань',
                                                         callback_data='Казань')
button_ow_6: InlineKeyboardButton = InlineKeyboardButton(text='Нижний Новгород',
                                                         callback_data='Нижний Новгород')
button_ow_7: InlineKeyboardButton = InlineKeyboardButton(text='Челябинск',
                                                         callback_data='Челябинск')
button_ow_8: InlineKeyboardButton = InlineKeyboardButton(text='Красноярск',
                                                         callback_data='Красноярск')
button_ow_9: InlineKeyboardButton = InlineKeyboardButton(text='Самара',
                                                         callback_data='Самара')
button_ow_10: InlineKeyboardButton = InlineKeyboardButton(text='Уфа',
                                                          callback_data='Уфа')
button_ow_11: InlineKeyboardButton = InlineKeyboardButton(text='Ростов-на-Дону',
                                                          callback_data='Ростов-на-Дону')
button_ow_12: InlineKeyboardButton = InlineKeyboardButton(text='Омск',
                                                          callback_data='Омск')
button_ow_13: InlineKeyboardButton = InlineKeyboardButton(text='Краснодар',
                                                          callback_data='Краснодар')
button_ow_14: InlineKeyboardButton = InlineKeyboardButton(text='Воронеж',
                                                          callback_data='Воронеж')
button_ow_15: InlineKeyboardButton = InlineKeyboardButton(text='Волгоград',
                                                          callback_data='Волгоград')
button_ow_16: InlineKeyboardButton = InlineKeyboardButton(text='Пермь',
                                                          callback_data='Пермь')
button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_back')


open_weather_keyboard: InlineKeyboardMarkup = \
    InlineKeyboardMarkup(inline_keyboard=[[button_ow_1, button_ow_2, button_ow_3, button_ow_4],
                                  [button_ow_5, button_ow_6, button_ow_7, button_ow_8],
                                  [button_ow_9, button_ow_10, button_ow_11, button_ow_12],
                                  [button_ow_13, button_ow_14, button_ow_15, button_ow_16],
                                  [button_back]])


button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_back')

button_leave_here_wiki: InlineKeyboardButton = InlineKeyboardButton(text='Оставить ответ здесь',
                                                                    callback_data='button_leave_here_wiki')

button_again_joke: InlineKeyboardButton = InlineKeyboardButton(text='Ещё!',
                                                               callback_data='button_again_joke')

button_again_open_weather: InlineKeyboardButton = InlineKeyboardButton(text='Посмотреть погоду в другом городе',
                                                                       callback_data='button_again_open_weather')

button_again_wiki: InlineKeyboardButton = InlineKeyboardButton(text='Да!',
                                                               callback_data='button_again_wiki')

button_again2_wiki: InlineKeyboardButton = InlineKeyboardButton(text='Eще!',
                                                                callback_data='button_again_wiki')

assist_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_back]])

assist_joke_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_again_joke],
                                                                                   [button_back],
                                                                                   [button_no]])

assist_open_weather_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_again_open_weather],
                                                                                           [button_back],
                                                                                           [button_no]])

assist_leave_wiki_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_again2_wiki,
                                                                                          button_leave_here_wiki],
                                                                                         [button_back],
                                                                                          [button_no]])

assist_wiki_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_again_wiki],
                                                                                   [button_back],
                                                                                   [button_no]])
