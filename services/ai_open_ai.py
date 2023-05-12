from config_data import Config, load_config

import openai


config: Config = load_config()
openai.api_key = config.open_ai.token


def chat_gpt(text: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
    return response['choices'][0]['text']
