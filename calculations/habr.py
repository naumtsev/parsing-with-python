from parsers.lxml.habr_parser import parse_habr_html as lxml_parse
from parsers.scrapy.habr_parser import parse_habr_html as scrapy_parse
from parsers.bs4.habr_parser import parse_habr_html as bs4_parse
from parsers.utils import get_working_time, get_average_working_time
from os import path


def test(index, number_launches=1):
    with open(path.dirname(path.abspath(__file__)) + f'/../tests/habr/tests_source/test{index}.html', 'r') as file:
        resource = file.read()
        lxml_time = get_average_working_time(lambda: get_working_time(lxml_parse, resource), number_launches)
        scrapy_time = get_average_working_time(lambda: get_working_time(scrapy_parse, resource), number_launches)
        bs4_time = get_average_working_time(lambda: get_working_time(bs4_parse, resource), number_launches)
        return {'test_id': f'habr_{index}', 'lxml_time': lxml_time, 'scrapy_time': scrapy_time, 'bs4_time': bs4_time}


def get_habr_results(number_launches=1):
    results = []
    for i in range(48):
        results.append(test(i, number_launches))
    return results