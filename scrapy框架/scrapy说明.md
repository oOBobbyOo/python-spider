1.  创建项目  
    scrapy startprojesct 项目名称

2.  进入项目目录  
    cd 项目名称

3.  创建爬虫

    - scrapy genspider example(爬虫名称) example.com(域名)

    - scrapy genspider -t crawl example(爬虫名称) example.com(域名)

4.  可能需要修改 start_urls, 修改成你要抓取的那个页面 url

5.  对数据进行解析，在 spiders 里面的 parse(self, response) 方法中进行解析  
    def parse(self, response):  
    esponse.text 拿到页面源码  
    response.xpath() 使用 xpath 解析  
    response.css() 使用 css 选择器解析

    解析数据的时候，需要注意，默认 xpath()返回的 Selector 对象  
    想要数据必须使用 extract() 提取数据  
    extract() 返回列表  
    extract_first() 返回第一个数据

    定义规范数据格式:  
    在 items.py 中定义 key: scrapy.Field()

    在 spiders 导入 在 items.py 定义的类  
    创建一个新的 item 对象  
    item = XxxItem()  
    item[key] = value

    yeild item -> 把数据交给 pipeline 管道进行持久化存储

6.  在 pipelines.py 中做数据处理, 完成数据的持久化存储  
    def process_item(self, item, spider):  
    item: 数据  
    spider: 爬虫  
    return item # 必须 return item, 否则下个管道接收不到数据

    数据的存储方案：

    - 数据存储在 csv 文件中
    - 数据存储在数据库中（mysql、mongodb）
    - 文件的存储

7.  设置 setings.py 文件中将 pipeline 进行生效设置  
    ITEM_PIPELINES = {  
     '管道路径'：优先级， 值越小，优先级越高  
    }

8.  运行爬虫  
    scrapy crawl 爬虫名字
