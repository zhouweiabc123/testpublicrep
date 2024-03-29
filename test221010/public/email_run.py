import os
from time import sleep
import pytest

from test221010.public.EmailSend_study import EmailSend

if __name__ == '__main__':
    print("开始执行测试用例")
    pytest.main(["test_email.py","test.py", "-vs", "--alluredir", "./tmp", "--clean-alluredir"])
    print("执行测试用例")
    os.system("allure generate ./tmp --clean")
    print("执行生成报告成功")
    sleep(3)
    # 判断是否存在，存在先删除
    if os.path.exists("send_dir.zip"):
        os.system("del -s -q send_dir.zip")
        print("删除zip成功")
    if os.path.exists("send_dir\\allure-report"):
        os.system("rmdir /s /q send_dir\\allure-report")
        print("删除report成功")
    # 移动到send_dir里
    os.system("move allure-report send_dir")
    emailsend = EmailSend(r"send_dir", r"send_dir.zip","send_dir.zip")
    emailsend.zipDir()
    #emailsend.sendemail()
    # sleep(5)