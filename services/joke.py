import requests

from bs4 import BeautifulSoup as BS


URL = 'https://www.anekdot.ru/last/good/'


def joke_pars(url=URL):
    get = requests.get(url)
    soup = BS(get.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    return [i.text for i in jokes]


joke = joke_pars()
