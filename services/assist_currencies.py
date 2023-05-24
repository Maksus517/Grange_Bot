import requests
from lexicon import LEXICON_CRIPTO_RU
from pycbrf import ExchangeRates
from datetime import datetime
import re


def get_ticker(coin1: str, coin2: str = 'usd') -> str:
    response = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}')
    result = response.json()
    return f"Покупка {LEXICON_CRIPTO_RU[coin1]} - {round(result[coin1+'_'+coin2]['buy'], 6)} {coin2}\n" \
           f"Продажа {LEXICON_CRIPTO_RU[coin1]} - {round(result[coin1+'_'+coin2]['sell'], 6)} {coin2}"


def get_rates_cbrf(currency: str) -> str:
    res = ExchangeRates(datetime.now())
    return f'Курс ЦБ РФ:\n{res[currency].par} {res[currency].name} = {round(res[currency].rate, 2)} рублей.'


def convert_usd_to_rub(text: str) -> str:
    match_usd = re.findall('\d+\.\d+', text)
    exchange_rate = float(ExchangeRates(datetime.now())['USD'].rate)
    return re.sub(f'{match_usd[1]} usd', f'{round(float(match_usd[1]) * exchange_rate, 2)} рублей',
                  re.sub(f'{match_usd[0]} usd', f'{round(float(match_usd[0]) * exchange_rate, 2)} рублей', text))
