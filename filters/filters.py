from aiogram.types import Message
from aiogram.filters import BaseFilter


class FilterWiki(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'wiki'


class FilterOpenWeather(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'open_weather'


class FilterMessageMp3(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'message_mp3'


class FilterOpenAi(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'chat_gpt'


class FilterComment(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'comment'
