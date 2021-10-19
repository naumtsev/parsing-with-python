from scrapy.selector import Selector
from parsers.utils import cian_apart_to_object
from scrapy.http import HtmlResponse


def parse_cian_html(html_source):
    response = HtmlResponse(url='cian.test', body=html_source, encoding='utf-8')
    for obj in response.xpath("//article[@data-name='CardComponent']"):
        name = Selector(text=obj.get()).xpath("//span[@data-mark='OfferTitle']/span/text()").get(),
        price = Selector(text=obj.get()).xpath("//span[@data-mark='MainPrice']/span/text()").get(),
        location = Selector(text=obj.get()).xpath("//a[@data-name='GeoLabel']/text()").getall(),
        return cian_apart_to_object(name, price, location)
