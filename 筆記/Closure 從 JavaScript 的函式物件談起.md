#認識 Lambda/Closure 從 JavaScript 的函式物件談起

根據維基百科對 Lamdba 條目的說明：「在諸如 Lisp 、Python 的語言中，Lambda 是代表匿名函數（Anonymous）或閉包（Closure）的運算子。」

JDK8 中即將支援 Lambda 語法，那麼 Lambda 是什麼？該怎麼用？ Lambda/Closure 在 Java 語言中一直不存在，因而對於 Java 開發者來說是陌生的。實際上，Lambda/Closure 早存在許多程式語言之中，對於尚不熟悉 Lambda/Closure 的 Java 開發者來而，可試著從其他具備 Lambda/Closure 的語言中，瞭解其概念及運用方式。

以現今許多開發者較熟悉的 JavaScript 為例。在 JavaScript 中可以如下定義函式：

```javascript
function doSome(param) {
  // dosomting
}
```

然而實際上在 JavaScript 中，函式是個物件，也可以如下建立一個函式物件，並指定給 doSome 變數：

```javascript
var doSome = function(param) {
  // dosomting
};
```

粗體定部份在 JavaScript 中稱為一個函式實字（Function literal），它會建立一個 Funciton 的實例。你也可以不將函式物件指定給變數，這就形式了一個匿名函式：

```javascript
function(param) {
  // dosomting
};
```

如果不考慮一些細節差異性，上面的函式實字建立的函式實例，相當於使用 `new Function('param', '函式本體') `。這強調了函式本身是個物件，也就是個值的概念。即然函式是物件，那麼可以作什麼？它可以指定給別的變數：

```javascript
function foo(param) {
  document.write(param, '<br>');
}
var zzz = foo;
zzz('demo');
```

上面這個程式片段跟以下是相同的（精確地說，是類似的）：

```javascript
var foo = function(param) {
  document.write(param, '<br>');
};
var zzz = foo;
zzz('demo');
```

既然可以指定給別的變數，就可以作為引數傳入函式中：

```javascript
function show(element) {
  document.write(element, '<br>'); 
}
[1, 2, 3, 4, 5].forEach(show);
```

上面這個程式片段與以下是相同的（或說是類似的）：

```javascript
var show = function(element) {
  document.write(element, '<br>');
};
[1, 2, 3, 4, 5].forEach(show);
```

瞭解一個程式語言的概念時，不僅是從語法來學習，更要定它的文化與風格來深入。舉例而言，如果你只是用 Java 的慣例，來寫 JavaScript 的陳列元素走訪的話，可能會寫出以下風格的程式碼：

```javascript
var array = [1, 2, 3, 4, 5];
for(var i = 0; i < array.length; i++) {
  document.write(array[i] + '<br>');
}
```

然而如果以 JavaScript 的慣例與風格來寫，可以如下走訪列元素：

```javascript
[1, 2, 3, 4 ,5].forEach(function(element) {
  document.write(element + '<br>');
});
```

從語言的文化、慣例與風格來瞭解與運用語法元素，你就可以更清楚地瞭解，像 Lambda/Closure 這類元素，該運用在何種場合。

既然函式可以作為引數傳入函式，那就可以設計回呼（Callback）函式。例如，如果你的瀏覽器或 JavaScript 客戶端沒有支援陳列的 forEach 函式，那可以自行設計：

```Javascript
Array.prototype.forEach = function(callback) {
  for(var i = 0; i < this.length; i++) {
  	callback(this[i]);
  }
};

[1, 2, 3, 4, 5].forEach(function(element) {
  document.write(element + '<br>');
});
```

從以上可知，當函式是物件，你就可以…

* 根據需要將之傳遞給另一個變數參考。
* 函式不再只能被呼叫，而可以主動傳遞給別的函式進行動作。
* 流程中不同的演算需求，可以設計回呼函式來抽換。

也就是，當函式是物件時，不但可以簡化語法，還可以有更多不同的設計方式，開放各種程式設計的可能性。

以上我們從 JavaScript 認識了匿名函式、函式是物件的概念，至於它為什麼叫 Lambda ，這要到比較後面才會提到。下一篇文章，則會先從什麼是 Closure 開始認識。