#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*

import requests
from lxml import etree


headers = {
	'User-Agent':
	'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}

url = "http://www.jianshu.com/p/1f90e12e663f"
request_get = requests.get(url, headers=headers)
page = request_get.text.encode("Utf-8")

# print(page)

etree_page = etree.HTML(page)
__xpath_for_article = u"//div[@class='article']"

temp_article = etree_page.xpath(__xpath_for_article)
# print(temp_article)

__xpath_for_title = u"//h1[@class='title']//text()"
temp_title = etree_page.xpath(__xpath_for_title)
print(temp_title)

__xpath_for_content = u"//div[@class='show-content']//text()"
temp_content = etree_page.xpath(__xpath_for_content)
# print(temp_content)

content_add_space = ''
for item in temp_content:
    content_add_space += item + '\n'

f = open("novel_file/test.txt", "wb")
f.write(content_add_space.encode("utf-8"))
f.close()
