import requests
import concurrent.futures as pool

def get_test(page_index):
    response = requests.get(f'https://habr.com/ru/post/{450000+page_index}/')
    if response.status_code == 200:
        response.encoding = 'utf-8'

        file = open(f'tests_source/test{page_index}.html', 'w')
        file.write(response.text)
        file.close()


executor = pool.ThreadPoolExecutor(max_workers=20)
for i in range(1000):
    executor.submit(get_test, i)