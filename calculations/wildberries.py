from parsers.lxml.wildberries_parser import parse_wildberries_html as lxml_parse
from parsers.scrapy.wildberries_parser import parse_wildberries_html as scrapy_parse
from parsers.bs4.wildberries_parser import parse_wildberries_html as bs4_parse
from parsers.utils import get_working_time


def test(index):
    with open(f'../tests/wildberries/tests_source/test{index}.html', 'r') as file:
        resource = file.read()
        lxml_time = get_working_time(lxml_parse, resource)
        scrapy_time = get_working_time(scrapy_parse, resource)
        bs4_time = get_working_time(bs4_parse, resource)
        return {'test_id': f'wildberries_{index}', 'lxml_time': lxml_time, 'scrapy_time': scrapy_time, 'bs4_time': bs4_time}


def get_wildberries_results():
    results = []
    for i in range(53):
        results.append(test(i))

