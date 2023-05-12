import requests
import aiohttp
import asyncio
import time

start_time = time.time()


async def get_page(url):
    print('正在下载', url)
    # requests.get 基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送

    # response = requests.get(url)
    # print('下载完毕', response.text)

   # aiohttp 基于异步网络请求的模块
    async with aiohttp.ClientSession() as session:
        # get()、post()
        # headers, params/data, proxy='ip'

        # 使用await进行挂起
        async with await session.get(url) as response:
            # text() 返回字符串形式的响应数据
            # read() 返回二进制形式的响应数据
            # json() 返回的json对象
            # 注意： 获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print('下载完毕', page_text)

urls = ['https://www.baidu.com/', 'https://www.python.org/']

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end_time = time.time()

print(f'总耗时: {end_time - start_time}')
