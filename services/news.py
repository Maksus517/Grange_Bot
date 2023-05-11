from bs4 import BeautifulSoup as BS
import asyncio
import aiohttp


URL = 'https://ria.ru/world/'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.read()


async def news_parser(url: str = URL) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}\n\n')
        return news_list
