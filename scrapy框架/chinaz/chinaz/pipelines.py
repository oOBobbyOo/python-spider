# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ChinazPipeline:

    def open_spider(self, spider):
        self.f = open('./图片.csv', mode='w', encoding='utf-8')
        print('爬虫开始')

    def process_item(self, item, spider):
        print(f'{item["img_name"]}')

        # 写入csv文件中
        self.f.write(f'{item["img_name"]},{item["img_url"]}\n')

        return item

    def close_spider(self, spider):
        if self.f:
            self.f.close()
        print('爬虫结束')


class MeinvSavePipeline(ImagesPipeline):  # 使用图片管道帮我们完成数据下载工作

    def get_media_requests(self, item, info):  # 负责请求下载
        return scrapy.Request(item['img_url'])

    def file_path(self, request, response=None, info=None, *, item=None):  # 负责准备文件路径
        file_name = request.url.split('/')[-1]
        return f'img/{file_name}'

    def item_completed(self, results, item, info):  # 返回文件的详细信息
        # print(results)
        # ok, fileinfo = results[0] # ok: 是否成功，fileinfo:文件信息
        # fileinfo['path'] # 图片下载路径

        return item  # 返回给下一个管道类进行处理
