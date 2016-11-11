from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

asert 'Django' in browser.title
