import requests
import re
import csv
import os
import time


def get_top250():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

   # 代理ip
    agent_ip = '61.216.185.88'

    # 编写正则表达式
    regex = re.compile(
        r'<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?<p class="">.*?导演: (?P<diretor>.*?)&nbsp;.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<average>.*?)</span>.*?<span class="inq">(?P<quote>.*?)</span>', re.S)

    # 判断路径是否存在
    base_path = './douban'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    # 文件名
    filename = 'top250.csv'

    f = open(os.path.join(base_path, filename), 'w', encoding='utf-8')

    # csv写入
    csvwriter = csv.writer(f)

    for i in range(0, 250, 25):
        print(f'正在爬取第{i}页')
        url = f'https://movie.douban.com/top250?start={i}'
        # print(url)

        time.sleep(2)

        resp = requests.get(url=url, headers=headers,
                            proxies={'http': agent_ip})
        # 解决页面乱码问题
        resp.encoding = 'utf-8'
        page_text = resp.text

        # 进行正则匹配
        result = regex.finditer(page_text)

        for item in result:
            dic = item.groupdict()
            dic['year'] = dic['year'].strip()

            csvwriter.writerow(dic.values())

        # for item in result:
        #     title = item.group('title')
        #     diretor = item.group('diretor')
        #     year = item.group('year').strip()
        #     average = item.group('average')
        #     quote = item.group('quote')
        #     # print(title, diretor, year, average, quote)
        #     f.write(f'{title}, {diretor}, {year}, {average}, {quote}\n')
        #     print(f'{title}写入成功')

        # 关闭
        resp.close()

    f.close()
    print('豆瓣top250提取完毕!!!')


if __name__ == '__main__':
    get_top250()
