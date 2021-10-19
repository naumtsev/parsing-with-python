from parsers.utils import cian_apart_to_object
from lxml import html


def parse_cian_html(html_source):
    doc = html.fromstring(html_source)
    block = doc.xpath('//div[@data-name="Offers"]')[0]
    cards = block.cssselect('article[data-name="CardComponent"]')
    for card in cards:
        name = card.cssselect('span[data-mark="OfferTitle"]')[0].cssselect('span')[0].text_content()
        price = card.cssselect('span[data-mark="MainPrice"]')[0].text_content().strip()
        location = ', '.join([x.text.strip() for x in card.cssselect('a[data-name="GeoLabel"]')])
        yield cian_apart_to_object(name, price, location)
