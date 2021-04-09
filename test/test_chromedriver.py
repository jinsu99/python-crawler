# pip install selenium
# pip freeze > requirements.txt
import time
from selenium import webdriver

wd = webdriver.Chrome('C:\\Users\\pc\\Desktop\\Pycharm-project\\chromedriver_win32\\chromedriver.exe')
wd.get('http://www.google.com')

time.sleep(3)
html = wd.page_source
print(html)

wd.close()