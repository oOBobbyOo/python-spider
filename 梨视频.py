import requests
import os


def main():

    url = 'https://www.pearvideo.com/video_1177447'
    contId = url.split('_')[1]
    # print(contId)

    videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.3438662622616'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        # 防盗链
        'Referer': url
    }

    resp = requests.get(url=videoStatusUrl, headers=headers)
    resp.encoding = 'utf-8'
    result = resp.json()
    # print(result)

    systemTime = result['systemTime']

    # https://video.pearvideo.com/mp4/short/20171019/1683627732274-11018046-hd.mp4
    srcUrl = result['videoInfo']['videos']['srcUrl']

    # https://video.pearvideo.com/mp4/short/20171019/cont-1177447-11018046-hd.mp4
    videoUrl = srcUrl.replace(systemTime, f'cont-{contId}')
    print(videoUrl)

    # 判断路径是否存在
    base_path = './pearvideo/'
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    # 视频路径
    videoPath = base_path + videoUrl.split('/')[-1]
    # 保存视频到本地文件
    with open(videoPath, 'wb') as f:
        f.write(requests.get(url=videoUrl, headers=headers, stream=True).content)
        print('视频下载完成~~~')


if __name__ == '__main__':
    main()
