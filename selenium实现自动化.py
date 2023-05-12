"""
selenium 使用教程：
  - 环境安装 pip install selenium
  - 安装浏览器驱动程序
  Chrome:	https://sites.google.com/chromium.org/driver/
  Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
  Firefox:	https://github.com/mozilla/geckodriver/releases
  Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

  - 1.下载后解压, 解压后的webdriver放到bin目录
  - 2.打开命令终端, cd /usr/local/bin (因为一般bin目录是隐藏的, 可以通过终端打开 cmd + shift + g)
  - 3. 如果在运行的过程中提示: 无法打开“chromedriver”, 因为无法验证开发者, 是因为mac 不信任我们下载下来的 webdriver 文件，打开安全隐私模式，添加信任就可以了
  - 进入webdriver存放目录, 我这里是/usr/local/bin, 在终端输入命令: xattr -d com.apple.quarantine chromedriver
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lxml import etree
import time

# chromedriver 路径
path = '/usr/local/bin/chromedriver'
service = Service(f'{path}')

options = Options()
# 沙盒模式运行
options.add_argument('--no-sandbox')

# 大量渲染时候写入/tmp 而非/dev/shm
options.add_argument('--disable-dev-shm-usage')

# 不自动关闭浏览器
options.add_experimental_option("detach", True)

# 添加实验性质的设置参数 实现监测规避
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 无头模式
# options.add_argument("--headless")

# 禁用GPU加速
# options.add_argument("--disable-gpu")

# 实例化一个浏览器对象 (传入浏览器驱动)
# driver = webdriver.Chrome(executable_path=path)

# 隐藏滚动条, 应对一些特殊页面
# options.add_argument('--hide-scrollbars')

# 禁用JavaScript
# options.add_argument("--disable-javascript")

# 启动浏览器最大化
# options.add_argument('--start-maximized')

driver = webdriver.Chrome(
    service=service, options=options)


# 让浏览器发起一个指定url
# driver.get('https:///www.baidu.com/')
driver.get('https://www.umei.cc/')

time.sleep(2)

# driver.find_element('xpath', '//*[@id="nav"]/ul/li[3]/a').click()
driver.find_element(By.XPATH, '//*[@id="nav"]/ul/li[3]/a').click()


# 获取浏览器当前页面的源码数据
# page_text = driver.page_source
# tree = etree.HTML(page_text)

time.sleep(3)

# 关闭当前窗口
driver.close()
