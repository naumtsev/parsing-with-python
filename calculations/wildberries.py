from parsers.lxml.wildberries_parser import parse_wildberries_html as lxml_parse
from parsers.scrapy.wildberries_parser import parse_wildberries_html as scrapy_parse
from parsers.bs4.wildberries_parser import parse_wildberries_html as bs4_parse
from parsers.utils import get_working_time, get_average_working_time, split_into_parts, parse_several_tests
from os import path
from random import shuffle


def test(indexes, number_launches=1):
    sources = []
    for index in indexes:
        try:
            with open(path.dirname(path.abspath(__file__)) + f'/../tests/wildberries/tests_source/test{index}.html', 'r') as file:
                sources.append(file.read())
        except:
            pass
    lxml_time = get_average_working_time(lambda: get_working_time(parse_several_tests, lxml_parse, sources), number_launches)
    scrapy_time = get_average_working_time(lambda: get_working_time(parse_several_tests, scrapy_parse, sources), number_launches)
    bs4_time = get_average_working_time(lambda: get_working_time(parse_several_tests, bs4_parse, sources), number_launches)
    test_id = ','.join(list(map(str, indexes)))
    return {'test_id': f'wildberries_{test_id}', 'lxml_time': lxml_time, 'scrapy_time': scrapy_time, 'bs4_time': bs4_time}


def get_wildberries_results(group_size=1, number_launches=1):
    results = []
    ids = list(range(317))
    shuffle(ids)
    for test_group in split_into_parts(ids, group_size):
        results.append(test(test_group, number_launches))
    return results
