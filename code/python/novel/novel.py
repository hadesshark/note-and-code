#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-

import requests

headers = {
	'User-Agent':
	'Mozilla/5.0 (Windows NT 6.1) Chrome/44.0.2403.157 Safari/537.36'}

url = "http://ck101.com/thread-2462938-1-1.html"
request_get = requests.get(url, headers=headers)
print(request_get.text.encode('utf-8'))
