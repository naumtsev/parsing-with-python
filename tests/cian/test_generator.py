import requests
import concurrent.futures as pool

search = [
    'kupit-{0}-komnatnuyu-kvartiru/',
    'snyat-{0}-komnatnuyu-kvartiru/'
]

cities = [
    'spb',
    'ekb',
    'irkutsk',
    'tula',
    'omsk'
]


def get_test(url, test_id):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        file = open(f'tests_source/test{test_id}.html', 'w')
        file.write(response.text)
        file.close()

executor = pool.ThreadPoolExecutor(max_workers=3)

test_id = 0
for city in cities:
    for s in search:
        for i in range(1, 14):
                url = 'https://' + city + '.cian.ru/' + s.format(i)
                executor.submit(get_test, url, test_id)
                test_id += 1
