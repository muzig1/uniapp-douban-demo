#!/bin/env python3
# coding=utf-8

from bs4 import BeautifulSoup
import pprint
import util

soup = BeautifulSoup(open('index.html', 'r'), 'lxml')

collector = []
for tag in soup.find_all('a'):
    c = tag.get('class')
    if c is None or "item" not in c:
        continue
    target = tag.get('target')
    if target is None or "_blank" not in target:
        continue
    img = tag.find('img')
    if img is None:
        continue
    span = tag.find('span')
    if span is None or 'episodes-info' not in span.get('class'):
        continue
    # 获取基本信息
    data = {
        "title": img.get('alt'),
        "img": img.get('src'),
        "blues": span.string
    }
    # 获取分数
    strong = tag.find('strong')
    if strong is not None:
        data['score'] = float(strong.string)
    else:
        data['score'] = 0
    collector.append(data)

# pprint.pprint(collector)

with open(util.get_static_path()+'/hot_teleplay.json', 'w') as f:
    f.write(collector.__str__().replace('\'','\"'))
