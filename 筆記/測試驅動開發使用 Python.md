# 測試驅動開發使用 Python

## 第一部分 TDD 與 Django 基礎知識

### 第一章 設定 Django ，使用功能測試

~~~python
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
~~~



> 第一章整體來說，就是後半段的 `functional_test.py` 加入資料夾之後使用 `git` 來做記錄。最有趣的就是兩個 `git` 沒有干擾，非常神奇。



### 第二章 以 unittest 模組擴充功能測試

> 功能測試 == 接受度測試 == 雙端測試

~~~python
Traceback (most recent call last):
  File "functional_test.py", line 3, in <module>
    browser = webdriver.Firefox()
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/firefox/webdriver.py", line 80, in __init__
    self.binary, timeout)
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/firefox/extension_connection.py", line 52, in __init__
    self.binary.launch_browser(self.profile, timeout=timeout)
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/firefox/firefox_binary.py", line 68, in launch_browser
    self._wait_until_connectable(timeout=timeout)
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/firefox/firefox_binary.py", line 99, in _wait_until_connectable
    "The browser appears to have exited "
selenium.common.exceptions.WebDriverException: Message: The browser appears to have exited before we could connect. If you specified a log_file in the FirefoxBinary constructor, check it for details.
~~~

> 上面的內容可以知道，程式對於 url 的輸入產生問題了。



> 用 chrome driver 在 mac 上無法成功顯示視窗



> 經過測試要照以下步驟：
>
> 1. 先更新 selenium
> 2. 下載 geckodriver
> 3. 把 2. 的文件解壓縮後放到和 python 一樣的位置



### 第三章 使用單元測試，來測試簡單的首頁

> 不清楚為什麼要加入一個 lists 書上的說法完全看不懂。



```python
Creating test database for alias 'default'...
E
======================================================================
ERROR: test_root_url_resolves_to_home_page_view (lists.tests.HomePageTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/hadesshark/note-and-code/code/python/TDD/superlists/lists/tests.py", line 8, in test_root_url_resolves_to_home_page_view
    found = resolve('/')
  File "/usr/local/lib/python3.5/site-packages/django/core/urlresolvers.py", line 522, in resolve
    return get_resolver(urlconf).resolve(path)
  File "/usr/local/lib/python3.5/site-packages/django/core/urlresolvers.py", line 388, in resolve
    raise Resolver404({'tried': tried, 'path': new_path})
django.core.urlresolvers.Resolver404: {'tried': [[<RegexURLResolver <RegexURLPattern list> (admin:admin) ^admin/>]], 'path': ''}

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (errors=1)
Destroying test database for alias 'default'...
```



>  原本想用 `>> info.txt` 這樣的方法來輸出結果，但無法把全部的錯誤訊息寫入。



> 第三章結束，主要就是建立一個簡單的 html 畫面。



### 第四章 我們用這些測試來做什麼？

~~~python
'NoneType' object has no attribute 'path'
E
======================================================================
ERROR: test_can_start_a_list_and_retriveve_it_later (__main__.NewVisitorTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "functional_test.py", line 21, in test_can_start_a_list_and_retriveve_it_later
    header_text = self.browser.find_element_by_tag_name('h1').text
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 389, in find_element_by_tag_name
    return self.find_element(by=By.TAG_NAME, value=name)
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 752, in find_element
    'value': value})['value']
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 236, in execute
    self.error_handler.check_response(response)
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 192, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: h1
~~~



> 錯誤雖然不是和書上一樣，但表達的內容是一樣的。



> 最後增加 functional 結束這一章。



### 第五章 保存使用輸入的資料

> p58 的錯誤訊息還是有問題。

> 這一章開始有很多測試和書上不同（像是書上顯示錯誤，但執行後卻是正確），很有可能是版本問題，但又怕修改回原版本， firefox 又出現問題。



### 第六章 完成最低可行的網站





## 第二部分 網頁程式開發的必備條件

### 第七章 修飾：版面配置與樣式設計，以及用什麼測試它





### 第八章 使用預備網站來測試部署





### 第九章 使用 Fabric 來自動部署





### 第十章 輸入驗與測試組織





### 第十一章 簡單的表單





### 第十二章 進階的表單





### 第十三章 小心翼翼地把我們的腳趾放入 JavaScript





### 第十四章 部署我們的新程式





## 第三部分 要進階的主題

### 第十五章 使用者驗證、整合第三方外掛與模仿 JavaScript





### 第十六章 使用 Python 進行伺服器端驗證與 Mock





### 第十七章 測試 fixture 、登入與伺服器除錯





### 第十八章 完成“MyLists“：由外而內的 TDD





### 第十九章 測試隔離與“聆聽你的測試“





### 第二十章 持續整合（CI）





### 第二十一章 社交、Page 模式，與給讀者的練習





### 第二十二章 快速測試、慢速測試與熟熔岩





