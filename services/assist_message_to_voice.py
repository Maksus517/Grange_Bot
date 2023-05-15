from gtts import gTTS
from aiogram.types import Message


async def message_to_mp3(message: Message) -> None:
    tts = gTTS(message.text, lang='ru')
    tts.save(f'voice from {message.from_user.id}.mp3')


async def message_to_voice(message: str) -> list:
    tts = gTTS(message, lang='ru')
    a = tts.get_bodies()
    return a
