from parsers.utils import cian_apart_to_object
from scrapy.http import HtmlResponse


def parse_cian_html(html_source):
    response = HtmlResponse(url='cian.test', body=html_source, encoding='utf-8')
    for obj in response.xpath("//article[@data-name='CardComponent']"):
        name = obj.xpath(".//span[@data-mark='OfferTitle']/span/text()").get(),
        price = obj.xpath(".//span[@data-mark='MainPrice']/span/text()").get(),
        location = obj.xpath(".//a[@data-name='GeoLabel']/text()").getall(),
        yield cian_apart_to_object(name, price, location)
