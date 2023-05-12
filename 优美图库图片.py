import requests
import random
import time
import os
from bs4 import BeautifulSoup


def main():
    domain = 'https://www.umei.cc'
    url = 'https://www.umei.cc/bizhitupian/xiaoqingxinbizhi'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    # 代理ip
    ips_list = ['61.216.185.88', '183.236.232.160',
                '182.139.110.15', '117.114.149.66', '112.14.47.6', '49.85.15.144']

    agent_ip = random.choice(ips_list)
    print('ip', agent_ip)

    resp = requests.get(url=url, headers=headers, proxies={
                        'http': agent_ip})
    resp.encoding = 'utf-8'
    page_text = resp.text
    # print(page_text)

    main_page = BeautifulSoup(page_text, 'html.parser')
    # print(main_page.prettify())

    a_list = main_page.find_all('a', attrs={'class': 'img_album_btn'})

    # 判断路径是否存在
    base_path = './umei/big-pic'
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for a in a_list:
        href = a.get('href')
        # print(href)
        child_url = domain + href

        time.sleep(2)

        child_resp = requests.get(
            url=child_url, headers=headers, proxies={'http': agent_ip})
        child_resp.encoding = 'utf-8'
        child_text = child_resp.text

        child_page = BeautifulSoup(child_text, 'html.parser')
        div = child_page.find('div', attrs={'class': 'big-pic'})
        img_src = div.find('img').get('src')
        # print(img_src)

        img_data = requests.get(url=img_src, headers=headers).content
        img_path = base_path + '/' + img_src.split('/')[-1]

        with open(img_path, 'wb') as f:
            f.write(img_data)
            print(f'{img_path} 下载成功')


if __name__ == '__main__':
    main()
