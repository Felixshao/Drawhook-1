#!usr/local/bin/python3.7
# -*-coding: utf-8 -*-
from selenium.webdriver.common.by import By
from Web.Page.AddMemberPage import AddMemberPage
from Web.Page.BasePage import BasePage


class IndexPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def click_add_member(self):
        # 点击添加成员
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage()
