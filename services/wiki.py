import wikipedia


wikipedia.set_lang("ru")


def get_wiki(message: str) -> str:
    page = wikipedia.page(message)
    text: str = page.content
    return text.partition('=')[0][0:-3]
