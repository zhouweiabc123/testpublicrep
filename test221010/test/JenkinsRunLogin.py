import os
import sys
sys.path.append(r" D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test")
from EmailSend_study import EmailSend
import pytest
from time import sleep
if __name__ == '__main__':
    os.listdir()
    print("开始执行测试用例")
    testpy_path=os.path.dirname(__file__)
    print(testpy_path)
    #pytest.main([fr"{testpy_path}\test_LoginID80qw.py",fr"{testpy_path}\test_LoginID79qw.py",fr"{testpy_path}\test_LoginApi.py",fr"{testpy_path}\test_LoginID32qw.py",fr"{testpy_path}\test_LoginID37qw.py","-vs","--alluredir", "allure-results", "--clean-alluredir"])
    pytest.main([fr"{testpy_path}\test_LoginID32qw.py","-vs","--alluredir", "allure-results", "--clean-alluredir"])
    print("执行测试用例")
    #os.system("allure generate ./allure-results --clean")
    print("执行生成报告成功")
    sleep(2)

