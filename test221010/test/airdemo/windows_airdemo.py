import pytest
from allure_commons.utils import md5
from selenium import webdriver
import os
import time
from airtest.core.api import *
from airtest.report.report import simple_report
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://h5-dev.hhygames.com/dfs/h5SDK/?gameId=32#/login")
game_url="https://h5.hhygames.com/dfs/h5SDK/?gameId=32#/login"
game_connect="h5.hhygames.com/dfs/h5SDK/"
gid='32'
driver = webdriver.Chrome()
def premise_windows_airtet():
    __author__ = "周伟"
    auto_setup(__file__, logdir=True)
    #driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(game_url)
    time.sleep(3)
    qr = driver.find_element("xpath", '//*[@id="app"]/div[10]/div/div[3]/span/button[2]')
    print(qr)
    qr.click()
    check_box = driver.find_element("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[5]/label')
    check_box.click()
    print(check_box)
    time.sleep(2)
    # 定位账号框和密码框
    user_input = driver.find_element("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/input')
    password_input = driver.find_element("xpath",
                                         '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/input')
    # print(self.username + "----" + self.password)
    print(user_input)
    # 输入事先保存的账号和密码
    user_input.send_keys("18598019760")
    time.sleep(1)
    password_input.send_keys("123456")
    time.sleep(1)
    print("输入账号密码成功！")
    # 点击登录
    login_bt = driver.find_element("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[3]/button')
    login_bt.click()
    print("睡眠60秒")
    print(driver.current_window_handle)
    print(driver.window_handles)
    jb = driver.current_window_handle
    # dev = connect_device(f"Windows:///?{game_connect}*32*")
    # time.sleep(5)

def demo_windows_airtest():
    #连接打开的浏览器窗口，根据title模糊匹配
    dev = connect_device(f"Windows:///?{game_connect}*{32}*")
    time.sleep(5)
    #选服界面开始进入游戏
    if exists(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928))):
        touch(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928)))
        # 这个之前是准确的
        touch(Template(r"tpl1689738934583.png", record_pos=(0.175, 0.473), resolution=(732, 856)))
        sleep(10)
        # 20秒没进入游戏，刷新页面，重新来
        driver.refresh()
        sleep(5)
    if exists(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928))):
        touch(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928)))
    #判断是否存在“进入游戏按钮”，再次点击进入游戏
    if exists(Template(r"tpl1689738934583.png", record_pos=(0.175, 0.473), resolution=(732, 856))):
        touch(Template(r"tpl1689738934583.png", record_pos=(0.175, 0.473), resolution=(732, 856)))
    sleep(20)
    #进入游戏等待一些活动弹窗弹出，如果有就按关闭按钮关闭，某些活动则需要手动关闭
    sleep(5)
    if exists(Template(r"tpl1689903156406.png", record_pos=(0.27, -0.12), resolution=(1079, 979))):
        touch(Template(r"tpl1689903156406.png", record_pos=(0.27, -0.12), resolution=(1079, 979)))
    if exists(Template(r"tpl1689903156406.png", record_pos=(0.27, -0.12), resolution=(1079, 979))):
        touch(Template(r"tpl1689903156406.png", record_pos=(0.27, -0.12), resolution=(1079, 979)))
    # touch(Template(r"tpl1689903194123.png", record_pos=(0.27, -0.133), resolution=(1079, 979)))
    # touch(Template(r"tpl1689903209803.png", record_pos=(0.271, -0.132), resolution=(1079, 979)))
    if exists(Template(r"tpl1689903233756.png", record_pos=(0.272, -0.131), resolution=(1079, 979))):
        touch(Template(r"tpl1689903233756.png", record_pos=(0.272, -0.131), resolution=(1079, 979)))
    sleep(3)
    #定位商城打开
    if exists(Template(r"tpl1689905871166.png", threshold=0.49999999999999983, record_pos=(-0.462, -0.176), resolution=(949, 928))):
        touch(Template(r"tpl1689905871166.png", threshold=0.49999999999999983, record_pos=(-0.462, -0.176), resolution=(949, 928)))
    sleep(2)
    #打开的商城找到仙玉商城打开，宝藏阁切换，如果直接是仙玉商城则不打开
    if exists(Template(r"tpl1689904990142.png", record_pos=(0.02, 0.374), threshold=0.6, resolution=(1185, 979))):
        touch(Template(r"tpl1689904990142.png", record_pos=(0.02, 0.374), threshold=0.6, resolution=(1185, 979)))
    #找到仙玉商品，点击打开创建订单
    sleep(3)
    if exists(Template(r"tpl1689909927240.png", threshold=0.44999999999999984, rgb=True, record_pos=(-0.01, 0.102),
                       resolution=(1047, 979))):
        touch(Template(r"tpl1689909927240.png", threshold=0.44999999999999984, rgb=True, record_pos=(-0.01, 0.102),
                       resolution=(1047, 979)))
    sleep(3)
    #断言选择支付界面是否存在，存在则通过
    try:
        res_exists=assert_exists(
            Template(r"tpl1689911852702.png", threshold=0.49999999999999983, rgb=True, record_pos=(0.048, 0.061),
                     resolution=(1178, 928)), "支付界面存在，通过")

        print(type(res_exists))
        print(res_exists[0])
        return res_exists[0]
        sleep(5)
        driver.quit()
    except Exception as e:
        print("出现错误，继续往下执行")
        print(e)
    print("selenium+airtest,整合执行成功")

# @pytest.mark.parametrize('num1,num2',[(1,2),(2,3)])#动态入参，测试不同参数的用例执行结果
# def test_param(num1,num2):
#
#     assert num1 < 2
#     assert num2 < 1

if __name__ == '__main__':

    # dirpath_yml=os.path.dirname(os.path.abspath(__file__))
    # d=os.path.join(os.path.dirname(os.path.abspath(__file__)),"yml")
    # print("开始执行测试")
    # print("执行成功")
    # print(dirpath_yml)
    # print(d)
    print("开始执行测试")
    premise_windows_airtet()
    demo_windows_airtest()
    print("执行成功")
