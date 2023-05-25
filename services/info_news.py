from bs4 import BeautifulSoup as BS
import aiohttp


URL_RIA: str = 'https://ria.ru/'

URL_DOTA: str = 'https://www.cybersport.ru/tags/dota-2/'


async def fetch(session, url) -> str:
    async with session.get(url) as response:
        return await response.read()


# ria news

async def ria_politics_news(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}politics/')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


async def ria_world_news(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}world/')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


async def ria_economy_news(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}economy/')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


async def ria_society_news(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}society/')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


async def ria_incidents_news(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}incidents/')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


async def ria_defense_safety_news(url_ria: str = URL_RIA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, f'{url_ria}defense_safety/')
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="list-item__title color-font-hover-only")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'{post[i]["href"]}')
        return news_list


# async def ria_sport_news(url_ria: str = 'https://rsport.ria.ru/') -> list:
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, url_ria)
#         soup = BS(html, 'html.parser')
#         print(soup)
#         post = soup.find_all("a", class_="list-item__title color-front-hover-only")
#         print(post)
#         news_list = []
#         for i in range(len(post)):
#             news_list.append(f'{post[i]["href"]}')
#         return news_list


# cyber sport news

async def cyber_sport_dota_news(url_dota: str = URL_DOTA) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url_dota)
        soup = BS(html, 'html.parser')
        post = soup.find_all("a", class_="link_CocWY")[0:15]
        news_list = []
        for i in range(len(post)):
            news_list.append(f'https://www.cybersport.ru{post[i]["href"]}')
        return news_list
