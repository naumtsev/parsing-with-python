from parsers.utils import habr_article_to_object
from lxml import html


def parse_habr_html(html_source):
    doc = html.fromstring(html_source)
    time_ = doc.find_class("tm-article-snippet__datetime-published")[0].text_content()
    tags = [x.text_content().strip().lower() for x in doc.find_class("tm-tags-list__link")]
    habs = [x.text_content().strip().lower() for x in doc.find_class("tm-hubs-list__link")]
    saved = doc.find_class("bookmarks-button__counter")[0].text_content().strip()
    return habr_article_to_object(time_, tags, habs, saved)
