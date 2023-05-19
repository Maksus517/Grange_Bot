import random

from lexicon.lexicon import LEXICON_KNB_GAME_RU


# Rock paper scissors game

async def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


async def get_winner(user_choice: str, bot_choice: str) -> str:
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
