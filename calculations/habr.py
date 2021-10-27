from parsers.lxml.habr_parser import parse_habr_html as lxml_parse
from parsers.scrapy.habr_parser import parse_habr_html as scrapy_parse
from parsers.bs4.habr_parser import parse_habr_html as bs4_parse
from parsers.utils import get_working_time, get_average_working_time, split_into_parts, parse_several_tests
from os import path
from random import shuffle
from multiprocessing import Process, Manager

def test(test_id, indexes, number_launches=1):
    sources = []
    for index in indexes:
        try:
            with open(path.dirname(path.abspath(__file__)) + f'/../tests/habr/tests_source/test{index}.html', 'r') as file:
                sources.append(file.read())
        except:
            pass

    result = Manager().dict()
    result['test_id'] = f'habr_{test_id}'


    def process(results, key, f):
        results[key] = f()

    scrapy_thread = Process(target=process, args=(result, 'scrapy_time', lambda: get_average_working_time(lambda: get_working_time(parse_several_tests, scrapy_parse, sources[:]), number_launches)))
    lxml_thread = Process(target=process, args=(result, 'lxml_time', lambda: get_average_working_time(lambda: get_working_time(parse_several_tests, lxml_parse, sources[:]), number_launches)))
    bs4_thread = Process(target=process, args=(result, 'bs4_time', lambda: get_average_working_time(lambda: get_working_time(parse_several_tests, bs4_parse, sources[:]), number_launches)))

    scrapy_thread.start()
    bs4_thread.start()
    lxml_thread.start()
    scrapy_thread.join()
    bs4_thread.join()
    lxml_thread.join()
    return result


def get_habr_results(group_size=1, number_launches=1):
    results = []
    ids = list(range(999))
    shuffle(ids)
    i = 1
    for test_group in split_into_parts(ids, group_size):
        results.append(test(i, test_group, number_launches))
        i+=1
    return results