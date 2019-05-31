import time
import allure,os
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: (By.ID,id属性）......
        :param timeout: 超时时长
        :param poll_frequency: 搜索间隔
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: (By.ID,id属性）......
        :param timeout: 超时时长
        :param poll_frequency: 搜索间隔
        :return: 元素定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, poll_frequency=1.0):
        self.get_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=30, poll_frequency=1.0):
        input_text = self.get_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    def scroll_sreen(self, sc=1):
        """
        滑动页面
        :param sc:1 上滑，2 下滑，3 左滑，4 右滑
        :return:
        """
        time.sleep(2)
        # 获取屏幕分辨率('width','height')
        screen_size = self.driver.get_window_size()
        # 获取宽
        width = screen_size.get('width')
        # 获取高
        height = screen_size.get('height')
        # 根据宽高滑动
        if sc == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if sc == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if sc == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if sc == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def screen_page(self,name='截图'):
        """
        报告添加截图
        :param name: 截图名字
        :return:
        """
        # 定义图片名字
        png_name = './image'+os.sep+'{}.png'.format(int(time.time()))
        # 截图
        self.driver.get_screenshot_as_file(png_name)
        # 二进制打开文件
        with open(png_name,'rb') as f:
            allure.attach("截图名字",f.read(),allure.attach_type.PNG)
        # 使用添加附件 添加到allure报告

    def get_toast(self,toast):
        """
        获取toast消息
        :param toast:拼接toast消息内容
        :return: 返回获取到的toast

        """
        # 找toast
        toast_xpath = (By.XPATH, "//*[contains(@text,'{}')]".format(toast))
        # 找元素
        data = self.get_element(toast_xpath).text
        # 返回toast小心
        return data
