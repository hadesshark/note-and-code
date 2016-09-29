#Python 對 Lambda/Closure 的支援

在Python 中可以使用 def 定義函式。每個函式都是 function 的實例，所以可以指定給其他變數。例如：

```python
def max(m, n):
    return m if m > n else n

print(max(10, 3)) # print 10
maximum = max
print(maximum(10, 3)) # print 10
```

如果要在 Python 中建立匿名函式，可以使用 lambda 運算式。例如：

```python
max = lambda m, n: m if m > n else n
print(max(10, 3)) # print 10
```

不同的語言在支援函式或 Lambda 時提供不同的語法。Python 簡明的語法顯然在表達函式上，優於 JavaScript 。在以下的對比中，你可以明顯看出者在表達函式上的差異性：

```javascript
// 定義函式：JavaScript
function max(n, n) {
  return m > n ? m: n;
}
```

```python
# 定義函式：Python
def max(m, n):
    return m if m > n else n
```

```javascript
// 建立匿名函式：JavaScript
function(n, n) {
  return m > n ? m:n;
}
```

```python
# 建立匿名函式：Python
lambda m, n: m if m > n else n
```

來看看另一個運用 Lambda/Closure 的例子。如果你的函式運用了某個耗時的資源，通常可以考慮將運算的結果加以重用，這是效能調整上的一個考量。方法之一個建立全域資源，並在函式中加以運用。然而，全域資源不是個好的方式。我們可以在函式中準備資源，建立一個 Closure 捕捉他，然後從函式中傳回 Closure 。例如：

```python
import math
def prepare_factor(max):
    # Creating a prime table is time-consuming.
    primes = [i for i in range(2, max) if prime[i] == 1]
    
    def factor(num):
        while primes[i] ** 2 <= num:
            if num % primes[i] == 0:
                list.append(primes[i])
                num //= primes[i]
            else:
                i += 1
	return factor

factor = prepare_factor(1000)
print(factor(100)) # print [2, 2, 5, 5]
```

在上例中，內部函式 factor 建立了 Closure 捕捉了外部函式的 primes 變數。因為函式是物件，你可以從函式中傳回他。primes 變數的生命週期現在跟隨著被傳回的函式。我們沒有將 primes 變數放在全域範圍，但仍可以重用資源。到目前為止你可以看到，如果函式是物件，那麼就可以：

* 被位何變數參考。
* 不只是被動地被呼叫，還可以主動地傳入函式中，取代某個可重用流程模版中的演算法。
* 建立 Closure 捕捉閒變數（Free varialbe）並從函式中傳回。

不過，Python 的 Closure 有個重大的限制。你沒辦法對閒置變數設值。也就是說，在 Python 中，Closure 捕捉的閒置變數是唯讀的。例如：

```python
def func():
    x =10
    def getX():
        return x
    def setX(n):
        x = n # 建立區域變數 x
    return (getX, setX)

getX, setX = func()
getX() # 10

setX(20)
getX(10) # still 10
```

在 Python 中，首次對變數設值時就等同於建立新的區域變數。在上例中，如果呼叫 setX ，事實上會在 setX 中建立區域變數 x ，而不是將參數 n 指定給 func 的區域變數。這就是為何你最後會得到 10 的原因。

幸運地，在 Python 3 中，可以使用 global 或 nonlocal 關鍵字來明確指定數數的範圍，以避免這類情況。例如：

```python
def func():
    x = 10
    def getX():
        return x
    def setX(n):
        nonlocal x = n
    return (gegX, setX)

getX, setX = func()
getX() # 10

setX(20)
getX(10) # 20
```

在上例中，nonlocal 關鍵字表示 x 不會是區域變數。Python 直譯器會看看外部函式，並瞭解到 x 是從 func 的區域變數 x 捕捉而來。這次再呼叫 setX ，改變的值確實就是 func 中區域變數 x 的值了。

我們已經看過 JavaScript 與 Python 對 Lambda/Closure 的支援方式。他們都是動態語言。如果使用的是靜態語言，從中瞭解一些經驗似乎是個不錯的方式。這也是下一篇文章要看的內容，我們會來看看 Scala 如何支援 Lambda/Closure 。