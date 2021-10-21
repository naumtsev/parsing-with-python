import time
from contextlib import closing
from selenium.webdriver import Firefox
import concurrent.futures as pool


def get_page_source(url):
    with closing(Firefox()) as browser:
        browser.get(url)
        time.sleep(5)
        return browser.page_source
    return ''


products = [
    'книги+для+детей',
    'телефоны',
    'кремы',
    'настольные+игры',
    'телевизоры',
    'ноутбуки',
    'постельное+бельё',
    'одежда',
    'обувь',
    'инструменты+для+дачи',
    'часы',
    'канцтовары',
    'подарки',
    'пылесосы',
    'зоотовары',
    'игрушки',
    'ремень',
    'диваны',
    'стулья',
    'кухонный+гарнитур',
    'косметика',
    'китайский+чай',
    'сок+для+детей',
    'конфеты',
    'мармелад',
    'орехи',
    'семена+для+дачи',
    'кронштейн',
    'бокалы',
    'кастрюли',
    'чайники',
    'вино',
    'кофе',
    'самокат',
    'наручники',
    'шлем',
    'пластырь',
    'шприцы',
    'торты',
    'форма+для+выпекания',
    'утюг',
    'шкаф',
    'гардина',
    'кресло',
    'фен',
    'сапоги',
    'наушники',
    'принтер',
    'клавиатура',
    'корм+для+животных',
    'перец',
    'антисептик',
    'спрей'
]


def write_test(i, product, page):
    file = open(f'tests_source/test{i}.html', 'w')
    source = get_page_source(f'https://www.wildberries.ru/catalog/0/search.aspx?search={product}&page={page}')
    file.write(source)
    file.close()


executor = pool.ThreadPoolExecutor(max_workers=5)
test_id = 0
for product in products:
    for page in range(10):
        executor.submit(write_test, test_id, product, page)
        test_id += 1