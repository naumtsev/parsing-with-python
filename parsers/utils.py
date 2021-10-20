#!/usr/bin/env python
import json
import time

# def write_to_json(object, path):
#     file = open(path + '.json', 'w')
#     line = json.dumps(object) + "\n"
#     file.write(line)
#     file.close()


def wildberries_product_to_object(product_name, current_price, old_price, img_url):
    return {'product_name': product_name, 'current_price': current_price, 'old_price': old_price, 'img': img_url}


def cian_apart_to_object(name, price, location):
    return {'name': name, 'price': price, 'location': location}


def habr_article_to_object(times, tags, habs, saved):
    return {'times': times, 'tags': tags, 'habs': habs, 'saved': saved}


def get_working_time(f, *args, **kwargs):
    start_time = time.time()
    f(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


def get_average_working_time(f, number_launches=3):
    sum_time = 0
    for i in range(number_launches):
        sum_time += f()
    return sum_time / number_launches
