#!usr/local/bin/python3.7
# -*-coding: utf-8 -*-
import random

from Web.Page.IndexPage import IndexPage


class TestContact:
    name = "aab2_test_002"
    account = "aad5"
    phone = "13211212223"

    def setup(self):
        self.index = IndexPage()
        pass

    def test_contact(self):
        # 点击添加
        member = self.index.click_add_member().add_member(self.name, self.account, self.phone)
        # 断言
        assert member

    def test_contact2(self):
        # 点击添加
        # 获取列表
        member = self.index.click_add_member()
        member.add_member(self.name, self.account, self.phone)
        bool = member.get_member(self.name)
        # 断言
        assert bool