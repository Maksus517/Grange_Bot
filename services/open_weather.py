import requests
from datetime import datetime
from config_data import load_config, Config
from lexicon import code_to_smile

config: Config = load_config()
ow_token: str = config.open_weather.token


def get_weather(city: str, token: str = ow_token) -> str:
    try:
        res = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric'
        )

        data = res.json()
        name: str = data['name']
        temp: int = int(data['main']['temp'])
        max_temp: int = int(data['main']['temp_max'])
        min_temp: int = int(data['main']['temp_min'])
        humidity: int = data['main']['humidity']
        pressure: int = int(data['main']['pressure'] * 0.750064)
        wind: float = data['wind']['speed']
        sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_time - sunrise_time
        description = data['weather'][0]['main']
        if description in code_to_smile:
            wd = code_to_smile[description]
        else:
            wd = 'Посмотрите в окно, не пойму что там за погода'

        return f'Погода в городе: {name}\n\n' \
               f'Температура воздуха: {temp} °C {wd}\n' \
               f'Максимальная температура: {max_temp} °C\n' \
               f'Минимальная температура: {min_temp} °C\n' \
               f'Атмосферное давление: {pressure} мм. рт. ст.\n' \
               f'Влажность воздуха: {humidity} %\n' \
               f'Скорость ветра: {wind} м/с\n\n' \
               f'Восход солнца: {sunrise_time.time()}\n' \
               f'Закат солнца:   {sunset_time.time()}\n' \
               f'Продолжительность дня: {length_of_day}'
    except:
        return f'Вы ввели неверное название города.'

