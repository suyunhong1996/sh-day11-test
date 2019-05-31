from selenium.webdriver.common.by import By


class UIElements:
    """管理所有页面元素"""

    """首页"""
    # 首页我的按钮
    home_my_btn_id = (By.ID, "com.yunmall.lc:id/tab_me")

    """注册页面"""
    # 已有账号去登录
    sign_exits_account_btn_id = (By.ID, "com.yunmall.lc:id/textView1")
    """登录页面"""
    # 账号框
    login_account_id = (By.ID, "com.yunmall.lc:id/logon_account_textview")
    # 密码框
    login_password_id = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    # 登录按钮
    login_btn_id = (By.ID, "com.yunmall.lc:id/logon_button")
    """个人中心页面"""
    # 我的优惠券
    my_shopping_cart_id = (By.ID, '')
    # 设置按钮
    person_setting_id = (By.ID, '')
    """设置页面"""
    # 退出按钮
    setting_logout_btn_id = (By.ID, '')
    # 弹窗 确认退出按钮
    setting_acc_quit_btn_id = (By.ID, '')
    # 弹窗 取消退出按钮
    setting_dis_quit_btn_id = (By.ID, '')
