#ocding=utf-8
from log import MyLog
Lg=MyLog.get_log()
Log=Lg.get_logger()

class loginPage:

    def __init__(self,driver,login_elements):
        self.driver=driver
        self.login_elements=login_elements


    #定位用户输入框

    def get_account_ipt(self):
        account_Locator=self.login_elements.account
        Log.info('定位用户输入框')
        account_ipt=self.driver.find_element_by_name(account_Locator)
        return account_ipt

    #情空用户信息

    def clear_account_ipt(self,account_ipt):
        Log.info('清空用户信息')
        account_ipt.clear()

    #输入用户名
    def account_input(self,account_ipt,account):
        Log.info('输入用户名')
        account_ipt.send_keys(account)


    #定位密码输入框

    def get_pwd_ipt(self):
        pwd_Locator=self.login_elements.password
        Log.info('定位密码输入框')
        pwd_ipt=self.driver.find_element_by_name(pwd_Locator)
        return pwd_ipt

    #清空密码信息

    def clear_pwd_ipt(self,pwd_ipt):
        Log.info('清空密码信息')
        pwd_ipt.clear()

    #输入密码
    def pwd_input(self,pwd_ipt,password):
        Log.info('输入密码')
        pwd_ipt.send_keys(password)

    #获取登录按钮

    def get_login_btn(self):
        btn_Locator=self.login_elements.login_btn
        Log.info('定位登录按钮')
        login_btn=self.driver.find_element_by_id(btn_Locator)
        return login_btn

    #点击登录
    def click_btn(self,login_btn):
        Log.info('点击登录')
        login_btn.click()


class LoginElements:

    def __init__(self,account='',password='',login_btn=''):
        self.account=account
        self.password=password
        self.login_btn=login_btn
