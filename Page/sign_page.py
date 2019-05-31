from Base.base import Base
from Page.UIElements import UIElements




class SignPage(Base):
    """注册页面"""

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_sign(self):
        """点击首页按钮"""
        self.click_element(UIElements.sign_exits_account_btn_id)









