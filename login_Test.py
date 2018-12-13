#coding=utf-8

from loginPage import LoginElements,loginPage
import time
from config.configDriver import DRIVER
from log import *
class Login_Test:
    def __init__(self):
        self.logpath = MyLog.get_log()
        self.retult_path = self.logpath.get_result_path()

    def Login(self,driver):

        login=LoginElements('userName','password','TANGRAM__PSP_10__submit')
        loginpage=loginPage(driver,login)
        time.sleep(2)
        userName=loginpage.get_account_ipt()
        time.sleep(2)
        loginpage.clear_account_ipt(userName)
        time.sleep(2)
        loginpage.account_input(userName,'18600129395@163.com')
        time.sleep(2)

        DRIVER.save_screenshot(self.retult_path,driver)
        password=loginpage.get_pwd_ipt()
        time.sleep(2)
        loginpage.clear_pwd_ipt(password)
        time.sleep(2)
        loginpage.pwd_input(password,'xtloveplr520')
        time.sleep(2)
        login_btn=loginpage.get_login_btn()
        loginpage.click_btn(login_btn)
        DRIVER.save_screenshot(self.retult_path, driver)
