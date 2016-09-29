# JavaScript 生態圈現狀：初學者地圖

http://www.infoq.com/cn/articles/state-of-javascript-2016?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global

縱覽當前的「JavaScript 生態圈」。這應該足夠你找淮方向，開啟前端開發之旅。

## 客戶端 JavaScript 是如何工作的，為什麼要使用它？

為了編寫高效的前端代碼，你需要對如何綜合運用 HTML 、 CSS 和 JavaScript 創建 Web 頁面有一個基本的了解。

當**客戶端**（通常是**瀏覽器**）訪問 HTML 頁面時，它會下載它，解析它，然後使用它構造 **DOM** （文檔對象模型）。 JavaScript 可以同 DOM 交互及修改 DOM ，**交互式**站點就是這樣創建的。

JavaScript 是如何包含到頁面中的？那是另一個複雜的問題，但它是以 script 標簽開始的。

JavaScript 的執行會阻塞 DOM 構造。這就是說，執行 JavaScript 的時間過長會讓人覺得頁面沒響應。客戶端 JavaScript 經常都是大量使用**異步**。

## 框架是什麼？我需要使用 trendy.js 嗎？

JavaScript 框架的目標通常是減少構建交互式 Web 頁面過程中無謂的工作。從根本上說，框架就是腳手架，設計用來解決一個特定種類的問題。

那麼該用哪個框架呢？ React ？ Angular ？ 還是 Ember ？ 甚至說你需要框架嗎？ 選擇麻痹症的信號！對於選擇哪個框架，沒有正確的答案，如果有，你就應該使用。

## 我應該編寫 JavaScript ，還是其他的什麼？ JavaScript 的種類有哪些？

如果你是前端開發初學者，那麼你也許應該編寫 ES6 風格的 JavaScript。

## 如何使用其他人的代碼？

在工作中，你很可能會遇到所有這三種類型的模塊。對於新項目，你應該使用 ES6 原生模塊。構建工具，如 webpack （下面會介紹），會幫助你在現有項目中使用各種類型的模塊。

## 我需要 Node.js 嗎？

...

## 我該用什麼構建工具？

大多類站點都使用所謂的 JavaScript **bundles**。對於新項目，我推薦(KF) **webpack**。

## 我如何測試代碼？

Mocha 和 Jasmine 是兩個流行的庫，有時候稱為**測試框架**，可以幫助你編寫測試。