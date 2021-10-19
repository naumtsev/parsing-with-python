from parsers.utils import habr_article_to_object
from scrapy.http import HtmlResponse


def parse_habr_html(html_source):
    response = HtmlResponse(url='habr.test', body=html_source, encoding='utf-8')
    times = response.xpath("//span[@class='tm-article-snippet__datetime-published']/time/@datetime").get().strip(),
    tags = [result.lower().strip()
             for result in response.xpath("//a[@class='tm-tags-list__link']/text()").getall()],
    habs = [result.lower().strip()
             for result in response.xpath("//a[@class='tm-hubs-list__link']/text()").getall()],
    saved = response.xpath("//span[@class='bookmarks-button__counter']/text()").get().strip(),
    return habr_article_to_object(times, tags, habs, saved)
