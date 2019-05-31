from Page.home_page import HomePage
from Page.setting_page import SettingPage
from Page.login_page import LoginPage
from Page.person_page import PersonPage
from Page.sign_page import SignPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_homepage(self):
        """返回首页实例化对象"""
        return HomePage(self.driver)

    def get_signpage(self):
        """返回注册页面对象 """
        return SignPage(self.driver)

    def get_personpage(self):
        """返回个人中心页面对象"""
        return PersonPage(self.driver)

    def get_settingpage(self):
        """返回设置页面对象"""
        return SettingPage(self.driver)

    def get_loginpage(self):
        """返回登录页面对象"""
        return LoginPage(self.driver)
