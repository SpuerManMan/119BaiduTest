#coding=utf-8
from ReadConfig import ReadConfig as rc
from selenium import webdriver
from log import MyLog
import time
import os
log=MyLog.get_log()
logger=log.get_logger()

class DRIVER:
    @staticmethod
    def get_driver():
        URL = rc.get_URL('host')
        Type = rc.get_URL('BROWSER_TYPE')
        ChromeDriver=rc.get_Driver('Chrome')
        IEDriver=rc.get_Driver('IE')
        FireFoxDriver=rc.get_Driver('Firefox')
        #print(FireFoxDriver)
        if Type=='Chrome':
            driver=webdriver.Chrome(ChromeDriver)
            time.sleep(2)
            driver.maximize_window()
            time.sleep(2)
            driver.get(URL)
            time.sleep(2)
            return driver
        elif Type=='IE':
            driver=webdriver.Ie()
            time.sleep(2)
            driver.maximize_window()
            time.sleep(2)
            driver.get(URL)
            time.sleep(2)
            return  driver
        elif Type=='Firefox':
            driver=webdriver.Firefox(executable_path='geckodriver.exe')
            driver.maximize_window()
            driver.get(URL)
            return driver

    @staticmethod
    def save_screenshot(path,driver):
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        driver.save_screenshot(os.path.join(path,'%s.png' % current_time))