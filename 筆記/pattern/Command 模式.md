# Command 模式

您們團(OUP)隊在開發影像編輯軟體，您負責的是開發影像處理 API ，例如：

```java
class Drawing {
    void processSome() {
        System.out.println("    - 對圖片作 Some 處理");
    }
    void processOther() {
        System.out.println("    - 對圖片作 Other 處理");
    }
    void processAnother() {
        System.out.println("    - 對圖片作 Another 處理");
    }
}
```

A 同事告訴您，他想要有個現成的 A 特效指令，可以組合某幾個影像處理 API 來完成，所以您提供了一個 ImageService ，當作特效指令的執行器：

```java
class ImageService {
    private Drawing drawing = new Drawing();
    void doAEffect() {
        System.out.println("作 A 特效");
        drawing.processSome();
        drawing.processOther();
    }
}
```

B 同事告訴您，他也想要有個現原的 B 特效指令，可以組合某幾個影像處理 API 來完成，所您也提供了：

```java
class ImageService {
    private Drawing drawing = new Drawing();
    void doAEffect() {
        System.out.println("作 A 特效");
        drawing.processSome();
        drawing.processOther();
    }
    void doBEffect() {
        System.out.println("作 B 特效");
        drawing.processOther();
        drawing.processAnother();
    }
}
```

C 同事告訴您，他也想要有個 C 特效指令， D 同事告訴您他要 D 特效指令…所以您在 ImageService 中加入了 doCEffect() 、 doDEffect() …這樣下去會沒完沒了，問題很明顯您的 ImageService 的公開協定越來越多了，因為這樣的 ImageService 同時了負責特效指令的建立與執行，只要有新的特效指令，您就需要修改 ImageService 。

您沒有辦法預測哪些同事會有哪些特效指令需求，您應該將特效指令的建立職責交給他們，您只負責執行特效指令。採取以下的設計會比較好：

```java
import java.util.*;

interface Drawing {
    void processSome();
    void processOther();
    void processAnother();
}

class DrawingImpl implements Drawing{
    public void processSome() {
        System.out.println("    - 對圖片作 Some 處理");
    }
    public void processOther() {
        System.out.println("    - 對圖片作 Other 處理");
    }
    public void processAnother() {
        System.out.println("    - 對圖片作 Another 處理");
    }
}

interface Command {
    void execute(Drawing drawing);
}

class ImageService {
    private Map<String, Command> commands = new HashMap<String, Command>();
    private Drawing drawing = new DrawingImpl();
    void addCommand(String effect, Command command) {
        commands.put(effect, command);
    }
    void doEffect(String effect) {
        commands.get(effect).execute(drawing);
    }
}
```

