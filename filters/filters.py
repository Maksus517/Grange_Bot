from aiogram.types import Message
from aiogram.filters import BaseFilter


class FilterChat(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'chat'


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


class FilterCommentWait(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'comment_wait'


class FilterComment(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'comment'


class FilterWikiError(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'state_wiki'


class FilterNewsError(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'news'


class FilterTranslator(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'translator'


class FilterLanguageChoiceOne(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'language_choice_one'


class FilterLanguageChoiceTwo(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'language_choice_two'


class FilterKnbGame(BaseFilter):
    def __init__(self, users_data: dict[int, dict]) -> None:
        self.users_data = users_data

    async def __call__(self, message: Message) -> bool:
        return self.users_data[message.from_user.id]['user_status'] == 'knb_game'
