from parsers.utils import habr_article_to_object
from lxml import html


def parse_habr_html(html_source):
    doc = html.fromstring(html_source)
    time_ = doc.xpath('//span[@class="tm-article-snippet__datetime-published"]')[0].text_content()
    tags = [x.text_content().strip().lower() for x in doc.xpath('//a[@class="tm-tags-list__link"]')]
    habs = [x.text_content().strip().lower() for x in doc.xpath('//a[@class="tm-hubs-list__link"]')]
    saved = doc.xpath('//span[@class="bookmarks-button__counter"]')[0].text_content().strip()
    yield habr_article_to_object(time_, tags, habs, saved)