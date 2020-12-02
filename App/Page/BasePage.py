#!usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# 基类，用来封装基础方法，如：driver、find...
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def Find(self, by, locator):
        # 查找元素，返回第一个element
        return self.driver.find_element(by, locator)

    def Finds(self, by, locator):
        # 查找元素，返回所有element，列表
        return self.driver.find_elements(by, locator)

    def FindText(self, text):
        # 通过文本查找元素
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"' + text + '\")')

    def SlipeUpWindow(self, num=1):
        """
        向上滑动页面
        num:传入次数，控制滑动次数
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.8
        y2 = height * 0.2
        for i in range(num):
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(1)

    def SlipeUnderWindow(self, num=1):
        """
        向下滑动页面
        num:传入次数，控制滑动次数
        """
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x1 = width * 0.5
        y1 = height * 0.4
        y2 = height * 0.8
        for i in range(num):
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(1)
