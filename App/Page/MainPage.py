# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
# 首页Page
from appium.webdriver.common.mobileby import MobileBy
from App.Page.BasePage import BasePage


class MainPage(BasePage):
    _contact_list = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def GotoContactlist(self):
        """
        进入通讯录
        :return:
        """
        self.Find(*self._contact_list).click()
        return ContactPage(self.driver)