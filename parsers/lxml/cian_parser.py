from parsers.utils import cian_apart_to_object
from lxml import html


def parse_cian_html(html_source):
    doc = html.fromstring(html_source)
    block = doc.xpath('.//div[@data-name="Offers"]')[0]
    cards = block.xpath('.//article[@data-name="CardComponent"]')
    for card in cards:
        name = card.xpath('.//span[@data-mark="OfferTitle"]/span/text()')[0]
        price = card.xpath('.//span[@data-mark="MainPrice"]')[0].text_content().strip()
        location = ', '.join([x.text.strip() for x in card.xpath('.//a[@data-name="GeoLabel"]')])
        yield cian_apart_to_object(name, price, location)
