from Base.base import Base
from Page.UIElements import UIElements





class HomePage(Base):

    def __init__(self,driver):

        Base.__init__(self,driver)

    def click_my_btn(self):
        """点击首页按钮"""
        self.click_element(UIElements.home_my_btn_id)

























