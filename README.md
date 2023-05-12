# Python 爬虫

## Robots 协议

robots 协议也称爬虫协议、爬虫规则等,是指网站可建立一个 robots.txt 文件来告诉搜索引擎哪些页面可以抓取,哪些页面不能抓取,而搜索引擎则通过读取 robots.txt 文件来识别这个页面是否允许被抓取。

```
禁止所有机器人访问
User-agent: *
Disallow: /

允许所有机器人访问
User-agent: *
Disallow:

禁止特定机器人访问
User-agent: BadBot
Disallow: /

允许特定机器人访问
User-agent: GoodBot
Disallow:

禁止访问特定目录
User-agent: *
Disallow: /images/
Disallow: /private/

禁止所有机器人访问特定文件类型
User-agent: *
Disallow: /*.html$
Disallow: /*.php$
Disallow: /*.js$
Disallow: /*.inc$
Disallow: /*.css$

```
