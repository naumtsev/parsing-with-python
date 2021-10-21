from scrapy.http import HtmlResponse
from parsers.utils import wildberries_product_to_object


def parse_wildberries_html(html_source):
    response = HtmlResponse(url='habr.test', body=html_source, encoding='utf-8')
    product_card_list = response.xpath("//div[@class='product-card-list']")
    product_cards = product_card_list.xpath(".//div[@class='product-card j-card-item']")
    for product in product_cards:
        name = product.xpath(".//span[@class='goods-name']/text()").get()
        prices = product.xpath(".//div[@class='price-commission']")
        img_url = product.xpath('.//div[@class="product-card__img"]').xpath('.//img/@src').get()
        if prices:
            current_price = prices.xpath(".//span[@class='price-commission__current-price']/text()").get().strip()
            old_price = prices.xpath(".//del[@class='price-commission__old-price']/text()").get().strip().strip()
        else:
            current_price = product.xpath(".//span[@class='lower-price']/text()").get().strip()
            old_price = '0'

        yield wildberries_product_to_object(name, current_price, old_price, img_url)