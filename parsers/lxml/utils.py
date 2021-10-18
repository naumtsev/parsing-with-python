#!/usr/bin/env python
import time
from contextlib import closing
from selenium.webdriver import Firefox


def get_page_source(url):
    with closing(Firefox()) as browser:
        browser.get(url)
        time.sleep(5)
        return browser.page_source
    return ''


def to_dict(name, current_price, old_price, img_url):
    return {'name': name, 'current_price': current_price, 'old_price': old_price, 'img': img_url}
