import requests

from bs4 import BeautifulSoup as BS

URL = 'https://ria.ru/world/'


def news_parser(url: str = URL):
    page = requests.get(url)
    soup = BS(page.content, 'html.parser')
    post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:4]
    for i in range(len(post)):
        yield f'{post[i]["href"]}\n\n'



