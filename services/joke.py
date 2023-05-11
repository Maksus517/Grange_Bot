from bs4 import BeautifulSoup as BS
import random
import asyncio
import aiohttp


URL = 'https://www.anekdot.ru/last/good/'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def joke_pars(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BS(html, 'html.parser')
        jokes = soup.find_all('div', class_='text')
        return [i.text for i in jokes]

loop = asyncio.get_event_loop()
joke = loop.run_until_complete(joke_pars(URL))
random.shuffle(joke)
