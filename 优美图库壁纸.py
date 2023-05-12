import requests
from lxml import etree
import os


def main():
    url = 'https://www.umei.cc/bizhitupian/diannaobizhi/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers)
    resp.encoding = 'utf-8'
    page_text = resp.text
    # print(page_text)

    tree = etree.HTML(page_text)
    a_list = tree.xpath('//*[@id="infinite_scroll"]//div[@class="img"]/a')
    # print(a_list, len(a_list))

    # 判断路径是否存在
    base_path = './umei/thump-pic'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for a in a_list:
        img_title = a.xpath('./img/@alt')[0]
        img_url = a.xpath('./img/@data-original')[0]
        # print(img_title, img_url)
        img_path = base_path + '/' + img_url.split('/')[-1]
        # print(img_path)
        img_data = requests.get(url=img_url, headers=headers).content

        with open(img_path, 'wb') as f:
            f.write(img_data)
            print(f'{img_title} 下载成功')


if __name__ == '__main__':
    main()
