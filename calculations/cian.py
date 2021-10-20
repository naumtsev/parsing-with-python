from parsers.lxml.cian_parser import parse_cian_html as lxml_parse
from parsers.scrapy.cian_parser import parse_cian_html as scrapy_parse
from parsers.bs4.cian_parser import parse_cian_html as bs4_parse
from parsers.utils import get_working_time, get_average_working_time
from os import path

def test(index, number_launches=1):
    with open(path.dirname(path.abspath(__file__)) + f'/../tests/cian/tests_source/test{index}.html', 'r') as file:
        resource = file.read()
        lxml_time = get_average_working_time(lambda: get_working_time(lxml_parse, resource), number_launches)
        scrapy_time = get_average_working_time(lambda: get_working_time(scrapy_parse, resource), number_launches)
        bs4_time = get_average_working_time(lambda: get_working_time(bs4_parse, resource), number_launches)
        return {'test_id': f'cian_{index}', 'lxml_time': lxml_time, 'scrapy_time': scrapy_time, 'bs4_time': bs4_time}


def get_cian_results(number_launches=1):
    results = []
    for i in range(1, 51):
        results.append(test(i, number_launches))
    return results