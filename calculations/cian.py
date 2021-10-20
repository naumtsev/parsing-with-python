from parsers.lxml.cian_parser import parse_cian_html as lxml_parse
from parsers.scrapy.cian_parser import parse_cian_html as scrapy_parse
from parsers.bs4.cian_parser import parse_cian_html as bs4_parse
from parsers.utils import get_working_time


def test(index):
    with open(f'../tests/cian/tests_source/test{index}.html', 'r') as file:
        resource = file.read()
        lxml_time = get_working_time(lxml_parse, resource)
        scrapy_time = get_working_time(scrapy_parse, resource)
        bs4_time = get_working_time(bs4_parse, resource)
        return {'test_id': f'cian_{index}', 'lxml_time': lxml_time, 'scrapy_time': scrapy_time, 'bs4_time': bs4_time}


def get_cian_results():
    results = []
    for i in range(1, 51):
        results.append(test(i))
    return results

print(get_cian_results())