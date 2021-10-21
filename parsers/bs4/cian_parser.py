from parsers.utils import cian_apart_to_object
from bs4 import BeautifulSoup


def parse_cian_html(html_source):
    response = BeautifulSoup(html_source, 'lxml', parse_only=True)
    cards = response.select(r'[data-name="CardComponent"]')
    for card in cards:
        name = card.select_one(r'[data-name="TitleComponent"]').text.strip()
        price = card.select_one(r'[data-mark="MainPrice"]').text.strip()
        location = ','.join([x.text.strip() for x in card.select(r'[data-name="GeoLabel"]')])
        yield cian_apart_to_object(name, price, location)
