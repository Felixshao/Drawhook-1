# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


# 读取yaml
def load_data(path):
    with open(path, 'r', encoding="utf-8") as f:
        return yaml.load(f)


class TestDemo:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        pass

    # 参数化数据
    @pytest.mark.parametrize('data', load_data("test_data.yaml")['data'])
    def test1(self, data):

        for step in load_data("test_data.yaml")['steps']:
            print(step)

            if "get" in step:
                url = step.get("get")
                self.driver.get(url)

            elif 'find_element' in step:
                by = step.get("find_element")['by']
                locator = step.get("find_element")['value']
                current_element: WebElement = self.driver.find_element(by, locator)

            elif "click" in step:
                current_element.click()

            elif 'send_keys' in step:
                value = step.get('send_keys')
                value = value.replace('${data}', data)
                current_element.send_keys(value)

            elif 'sleep' in step:
                time.sleep(step.get('step'))

    # 自定义
    @pytest.mark.parametrize('data', load_data("test_data.yaml")['data'])
    def test2_my_frame(self, data):
        for step in load_data("test_data.yaml")['steplists']:
            # 获取动作
            action = [key for key in step.keys()][0]
            # 获取参数
            values = step.get(action) if isinstance(step.get(action), list) else [step.get(action)]
            common = ''
            for value in values:
                # 判断数据驱动
                if '${data}' in value:
                    value = data
                # 拼接参数
                common = common + '\'{}\', '.format(value)
            if action in ['click', 'send_keys']:
                # 拼接执行语句
                pd = 'current_element.{}({})'.format(action, common)
            else:
                pd = 'self.driver.{}({})'.format(action, common)
            # 执行语句并获取返回值
            current_element = eval(pd)
