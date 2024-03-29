import allure

import pytest
class TestOne:
    @allure.feature("正确模块")
    @allure.story("1小于2，用例成功")
    def test_03(self):
        print("第一条用例")
        assert 1<2
    @allure.story("1小于2，用例失败")
    def test_04(self):
        with allure.step("先输出描述"):
            print("第二条用例")
        assert 1>2