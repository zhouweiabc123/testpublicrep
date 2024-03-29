import os
from time import sleep
import pytest
#from test221010.public import EmailSend_study as es
import allure
import allure_pytest
import allure_commons

from test221010.public.EmailSend_study import EmailSend


class TestEmail:
    #@allure.feature("正确模块")
    #@allure.story("1小于2，用例成功")
    def test_01(self):
        print("第一条用例")
        assert 1<2
    #@allure.story("1小于2，用例失败")
    def test_02(self):
        with allure.step("先输出描述"):
            print("第二条用例")
        assert 1>2
if __name__ == '__main__':
    print("开始执行测试用例")
    pytest.main(["test_email.py","-vs","--alluredir","./tmp","--clean-alluredir"])
    print("执行测试用例")
    os.system("allure generate ./tmp --clean")
    print("执行生成报告成功")
    #sleep(5)
    #判断是否存在，存在先删除
    if os.path.exists("send_dir.zip"):
        os.system("del -s -q send_dir.zip")
        print("删除zip成功")
    if os.path.exists("send_dir\\allure-report"):
        os.system("rmdir /s /q send_dir\\allure-report")
        print("删除report成功")
    #移动到send_dir里
    #os.system("move allure-report send_dir")
    print("移动成功")
    emailsend = EmailSend(r"send_dir", r"send_dir.zip", 'send_dir.zip')
    emailsend.zipDir()
    # emailsend.sendemail()
