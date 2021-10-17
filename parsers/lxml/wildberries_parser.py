#   div class="product-card-list"
#       div class="product-card"
#           div class="product-card__wrapper"
#               div class="product-card__img"
#                   img src="img_url" <- tag-value
#               div class="product-card__brand"
#                   div class="product-card__price-commission"
#                       div class="price-commission"
#                           span class="price-commission__current-price" <- inside-value
#                           del class="price-commission__old-price" <- inside-value
#                   div class="product-card__brand-name"
#                       span class="goods-name" <- inside-value
#

from pyquery import PyQuery
from utils import to_json


def process_test(test_id):
    html_source_path = f'../../tests/wildberries/tests_source/test{test_id}.html'
    with open(html_source_path, 'r') as file:
        source = file.read()
        return parse_html(source)


def parse_html(html_source):
    products = []
    page = PyQuery(html_source)
    product_card_list = page('div[class=product-card-list]')
    product_cards = product_card_list('div[class=product-card__wrapper]').items()
    for product_card in product_cards:
        img_url = product_card('div[class=product-card__img]')('img').attr('src')
        product_card_brand = product_card('div[class=product-card__brand]')
        prices = product_card_brand('div[class=product-card__price-commission]')('div[class=price-commission]')
        current_price = prices('span[class=price-commission__current-price]').text()
        old_price = prices('div[class=price-commission__old-price]').text()
        name = product_card_brand('div[class=product-card__brand-name]')('span[class=goods-name]').text()
        products.append(to_json(name, current_price, old_price, img_url))
    return products


print(process_test(0))