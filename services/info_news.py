from bs4 import BeautifulSoup as BS
import requests
import aiohttp


URL_RIA: str = 'https://ria.ru/world/'


async def fetch(session, url) -> str:
    async with session.get(url) as response:
        return await response.read()


async def ria_news_parser(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url_ria)
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}\n\n')
        return news_list
