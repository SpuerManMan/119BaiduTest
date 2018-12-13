#coding
from  selenium import webdriver

class BasePage(object):

    def __init__(self):
        pass

    def set_driver(cls,driver):
        cls.driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        # 窗口最大化
        cls.driver.maximize_window()
        # 打开115网盘网址
        page_url = "http://baidu.com/"
        cls.driver.get(page_url)
