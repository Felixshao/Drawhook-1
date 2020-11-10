#!usr/local/bin/python3.7
# -*-coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Web.Page.BasePage import BasePage


class AddMemberPage(BasePage):
    _base_url = ''

    def add_member(self, name, account, phone):
        # 输入姓名
        self.find(By.ID, 'username').send_keys(name)
        # 输入账号
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        # 输入手机号
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        # 点击保存
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

        return True

    def get_member(self, value):
        # 等待复选框可点击
        locator = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_element_click(locator)

        while True:
            # 获取列表姓名
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2) > span')
            titles = [element.text for element in elements]

            # 判断新增成员是否在列表内
            if value in titles:
                return True

            # 获取当前页数和总页数
            element = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text')
            page = element.text.split('/')

            # 判断是否为最后一页，不是则点击下一页
            if page[0] != page[1]:
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
            else:
                return False