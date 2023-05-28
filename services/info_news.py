from bs4 import BeautifulSoup as BS
import aiohttp


URL_RIA: str = 'https://ria.ru/'

URL_DOTA: str = 'https://www.cybersport.ru/tags/'


async def fetch(session, url) -> str:
    async with session.get(url) as response:
        return await response.read()


# ria news

async def ria_news(patch: str, url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}{patch}')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


# cyber sport news

async def cyber_sport_news(patch: str, url_dota: str = URL_DOTA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_dota}{patch}')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="link_CocWY")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'https://www.cybersport.ru{post[i]["href"]}')
        return news_list
