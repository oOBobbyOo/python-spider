from selenium.webdriver import Chrome, Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

from time import sleep


options = ChromeOptions()

# 不自动关闭浏览器
options.add_experimental_option("detach", True)

# 设置代理
# proxy_ip = 'http://113.124.86.24:9999'
# options.add_argument("--proxy-server=%s" % proxy_ip)

driver = Chrome(options=options)

driver.get('https://www.lagou.com/')

# 延迟
sleep(1)

driver.find_element(By.XPATH, '//*[@id="cboxClose"]').click()

# 延迟
sleep(2)

# selenium 可以动态执行js
driver.execute_script("""
  var a = document.getElementsByClassName('un-login-banner')[0];
  a.parentNode.removeChild(a);
""")

sleep(1)

# 找到输入框 “输入python 回车”
driver.find_element(
    By.XPATH, '//*[@id="search_input"]').send_keys('python', Keys.ENTER)


sleep(1)

job_list = driver.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')


for job in job_list:
    job_a = job.find_element(By.XPATH, './div[1]/div[1]//a')
    # print(job_a.text)
    job_a.click()

    # 此时，在浏览器我们能看到详情页内容
    # 但是，在selenium中，我们依然在首页
    # 所以，必须得让selenium去调整它的视角, 切换窗口
    driver.switch_to.window(driver.window_handles[-1])

    job_detail = driver.find_element(
        By.XPATH, '//*[@id="job_detail"]/dd[2]')
    print(job_detail.text)
    print('----------------------------------------------------------------')

    sleep(3)
    # 关闭当前窗口
    driver.close()
    # 调整selenium视口
    driver.switch_to.window(driver.window_handles[0])
