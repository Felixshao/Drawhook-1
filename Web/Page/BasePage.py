#!usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# 基类，用来封装基础方法，如：driver、find...
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 复用浏览器
            option = Options()
            option._debugger_address = '127.0.0.1:9222'
            # 浏览器驱动
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver

        if self._base_url != "":
            # 打开网址
            self.driver.get(self._base_url)
        # 隐示等待
        self.driver.implicitly_wait(3)

    def find(self, by, locator):
        # 查找元素，返回第一个element
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        # 查找元素，返回所有element，列表
        return self.driver.find_elements(by, locator)

    def wait_element_click(self, locator, timeout=10):
        # 显示等待元素为可点击状态
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))