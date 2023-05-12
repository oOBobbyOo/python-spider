import json
import requests

# 快代理： https://www.kuaidaili.com/free/inha/1/


def main():
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    # 代理ip
    agent_ip = '117.93.180.175'

    response = requests.get(url=url, headers=headers,
                            proxies={'http': agent_ip})

    response.encoding = 'utf-8'
    html = response.text
    print(html)

    with open('./ip.html', 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    main()
