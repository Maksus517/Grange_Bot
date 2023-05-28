from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon import LEXICON_RU


# -----Other keyboard -----

button_back: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                         callback_data='button_back_info')
button_no: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_no_info'],
                                                       callback_data='button_no_info')

assist_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_back]])


# -----Info keyboard-----

button_wiki: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['wiki'],
                                                         callback_data='wikipedia')
button_open_weather: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['open_weather'],
                                                                 callback_data='open_weather')
button_news: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['news'],
                                                         callback_data='news')
button_joke: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['joke'],
                                                         callback_data='joke')

info_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_wiki, button_open_weather],
                     [button_news, button_joke],
                     [button_no]]
)


# -----Wikipedia keyboard-----

button_leave_here_wiki: InlineKeyboardButton = InlineKeyboardButton(text='📌 Закрепить',
                                                                    callback_data='button_leave_here_wiki')
button_again_wiki: InlineKeyboardButton = InlineKeyboardButton(text='✅ Eще!',
                                                               callback_data='button_again_wiki')
assist_leave_wiki_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_again_wiki, button_leave_here_wiki],
                     [button_back],
                     [button_no]]
)

assist_wiki_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_again_wiki],
                     [button_back],
                     [button_no]]
)


# -----Weather keyboard----- (СДЕЛАТЬ КНОПКУ СВОЙ ГОРОД)!!!!!

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
button_leave_here_open_weather: InlineKeyboardButton = \
    InlineKeyboardButton(text='📌 Закрепить',
                         callback_data='button_leave_here_open_weather')

open_weather_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_ow_1, button_ow_2, button_ow_3, button_ow_4],
                     [button_ow_5, button_ow_6, button_ow_7, button_ow_8],
                     [button_ow_9, button_ow_10, button_ow_11, button_ow_12],
                     [button_ow_13, button_ow_14, button_ow_15, button_ow_16],
                     [button_leave_here_open_weather, button_back],
                     [button_no]]
)


# -----News keyboard-----

button_world_news: InlineKeyboardButton = InlineKeyboardButton(text='📰 СМИ',
                                                               callback_data='smi_news')

button_cyber_sport_news: InlineKeyboardButton = InlineKeyboardButton(text='💻 Киберспорт',
                                                                     callback_data='cyber_sport_news')

news_choice_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_world_news,
                                                                                   button_cyber_sport_news],
                                                                                   [button_no, button_back]])

# smi news

button_ria_politics_news: InlineKeyboardButton = InlineKeyboardButton(text='🖋 Политика',
                                                                      callback_data='politics/')

button_ria_world_news: InlineKeyboardButton = InlineKeyboardButton(text='🌍 В мире',
                                                                   callback_data='world/')

button_ria_economy_news: InlineKeyboardButton = InlineKeyboardButton(text='💰 Экономика',
                                                                     callback_data='economy/')

button_ria_society_news: InlineKeyboardButton = InlineKeyboardButton(text='👩‍👩‍👦‍👦 Общество',
                                                                     callback_data='society/')

button_ria_incidents_news: InlineKeyboardButton = InlineKeyboardButton(text='💥 Происшествия',
                                                                       callback_data='incidents/')

button_ria_defense_safety_news: InlineKeyboardButton = InlineKeyboardButton(text='👮‍♀️ Безопасность',
                                                                            callback_data='defense_safety/')

button_ria_back_news: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                                  callback_data='ria_back_news')
#
# button_ria_sport_news: InlineKeyboardButton = InlineKeyboardButton(text='Спорт',
#                                                                    callback_data='ria_sport_news')

smi_news_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_ria_politics_news,
                                                                                 button_ria_world_news,
                                                                                 button_ria_economy_news],
                                                                                [button_ria_society_news,
                                                                                 button_ria_incidents_news,
                                                                                 button_ria_defense_safety_news],
                                                                                [button_no, button_ria_back_news]])


# cyber_sport_news

button_dota_news: InlineKeyboardButton = InlineKeyboardButton(text='🕹 Дота 2',
                                                              callback_data='dota_news')

cyber_sport_news_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_dota_news],
                                                                                        [button_no,
                                                                                         button_ria_back_news]])


# news actions

button_news_next: InlineKeyboardButton = InlineKeyboardButton(text='Следующая ➡️',
                                                              callback_data='button_news_next')
button_news_prev: InlineKeyboardButton = InlineKeyboardButton(text='⬅️ Предыдущая',
                                                              callback_data='button_news_prev')

button_leave_here_news: InlineKeyboardButton = InlineKeyboardButton(text='📌 Закрепить',
                                                                    callback_data='button_leave_here_news')

button_back_smi_news: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                                  callback_data='smi_news_back_news')

button_back_cyber_news: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['button_back'],
                                                                    callback_data='cyber_news_back_news')

news_press_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_news_next],
                     [button_leave_here_news, button_back_smi_news],
                     [button_no]]
)

news_next_prev_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_news_prev, button_news_next],
                     [button_leave_here_news, button_back_smi_news],
                     [button_no]]
)

news_prev_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_news_prev],
                     [button_leave_here_news, button_back_smi_news],
                     [button_no]]
)

cyber_news_press_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_news_next],
                     [button_leave_here_news, button_back_cyber_news],
                     [button_no]]
)

cyber_news_next_prev_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_news_prev, button_news_next],
                     [button_leave_here_news, button_back_cyber_news],
                     [button_no]]
)

cyber_news_prev_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_news_prev],
                     [button_leave_here_news, button_back_cyber_news],
                     [button_no]]
)


# -----Jokes keyboard-----

button_joke_again: InlineKeyboardButton = InlineKeyboardButton(text='✅ Ещё!',
                                                               callback_data='button_joke_again')
button_leave_here_joke: InlineKeyboardButton = InlineKeyboardButton(text='📌 Закрепить',
                                                                    callback_data='button_leave_here_joke')
assist_joke_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_leave_here_joke, button_joke_again],
                     [button_back],
                     [button_no]]
)
