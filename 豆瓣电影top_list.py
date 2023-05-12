import requests
import json
import os


def main():
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    params = {
        'type': 5,
        'interval_id': '100:90',
        'action': '',
        'start': 0,
        'limit': 20,
    }

    resp = requests.get(url=url, headers=headers, params=params)
    resp.encoding = 'utf-8'
    top_list = resp.json()

    # 判断路径是否存在
    base_path = './douban'
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    filename = 'top_list.json'

    fp = open(os.path.join(base_path, filename), 'w', encoding='utf-8')
    json.dump(top_list, fp=fp, indent=4, ensure_ascii=False)
    fp.close()
    print('豆瓣top_list提取完毕~~~~')


if __name__ == '__main__':
    main()
