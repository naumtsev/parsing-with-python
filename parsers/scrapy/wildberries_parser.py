import scrapy
from scrapy.crawler import CrawlerProcess
from parsers.utils import wildberries_product_to_object
from scrapy.http import HtmlResponse

def parse_wildberries_html(html_source):
    response = HtmlResponse(body=html_source, encoding='utf-8')
    prices = response.xpath("//span[@class='price-commission__current-price']/text()").get()
    name = response.xpath("//span[@class='goods-name']/text()").get()
    current_price = response.xpath("//span[@class='price-commission__current-price']/text()").get()
    old_price = response.xpath("//del[@class='price-commission__old-price']/text()").get().strip()
    img_url = response.xpath("//div[@class='product-card__img-wrap']/img/@src").get()
    yield wildberries_product_to_object(name, current_price, old_price, img_url)
