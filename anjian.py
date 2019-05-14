from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
browser = webdriver.Chrome()

browser.get("https://www.zhihu.com/question/305114445")

# js="var q=document.documentElement.scrollTop=100000"
# js="var q=document.documentElement.scrollTop={0}".format(i)
for i in range(0,11):
    i = i*100000
    js = "var q=document.documentElement.scrollTop={0}".format(i)
    browser.execute_script(js)
    time.sleep(1)

html = browser.page_source
result = re.findall('img src="(.*?)"',html)
print(len(result))
for i in result:
    if i.endswith('.jpg'):
        print(i)