#!/usr/bin/env python
import json

def write_to_json(object, path):
    file = open(path + '.json', 'w')
    line = json.dumps(object) + "\n"
    file.write(line)
    file.close()

def wildberries_product_to_object(product_name, current_price, old_price, img_url):
    object = {'product_name': product_name, 'current_price': current_price, 'old_price': old_price, 'img': img_url}
    path = 'wildberries_data'
    write_to_json(object, path)
    return object

def cian_apart_to_object(name, price, location):
    object = {'name': name, 'price': price, 'location' : location}
    path = 'cian_data'
    write_to_json(object, path)
    return object

def habr_article_to_object(times, tags, habs, saved):
    object = {'times' : times, 'tags': tags, 'habs' : habs, 'saved' : saved}
    path = 'habr_data'
    write_to_json(object, path)
    return object