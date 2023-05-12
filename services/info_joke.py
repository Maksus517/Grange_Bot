from bs4 import BeautifulSoup as BS
import random
import aiohttp


URL = 'https://www.anekdot.ru/last/good/'


async def fetch(session, url) -> str:
    async with session.get(url) as response:
        return await response.text()


async def joke_pars(url: str = URL) -> list:
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BS(html, 'html.parser')
        jokes = soup.find_all('div', class_='text')
        joke = [i.text for i in jokes]
        random.shuffle(joke)
        return joke
