#   div class="product-card-list"
#       div class="product-card"
#           div class="product-card__wrapper"
#               div class="product-card__img"
#                   img src="img_url" <- tag-value
#               div class="product-card__brand"
#                   div class="product-card__price-commission"
#
#                      | div class="price-commission"
#                      |     span class="price-commission__current-price" <- inside-value
#                      |     del class="price-commission__old-price" <- inside-value
#
#                      | span price
#                      | span lower-price <- inside-value
#                   div class="product-card__brand-name"
#                       span class="goods-name" <- inside-value
#

from parsers.utils import wildberries_product_to_object
from lxml import html


def parse_wildberries_html(html_source):
    doc = html.fromstring(html_source)
    product_card_list = doc.find_class('product-card-list')[0]
    product_cards = product_card_list.find_class("product-card__wrapper")

    for product_card in product_cards:
        img_url = product_card.find_class("product-card__img-wrap")[0].xpath('./img/@src')[0]
        product_card_brand = product_card.find_class('product-card__brand')[0]
        prices = product_card_brand.find_class('price-commission')
        if prices:
            current_price = prices[0].find_class('price-commission__current-price')[0].text_content()
            old_price = prices[0].find_class('price-commission__old-price')[0].text_content()
        else:
            prices = product_card_brand.find_class('price')[0]
            current_price = prices.find_class('lower-price')[0].text_content()
            old_price = 0

        name = product_card_brand.find_class('product-card__brand-name')[0].find_class('goods-name')[0].text_content()
        yield wildberries_product_to_object(name, current_price, old_price, img_url)