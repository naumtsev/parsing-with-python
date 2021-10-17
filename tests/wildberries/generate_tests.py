from parsers.lxml.utils import get_page_source
import concurrent.futures as pool

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


def write_test(i, product):
    file = open(f'tests_source/test{i}.html', 'w')
    print(get_page_source(f'https://www.wildberries.ru/catalog/0/search.aspx?search={product}'), file=file)
    file.close()


executor = pool.ThreadPoolExecutor(max_workers=10)

for i, product in enumerate(products):
    write_test(i, product)
    executor.submit(write_test, i, product)
