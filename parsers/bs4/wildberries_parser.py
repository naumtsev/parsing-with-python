from parsers.utils import wildberries_product_to_object
from bs4 import BeautifulSoup


def parse_wildberries_html(html_source):
    response = BeautifulSoup(html_source, 'lxml')
    cards_list = response.select_one(r".product-card-list")
    cards = cards_list.select(r".product-card")
    for card in cards:
        img_url = card.select_one(r".product-card__img-wrap").img['src']
        brand = card.select_one(r".product-card__brand")
        prices = card.select_one(r".price-commission")
        if prices:
            current_price = prices.select_one(r".price-commission__current-price").text.strip()
            old_price = prices.select_one(r".price-commission__old-price").text.strip()
        else:
            prices = brand.select_one(r".price")
            current_price = prices.select_one(r".lower-price").text.strip()
            old_price = '0'

        name = brand.select_one(r'.product-card__brand-name').select_one(r'.goods-name').text.strip()
        yield wildberries_product_to_object(name, current_price, old_price, img_url)