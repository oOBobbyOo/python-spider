import requests


def main():
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        "Referer": url
    }

    resp = requests.post(url=url, headers=headers, timeout=10)

    resp.encoding = 'utf-8'

    result = resp.json()
    print(result)


if __name__ == "__main__":
    main()
