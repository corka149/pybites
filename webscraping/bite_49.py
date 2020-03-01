from collections import namedtuple

from bs4 import BeautifulSoup as Soup
from bs4.element import NavigableString
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_description(soup):
    div = soup.find('div', {'class': 'dotd-main-book-summary'})
    description = [c.text.strip() for c in div.children if
                   not isinstance(c, NavigableString) and len(c.attrs) == 0]
    return description[1]


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    title = soup.h2.text.strip()
    description = get_description(soup)
    image = soup.find('img', {'class': 'bookimage'}).get('src')
    link = soup.find('div', {'class': 'dotd-main-book-image'}).find('a').get('href')
    return Book(title, description, image, link)


if __name__ == '__main__':
    print(get_book())
