import requests

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

cnt = 1
for city in cities:
    for s in search:
        for i in range(1, 6):
            response = requests.get('https://' + city + '.cian.ru/' + s.format(i))
            if response.status_code == 200:
                response.encoding = 'utf-8'
                file = open('test_source/test{0}.html'.format(cnt), 'w')
                file.write(response.text)
                file.close()
                cnt += 1