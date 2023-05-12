from gtts import gTTS
from aiogram.types import Message


async def message_to_mp3(message: Message) -> None:
    tts = gTTS(message.text, lang='ru')
    tts.save(f'voice from {message.from_user.id}.mp3')
