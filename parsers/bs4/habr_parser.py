from parsers.utils import habr_article_to_object
from bs4 import BeautifulSoup

def parse_habr_html(html_source):
    response = BeautifulSoup(html_source, 'html.parser')
    times = response.select_one(".tm-article-snippet__datetime-published").text.strip()
    tags = [x.text.strip().lower() for x in response.select(".tm-tags-list__link")]
    habs = [x.text.strip().lower() for x in response.select(".tm-hubs-list__link")]
    saved = response.select_one(".bookmarks-button__counter").text.strip()
    yield habr_article_to_object(times, tags, habs, saved)