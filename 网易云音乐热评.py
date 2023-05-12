import requests
import random


def main():
    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    # 代理ip
    ips_list = ['61.216.185.88', '183.236.232.160',
                '182.139.110.15', '117.114.149.66', '112.14.47.6', '49.85.15.144']

    agent_ip = random.choice(ips_list)
    # print('ip', agent_ip)

    # 请求参数
    data = {
        'params': 'sduLvbGInNsB5CXGH8iWJG9obyHJmpU4rkbPkL1KS5OP2UiP6+YPYfTR+nRbixMA3gzhHk7NRHIyKR217NfxTp7f2BCBsnQdX7zI/vvy/FwRmQwxYIYAnp8YGhqHxMaV1i+HYMm5Wg5Pt+er/N2dHFk9MQStqEaxz/6dkJLl00iS3fak4DrsJurKfdZnJ7dpM268PgtjwV3o8blb4tUnNmmO3n5u6bAX/jRDiWunJHqFbFXg3IDxgnmJoxOgBjLbwmW9Vy6lysQoXITbZliZqrgsYn7/cqaorkP6jqncajQ=',
        'encSecKey': '2c556fb976f57f840a1d7f0aca1ee34f8b18240a99c37d894bd9bb455513c1be0ec7a9672be2f9ab06fd5809959ea692848b0ba221a52d78073dd16c6af4cf514d63feed4d63bdfa59a5fedf3555ad6ee9d49d596fdb54d03ba46b5ee8e78f97bba496552cdb8824390a2995e1eb79b7bf73feb938f3fb77b38828cb6e2aadb7'
    }

    resp = requests.post(url=url, headers=headers, proxies={
        'http': agent_ip}, data=data)

    print(resp.json())


if __name__ == '__main__':
    main()


"""
  data = {
      'csrf_token': "",
      'cursor': "-1",
      'offset': "0",
      'orderType': "1",
      'pageNo': "1",
      'pageSize': "20",
      'rid': "R_SO_4_1948480485",
      'threadId': "R_SO_4_1948480485"
    }

    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'
    i = 'n0pjvFt8CjFAAngu'

  # 加密
  var bMs8k = window.asrsea(JSON.stringify(i2x), bsi5n(["流泪", "强"]), bsi5n(Vx0x.md), bsi5n(["爱心", "女孩", "惊恐", "大笑"]));
            e2x.data = j2x.cr3x({
                params: bMs8k.encText,
                encSecKey: bMs8k.encSecKey
            })

  function a(a) {  # a = 16
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c # 返回16为随机数
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b) # 密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a) # e: 数据
          , f = CryptoJS.AES.encrypt(e, c, { # c: 加密密钥
            iv: d, # 偏移量
            mode: CryptoJS.mode.CBC # 模式: CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) { 
        # d: 请求实际参数 e: bsi5n(["流泪", "强"])  f: bsi5n(Vx0x.md) g: bsi5n(["爱心", "女孩", "惊恐", "大笑"])
        var h = {}
          , i = a(16); # i: 16位随机数
        return h.encText = b(d, g), # d: 参数 g: 定值
        h.encText = b(h.encText, i), # 参数中的params 
        h.encSecKey = c(i, e, f), # 参数中的encSecKey => i: 16位随机数  e: 定值 f: 定值
        h
    }
    function e(a, b, d, e) {  
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
"""
