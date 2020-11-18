# usr/local/bin/python3.7
# -*-coding: utf-8 -*-
import time

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


# 读取yaml
def load_data(path):
    with open(path, 'r', encoding="utf-8") as f:
        return yaml.load(f)


class TestDemo:

    # 参数化数据
    @pytest.mark.parametrize('data', load_data("test_data.yaml")['data'])
    def test1(self, data):

        for step in load_data("test_data.yaml")['steps']:
            print(step)
            if "driver" in step:
                browser = str(step.get("driver").get("browser")).lower()
                if browser == "chrome":
                    driver: WebDriver = webdriver.Chrome()
                else:
                    print(f"{driver} don't know which browser")

            elif "get" in step:
                url = step.get("get")
                driver.get(url)

            elif 'find_element' in step:
                by = step.get("find_element")['by']
                locator = step.get("find_element")['value']
                current_element: WebElement = driver.find_element(by, locator)

            elif "click" in step:
                current_element.click()

            elif 'send_keys' in step:
                value = step.get('send_keys')
                value = value.replace('${data}', data)
                current_element.send_keys(value)

            elif 'sleep' in step:
                time.sleep(step.get('step'))
