from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from parsers.utils import wildberries_product_to_object


def parse_wildberries_html(html_source):
    response = HtmlResponse(url='habr.test', body=html_source, encoding='utf-8')
    product_card_list = response.xpath("//div[@class='product-card-list']").get()
    product_card = Selector(text=product_card_list).css("div.product-card__wrapper").getall()
    for product in product_card:
        name = Selector(text=product).xpath("//span[@class='goods-name']/text()").get()
        prices = Selector(text=product).xpath("//div[@class='price-commission']").get()
        img_url = Selector(text=product).xpath("//div[@class='product-card__img-wrap']/img/@src").get()

        if prices:
            current_price = Selector(text=prices).xpath("//span[@class='price-commission__current-price']/text()").get()
            old_price = Selector(text=prices).xpath("//del[@class='price-commission__old-price']/text()").get().strip()
        else:
            current_price = Selector(text=product).css("span.lower-price::text").get()
            old_price = '0'

        return wildberries_product_to_object(name, current_price, old_price, img_url)
