#
# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get("https://www.zhihu.com/question/299205851")
#
# print('Before search================')
#
# # 打印当前页面title
# title = driver.title
# print(title)
#
# # 打印当前页面URL
# now_url = driver.current_url
# print(now_url)
#
# # html = driver.page_source
# # print(html)

import requests
import re
url = 'https://www.zhihu.com/question/299205851/answer/532026743'

headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
}

html = requests.get(url, headers=headers)

html.encoding = 'utf-8'

html = html.text
result = re.findall('img src="(.*?)"',html)
for i in result:
    if i.endswith('.jpg'):
        print(i)

