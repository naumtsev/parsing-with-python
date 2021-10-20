from parsers.lxml.habr_parser import parse_habr_html as lxml_parse
from parsers.scrapy.habr_parser import parse_habr_html as scrapy_parse
from parsers.bs4.habr_parser import parse_habr_html as bs4_parse
from parsers.utils import get_working_time


def test(index):
    with open(f'../tests/habr/tests_source/test{index}.html', 'r') as file:
        resource = file.read()
        lxml_time = get_working_time(lxml_parse, resource)
        scrapy_time = get_working_time(scrapy_parse, resource)
        bs4_time = get_working_time(bs4_parse, resource)
        return {'test_id': f'habr_{index}', 'lxml_time': lxml_time, 'scrapy_time': scrapy_time, 'bs4_time': bs4_time}


def get_habr_results():
    results = []
    for i in range(48):
        results.append(test(i))
    return results
