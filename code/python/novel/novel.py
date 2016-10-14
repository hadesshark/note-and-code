#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import os


headers = {
	'User-Agent':
	'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}

url = "http://ck101.com/thread-2462938-1-1.html"
request_get = requests.get(url, headers=headers)
page = request_get.text.encode("Utf-8")

if request_get.status_code == 200:
	print("Tree")
else:
	print("False")

#================================

with open("test.htm", "rb") as f:
	html_unline_data = f.read()

etree_page = etree.HTML(html_unline_data.decode("utf-8"))
__xpath_for_next_url = u"//div[@class='pg']/a[@class='nxt']/@href"
temp_next_url = etree_page.xpath(__xpath_for_next_url)
print(temp_next_url)
