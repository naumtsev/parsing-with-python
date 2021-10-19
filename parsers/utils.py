#!/usr/bin/env python

def wildberries_product_to_object(product_name, current_price, old_price, img_url):
    return {'product_name': product_name, 'current_price': current_price, 'old_price': old_price, 'img': img_url}

def cian_apart_to_object(name, price, location):
    return {'name': name, 'price': price, 'location' : location}
    
def habr_article_to_object(times, tags, habs, saved):
    return {'times' : times, 'tags': tags, 'habs' : habs, 'saved' : saved}
