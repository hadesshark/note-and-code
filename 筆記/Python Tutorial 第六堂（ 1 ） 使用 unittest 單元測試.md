# Python Tutorial 第六堂（ 1 ） 使用 unittest 單元測試

unittest 有時亦稱為「PyUnit」，是 JUnit 的 Python 語言實現， JUnit 是個單元測試（Unit test）框架，單元測試指的是測試一個工作單元（a unit of work）的行為。舉例來說，對於建築橋墩而言，一個螺絲釘、一根鋼筋、一條鋼索甚至一公斤的水泥等，都可謂是一個工作單元，驗證這些工作單元行為或功能（硬度、張力等）是否符合預期，方可確保最後橋墩安全無虞(ZOKD)。

測試一個單元，基本上要與其它的單元獨立，否則你會在同時測試兩個單元的正確性，或是兩個單元之間的合作行為。就軟體測試而言，單元測試通常指的是測試某個函式（或方法），你給予該函式某些輸入，預期該函式會產生某種出，例如傳回預期的值、產生預期的檔案、新增預期的資料等。

unittest 模組主要包括四個部份：

1. 測試案例
2. 測試設備
3. 測試套件
4. 測試執行器

## 測試案例

對於測試案例的撰寫， unittest 模組提供了一個基礎類別 TestCase ，你可以繼承它來建立新的測試案例。例如：

```python
import unittest
import calculator
 
class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)
 
    def tearDown(self):
        self.args = None
 
    def test_plus(self):
        expected = 5;
        result = calculator.plus(*self.args);
        self.assertEquals(expected, result);
 
    def test_minus(self):
        expected = 1;
        result = calculator.minus(*self.args)
        self.assertEquals(expected, result)
```

每個測試必須定義在一個 **test** 名稱為開頭的方法中，一個 TestCase 的子類別，通常用來為某個類別或模組的單元方法或函式定義測試。

## 測試設備

許多單元測試經常藬用相同的測試設備，你可以在 TestCase 的子類別中定義 setUp 與 tearDown 方法，測試執行器會在每個測試運行之前執行 setUp 方法，每個測試運行之後執行 tearDown 方法。

## 測試套件

根據測試的需求不同，你可能會想要將不同的測試組合在一起，例如， CalculatorTestCase 中可能有數個 test_xxx 方法，而你只想將 test_plus 與 test_minus 組裝為一個測試套件的話，可以如下：

```python
suite = unittest.TestSuite()
suite.addTest(CalculatorTestCase('test_plus'))
suite.addTest(CalculatorTestCase('test_minus'))
```

或者是使用一個 list 來定義要組裝的 test_xxx 方法清單：

```python
tests = ['test_plus', 'test_minus']
suite = unittest.TestSuite(map(CalculatorTestCase, tests))
```

如果想要自動載入某個 TestCase 子類別中所有 test_xxx 方法，可以如下：

```python
unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCase)
```

