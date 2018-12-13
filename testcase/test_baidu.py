#coding=utf-8

import time
import unittest
from selenium import webdriver
from login_Test import Login_Test
from log import MyLog
from config.configDriver import DRIVER
from selenium.webdriver import ActionChains


Lg=MyLog.get_log()
Log=Lg.get_logger()
class TestBaiDu(unittest.TestCase):

    def setUp(self):
        self.logpath = MyLog.get_log()
        self.retult_path = self.logpath.get_result_path()
        self.driver=DRIVER.get_driver()


    def tearDown(self):
        self.driver.quit()  # 清理退出


    def test_login(self):
        try:

            self.driver.find_element_by_link_text('登录').click()
            time.sleep(3)
            DRIVER.save_screenshot(self.retult_path, self.driver)
            time.sleep(2)
            self.driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
            time.sleep(2)
            test_class = Login_Test()
            test_class.Login(self.driver)
            time.sleep(2)
            Log.info(self.driver.title)
            self.assertEqual(self.driver.title, "百度一下，你就知道")
        except Exception as ex:
             Log.info(ex)


    def test_search(self):
        self.driver.find_element_by_name('wd').send_keys('python')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        DRIVER.save_screenshot(self.retult_path, self.driver)
        time.sleep(2)
        self.assertEqual(self.driver.title, "Python_百度搜索")

    '''
    def test_quit(self):
        user=self.driver.find_element_by_id('s_username_top')
        time.sleep(2)
        ActionChains(driver=self.driver).move_to_element(user).perform()
        time.sleep(2)
        self.driver.find_element_by_link_text('退出').click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
    '''