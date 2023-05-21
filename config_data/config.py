from environs import Env


class DataBase:
    def __init__(self, host: str, user: str, password: str, db_name: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name


class OpenAI:
    def __init__(self, token: str) -> None:
        self.token = token


class OpenWeather:
    def __init__(self, token: str) -> None:
        self.token = token


class VkApi:
    def __init__(self, token: str) -> None:
        self.token = token


class TgBot:
    def __init__(self, token: str, admin_ids: list[int]) -> None:
        self.token = token
        self.admin_ids = admin_ids


class Config:
    def __init__(
            self, tg_bot: TgBot,
            open_weather: OpenWeather,
            open_ai: OpenAI,
            vk_api: VkApi,
            data_base: DataBase
    ) -> None:
        self.tg_bot = tg_bot
        self.open_weather = open_weather
        self.open_ai = open_ai
        self.data_base = data_base
        self.vk_api = vk_api


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  open_weather=OpenWeather(token=env('OPEN_WEATHER_TOKEN')),
                  open_ai=OpenAI(token=env('OPENAI_KEY')),
                  vk_api=VkApi(token=env('VK_API_KEY')),
                  data_base=DataBase(host=env('HOST'),
                                     user=env('USER'),
                                     password=env('PASSWORD'),
                                     db_name=env('DB_NAME')))
