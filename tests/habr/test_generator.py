import requests

cnt = 0
for i in range(450000, 450100):
    response = requests.get('https://habr.com/ru/post/{0}/'.format(i))
    if response.status_code == 200:
        response.encoding = 'utf-8'

        file = open('tests_source/test{0}.html'.format(cnt), 'w')
        file.write(response.text)
        file.close()

        cnt += 1
