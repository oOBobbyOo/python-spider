import requests
from lxml import etree
import re
import time


def main():
    url = 'https://www.dygod.net'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    # 代理ip
    agent_ip = '61.216.185.88'

    resp = requests.get(url=url, headers=headers, proxies={'http': agent_ip})
    # 解决页面乱码问题
    resp.encoding = 'gbk'
    page_text = resp.text
    # print(page_text)

    # 解析页面
    tree = etree.HTML(page_text)

    # 过滤掉第一条问题数据
    li_list = tree.xpath('//div[@class="co_content222"]//li')[1:]

    # 编写正则表达式
    regex = re.compile(
        r'<div id="Zoom">.*?◎译　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_url>.*?)">', re.S)

    for li in li_list:
        child_url = li.xpath('./a/@href')[0]
        detail_url = url + child_url
        # print(detail_url)

        time.sleep(1)

        # 获取detail页面的内容
        resp2 = requests.get(detail_url, headers=headers,
                             proxies={'http': agent_ip})

        # 解决页面乱码问题
        resp2.encoding = 'gbk'
        child_page_text = resp2.text

        # 进行正则匹配
        result = regex.finditer(child_page_text)

        for item in result:
            name = item.group('name')
            download_url = item.group('download_url')
            print(name, download_url)


if __name__ == '__main__':
    main()
