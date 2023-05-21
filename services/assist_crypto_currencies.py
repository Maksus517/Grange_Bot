import requests
from lexicon import LEXICON_CRIPTO_RU


def get_ticker(coin1: str, coin2: str = 'usd') -> str:
    response = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}')
    result = response.json()
    return f"Покупка {LEXICON_CRIPTO_RU[coin1]} - {round(result[coin1+'_'+coin2]['buy'], 2)} {coin2}\n" \
           f"Продажа {LEXICON_CRIPTO_RU[coin1]} - {round(result[coin1+'_'+coin2]['sell'], 2)} {coin2}"
