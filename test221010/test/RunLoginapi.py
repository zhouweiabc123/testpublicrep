import os
import sys
sys.path.append(r"E:\A_PythonProject\TestProject\test221010\test")
from EmailSend_study import EmailSend
import pytest
from time import sleep
if __name__ == '__main__':
    print("开始执行测试用例")
    pytest.main(["E:\A_PythonProject\TestProject\\test221010\\test\\test_LoginApi.py","-vs","--alluredir", "./tmp", "--clean-alluredir"])
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
    # 移动report到send_dir里
    # 移动
    try:
        os.system("move allure-report send_dir")
        print("移动report到send_dir里成功")
        sleep(5)
    except Exception as e:
        print(e)
    #创建email对象
    emailsend = EmailSend(r"send_dir", r"send_dir.zip", 'send_dir.zip')
    #压缩文件
    emailsend.zipDir()
    sleep(5)
    #'18407469853@163.com'
    #发送带附件的邮件
    emailsend.sendemail(addrs=['18407469853@163.com'])
    print("ok!")
    sleep(3)
