#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

import requests
from lxml import etree


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

# print(page)
