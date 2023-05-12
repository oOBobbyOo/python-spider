from urllib import request
import gzip
import re


class Spider():
    url = 'https://www.huya.com/g/2793'
    root_pattern = '<li class="game-live-item" .*?>([\s\S]*?)</li>'
    name_pattern = '<i class="nick" .*?>([\s\S]*?)</i>'
    num_pattern = '<i class="js-num">([\s\S]*?)</i>'

    def __fetch_contents(self):
        response = request.urlopen(Spider.url)
        # htmls = gzip.GzipFile(fileobj=response).read()
        # htmls = str(htmls, encoding="utf-8")

        if ('Content-Encoding', 'gzip') in response.headers._headers:
            content = response.read()
            htmls = gzip.decompress(content).decode('utf-8')
        else:
            htmls = response.read().decode('utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            num = re.findall(Spider.num_pattern, html)
            anchors.append({'name': name[0], 'num': num[0]})
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'].strip(), 'num': anchor['num']}
        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_by, reverse=True)
        return anchors

    def __sort_by(self, anchor):
        r = re.findall(r'\d+', anchor['num'])
        num = float(r[0])
        if '万' in anchor['num']:
            num *= 10000
        return num

    def __rank(self, anchors):
        print('--------------吃鸡主播排名--------------')
        for rank in range(0, len(anchors)):
            print(
                f"排名{rank + 1}: 主播名称: {anchors[rank]['name']}, 当前热度：{anchors[rank]['num']}")

    def __show(self, anchors):
        print('--------------吃鸡主播排行--------------')
        for anchor in anchors:
            print('主播名称：%s, 当前热度：%s' % (anchor['name'], anchor['num']))

    def run(self):
        htmls = self.__fetch_contents()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        # self.__show(anchors)
        self.__rank(anchors)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
