# Introducing HTML 5 Game Development

Making video games is hard work that requires technical skills, a lot of planning, and--most critically--a commitment to completing the project. With this hands-on guide, you'll learn step-by-step how to create a real 2D game from start to finish. In the process, you'll use Impact, the JavaScript game framework that works with HTML5's Canvas element.

Not only will you pick up important tips about game design, you'll also learn how to publish Impact games to the Web, desktop, and mobile--including a method to package your game as a native IOS app. Packed with screenshots and sample code, this book is ideal for game developers of all levels.

* Set up your development environment and discover Lmpact's advantages
* Build a complete game with core logic, collision detection, and player and monster behavior
* Learn why a game design document is critical before you start building
* Display and animate game art work with sprite sheets
* Add sound effects, background music, and text
* Create screens to display starts and in-game status
* Prepare to publish by baking your game files into a single file

Purchase the ebook edition of this O'Reilly title at oreilly.com and get free updates for the life of the edition. Our ebooks are optimized for several electronic formats, including PDF, EPUB, Mobi, APK, and DAISY--all  DRM-free.

## CHAPTER 1 Introduction To Impact

Impact is a JavaScript game framework created by Dominic Szablewski. Impact takes advantage of the modern browser's Canvas element in order to create high-performance 2D games on the Web and even mobile. One of the biggest advantages of using Impact is that it it is easy to pick up, comes with very good code examples, has an active com-munity, and has a very robust level editor called Weltmeister. The only barrier of entry is the licensing fee for the software, since it is not open surce. After purchasing a license, you do get the full source code, the Weltmeister level  editor, and free current major version updates (1,x). While there are other open source and free JavaScript game frameworks out there, Impact has an extra level of polish I haven't seen with anything else so far.

### Setting Up a Local Environment

Before getting started, we are going to have to set up a simple Web development environment in order to take full advantage of Impact and its level editor. Plus, by setting up a local development environment, we can simulate what it will be like to host the game in a production environment. Let's take a look at configuring Apacke, the IDE, and Impact itself.

### Install WebStorm/PHPStorm

While you can use any basic text editor, I prefer to use an IDE that offers a more robust set of features such as code hinting, refactoring, project management, version control integration, and a debugger. JetBrains has two IDEs that both handle JavaScript/HTML5 development. If you only plan on doing JavaScript development, I would suggest using WebStorm. If you need to do HTML5 and PHP development (which comes in handy since Impact's level editor uses PHP) you should look at PHPStorm.

Installing these applications is straightforward. Here are URLs for each IDE:

WebStorm
​	[http://www.jetbrains.com/webstiorm](http://www.jetbrains.com/webstiorm)

PHPStorm
​	[http://www.jetbrains.com/phpstorm](http://www.jetbrains.com/phpstorm)

