这个人在写一个网站。网址sanfensum.cn  
不想拖别人的模板所以基本是自己边查边学边写（0前端基础），所以搞得很慢。  
  
截止到创建github库（11月13日）。他才写完了主页。  
目前在写博客界面，暂时没上数据库，想着先读取文件夹试试水。很庆幸我的尝试成功了。  
  
总之目前就这个鬼样子。

11-22日  
稍稍完善了一下blog界面，可以点击进入查看，使用了一个markdown的样式渲染    

11-24日  
我审美不足  

11-26日
终于是换上了数据库来储存，但是貌似又没有储存  
舍弃了nodejs转而用python做后端  

11-27日  
完善了水这个模块，感谢还蛮不错。  
但是发现了一个非常恐怖的事实——我的接口都是暴露的，别人一个for循环疯狂用我的接口注入数据库。我就直接爆了  
于是我暂时关掉了python-api  
又是个大活  

12-1日  
于是我觉定做个登录界面，只有登录了才能使用那些功能,正在开发中......  
顺便写了个插入什么的限制，防止被爆破  