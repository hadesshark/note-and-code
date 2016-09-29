# Chain of Responsiblilty 模式

如果您有一個應用程式，必須對輸入的字元作不同的處理，例如：

```java
char c = 'A';
if (Character.isLetter(c)) {
   System.out.println("處理字母資料");
}
if (Character.isDigit(c)) {
   System.out.println("處理數字資料");
}

System.out.println("處理符號資料");
```

使用結構化的方式，用 `if..else` 來判斷是否應處理，雖然直覺，壞處是如果要調整處理方式，例如要增加或減少處理方式、調整處理順序等，都必須對程式作出修改。

您可以改為以下的方式：

```java
abstract class Handler {
    protected Handler next;
    Handler(Handler next) {
        this.next = next;
    }    
    void doNext(char c) {
        if(next != null) {
           next.handle(c);
        }
    }
    abstract void handle(char c);
}

class SymbolHandler extends Handler {
    SymbolHandler(Handler next) {
        super(next);
    }
    void handle(char c) {
        System.out.println("Symbol has been handled");
        doNext(c);
    }
}

class CharacterHandler extends Handler {
    CharacterHandler(Handler next) {
        super(next);
    }    
    void handle(char c) {
        if(Character.isLetter(c)) {
            System.out.println("Character has been handled"); 
        }
        doNext(c);
    }
}

class DigitHandler extends Handler {
    DigitHandler(Handler next) {
        super(next);
    }    
    void handle(char c) { 
       if(Character.isDigit(c)) {
            System.out.println("Digit has been handled"); 
       }
       doNext(c);
    }
}

public class Main {
    public static void main(String[] args) {
        Handler handler = new SymbolHandler(
                            new CharacterHandler(
                              new DigitHandler(null)));
        handler.handle('A');
        handler.handle('1');
    }
}
```

在上例中，在每個特定處理器物件處理過後，可以決定是否交給下一個物件作處理（如果有的話），您可以自由設定下一個處理器，調整處理的順序等，而不用條改程式。

這是 Chain of Responsibility 模式的一個例子，多個物件都有機會理請求，除了可以自由組合處理請求的物件之外，也可以避免請求的發送者與接收者之間的耦合關係，將這些物件組合為一個鏈，並沿著這個鏈傳遞該請求，每個都可以物件處理它，決定是否傳遞給下一個處理物件。

以下是使用 Python 示範：

```python
class Handler:
    def __init__(self, next):
        self.next = next;
    def doNext(self, c):
        if self.next:
            self.next.handle(c)

class SymbolHandler(Handler):
    def __init__(self, next):
        Handler.__init__(self, next)
        
    def handle(self, c):
        print("Symbol has been handled")
        self.doNext(c)

class CharacterHandler(Handler):
    def __init__(self, next):
        Handler.__init__(self, next)
        
    def handle(self, c):
        if c.isalpha():
            print("Character has been handled")
        self.doNext(c)        

class DigitHandler(Handler):
    def __init__(self, next):
        Handler.__init__(self, next)
        
    def handle(self, c):
        if c.isdigit():
            print("Digit has been handled")
        self.doNext(c)        

handler = SymbolHandler(CharacterHandler(DigitHandler(None)))
handler.handle('A')
handler.handle('1')
```

在組織物件之間的職責時，通常是從細粒度至粗粒度的方式來組織，從特殊到抽象化，就像程式中將數字視為字元的特殊化，字元又為符號的特殊化。

Chain of Responsibility 的 UML 結構圖如下所示：

![](ChainOfResponsibility-1.jpg)

從物件執行請求的時間來看，其運作是很簡單的職責傳遞而已，如下：

![](ChainOfResponsibility-2.jpg)

在更一般的情況下，可以將請求包裝為一個物件，並提供 getType() 之間的方法，以讓 Chain of Responsibility 中的物件進行比對，例如：

* Request.java

```java
abstract class Request{ 
　　private String type; 

    Request(String type) { this.type=type; }
    String getType() { return type; }

    abstract void execute();
} 

abstract class Handler {
    protected Handler next;
    Handler(Handler next) {
        this.next = next;
    }    
    void doNext(Request request) {
        if(next != null) {
           next.handle(request);
        }
    }
    abstract void handle(Request request);
}

class ConcreteHandler extends Handler {
    ConcreteHandler(Handler next) {
        super(next);
    }
    void handle(Request request) {
        if(request.getType().equals("concrete")) {
            request.execute();
        }
        else {
            doNext(request);
        }
    }
}
```

在 GoF 的書中所舉的例子為輔助說明系統，在一個介面中希望使用者一定可以得到相關的說明主題，如果子元件有說明的話，就顯示相關說明，否則的話就轉發給包括它的容器元件或父元件，以保證使用者的輔助說明請求一定可以得到回應。