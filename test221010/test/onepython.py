import unittest

import pytest
import unittestreport
import openpyxl
import allure
import requests
import yaml
def func1(e:list):
    print('返回')
    return e
def test_01_login():
    print('测试pytest')
    assert 1==2
if __name__ == '__main__':
    print('测试第一个Python程序')
    print(func1([1, 2]))
    # up = unittestreport()l
    # su = unittest.defaultTestLoader.discover('./test')
    # run = unittestreport.TestRunner(suite=su)
    # run.run()
    req = requests.session()
    rew = requests.get(url='https://www.baidu.com',encode='utf-8')
    print(rew.text)

    with open('a.yml', 'r', encoding='utf-8') as f:
       ab = yaml.full_load(f)
       print(ab)