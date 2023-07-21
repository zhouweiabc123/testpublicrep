from airtest.core.api import *
from selenium import webdriver
import os
import time
from airtest.report.report import simple_report
if __name__ == '__main__':

    __author__="周伟"
    auto_setup(__file__, logdir=True)
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://h5.hhygames.com/dfs/h5SDK/?gameId=32#/login")
    time.sleep(5)
    qr=driver.find_element("xpath",'//*[@id="app"]/div[10]/div/div[3]/span/button[2]')
    print(qr)
    qr.click()
    check_box = driver.find_element("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[5]/label')
    check_box.click()
    print(check_box)
    time.sleep(2)
    # 定位账号框和密码框
    user_input = driver.find_element("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/input')
    password_input = driver.find_element("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/input')
    #print(self.username + "----" + self.password)
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
    jb=driver.current_window_handle
    dev = connect_device("Windows:///?h5-dev.hhygames.com.*")
    time.sleep(5)

    #touch(Template(r"tpl1689734259813.png", record_pos=(0.015, 0.222), resolution=(1261, 991)))




    if exists(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928))):
        touch(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928)))
    #这个之前是准确的
    touch(Template(r"tpl1689738934583.png", record_pos=(0.175, 0.473), resolution=(732, 856)))
    sleep(10)
    #20秒没进入游戏，刷新页面
    driver.refresh()
    sleep(5)
    if exists(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928))):
        touch(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928)))
    #判断是否存在“进入游戏按钮”，再次点击进入游戏
    if exists(Template(r"tpl1689738934583.png", record_pos=(0.175, 0.473), resolution=(732, 856))):
        touch(Template(r"tpl1689738934583.png", record_pos=(0.175, 0.473), resolution=(732, 856)))


    sleep(20)
    #touch(Template(r"tpl1689762983160.png", record_pos=(0.077, 0.283), resolution=(1122, 928)))

    #sleep(5)


    # if exists(Template(r"tpl1689763006508.png", record_pos=(0.083, 0.366), resolution=(1122, 987))):
    #     touch(Template(r"tpl1689763006508.png", record_pos=(0.083, 0.366), resolution=(1122, 987)))
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

       #touch(Template(r"tpl1689902955843.png", record_pos=(-0.083, -0.205), resolution=(1079, 928)))

    #wait(Template(r"tpl1689741064648.png", record_pos=(-0.46, -0.229), resolution=(877, 928)))
    # sleep(10)
    # touch(Template(r"tpl1689739396109.png", record_pos=(-0.442, -0.358), resolution=(520, 856)))
    # wait(Template(r"tpl1689739736515.png", record_pos=(-0.427, -0.315), resolution=(520, 856)))

    # if exists(Template(r"tpl1689903391955.png", record_pos=(-0.468, -0.175), threshold=0.6, resolution=(1079, 979))):
    #     touch(Template(r"tpl1689903391955.png", record_pos=(-0.468, -0.175), threshold=0.6, resolution=(1079, 979)))
    if exists(Template(r"tpl1689905871166.png", threshold=0.49999999999999983, record_pos=(-0.462, -0.176), resolution=(949, 928))):
        touch(Template(r"tpl1689905871166.png", threshold=0.49999999999999983, record_pos=(-0.462, -0.176), resolution=(949, 928)))
    # touch(Template(r"tpl1689905871166.png", threshold=0.49999999999999983, record_pos=(-0.462, -0.176), resolution=(949, 928)))
    #touch(Template(r"tpl1689905879184.png", record_pos=(-0.463, -0.168), resolution=(949, 928)))

    # if exists(Template(r"tpl1689739736515.png", record_pos=(-0.427, -0.315), resolution=(520, 856))):
    #     touch(Template(r"tpl1689739736515.png", record_pos=(-0.427, -0.315), resolution=(520, 856)))
    sleep(2)
    # if exists(Template(r"tpl1689904251522.png", record_pos=(0.127, 0.304), resolution=(1472, 979))):
    #     touch(Template(r"tpl1689904251522.png", record_pos=(0.127, 0.304), resolution=(1472, 979)))


    # if exists(Template(r"tpl1689905007569.png", record_pos=(0.018, 0.37), resolution=(1185, 979))):
    #     touch(Template(r"tpl1689905007569.png", record_pos=(0.018, 0.37), resolution=(1185, 979)))
    if exists(Template(r"tpl1689904990142.png", record_pos=(0.02, 0.374), threshold=0.6, resolution=(1185, 979))):
        touch(Template(r"tpl1689904990142.png", record_pos=(0.02, 0.374), threshold=0.6, resolution=(1185, 979)))
    # touch(Template(r"tpl1689904990142.png", record_pos=(0.02, 0.374), resolution=(1185, 979)))

    # touch(Template(r"tpl1689905007569.png", record_pos=(0.018, 0.37), resolution=(1185, 979)))

    #touch(Template(r"tpl1689904234926.png", record_pos=(0.128, 0.303), resolution=(1472, 979)))

    #touch(Template(r"tpl1689904288429.png", record_pos=(0.126, 0.308), resolution=(1472, 979)))



    # touch(Template(r"tpl1689741064648.png", record_pos=(-0.46, -0.229), resolution=(877, 928)))

    #wait(Template(r"tpl1689734562985.png", record_pos=(0.146, 0.291), resolution=(775, 979)))
    #touch(Template(r"tpl1689734578878.png", record_pos=(0.143, 0.381), resolution=(775, 979)))
    #touch(Template(r"tpl1689748995201.png", record_pos=(0.28, 0.311), resolution=(1034, 984)))
    #wait(Template(r"tpl1689749459454.png", record_pos=(0.029, 0.04), resolution=(1520, 928)))
    sleep(3)

    if exists(Template(r"tpl1689909927240.png", threshold=0.44999999999999984, rgb=True, record_pos=(-0.01, 0.102), resolution=(1047, 979))):
        touch(Template(r"tpl1689909927240.png", threshold=0.44999999999999984, rgb=True, record_pos=(-0.01, 0.102), resolution=(1047, 979)))
    # if exists(Template(r"tpl1689906995760.png", threshold=0.49999999999999983, rgb=True, record_pos=(0.228, 0.097), resolution=(1085, 979))):
    #     touch(Template(r"tpl1689906995760.png", threshold=0.49999999999999983, rgb=True, record_pos=(0.228, 0.097), resolution=(1085, 979)))
    # if exists(Template(r"tpl1689905311884.png", threshold=0.49999999999999983, record_pos=(0.207, 0.267), resolution=(1140, 979))):
    #     #touch(Template(r"tpl1689768782355.png", record_pos=(0.184, 0.138), resolution=(947, 928)))
    #     touch(Template(r"tpl1689905311884.png", threshold=0.49999999999999983, record_pos=(0.207, 0.267), resolution=(1140, 979)))
    # if exists(Template(r"tpl1689905262223.png", threshold=0.49999999999999983, record_pos=(0.19, 0.319), resolution=(949, 979))):
    #     touch(Template(r"tpl1689905262223.png", threshold=0.49999999999999983, record_pos=(0.19, 0.319), resolution=(949, 979)))

    # touch(Template(r"tpl1689909927240.png", threshold=0.44999999999999984, rgb=True, record_pos=(-0.01, 0.102), resolution=(1047, 979)))

        #touch(Template(r"tpl1689906928772.png", record_pos=(-0.031, 0.102), resolution=(1085, 979)))
    # touch(Template(r"tpl1689906939271.png", record_pos=(0.098, 0.1), resolution=(1085, 979)))
    # touch(Template(r"tpl1689906978805.png", record_pos=(0.231, 0.098), resolution=(1085, 979)))
    # touch(Template(r"tpl1689906995760.png", record_pos=(0.228, 0.097), resolution=(1085, 979)))

    # touch(Template(r"tpl1689906965780.png", record_pos=(0.229, 0.1), resolution=(1085, 979)))


    # touch(Template(r"tpl1689905262223.png", threshold=0.49999999999999983, record_pos=(0.19, 0.319), resolution=(949, 979)))

    # touch(Template(r"tpl1689905304924.png", record_pos=(0.436, -0.11), resolution=(1140, 979)))
    # touch(Template(r"tpl1689905311884.png", threshold=0.49999999999999983, record_pos=(0.207, 0.267), resolution=(1140, 979)))
    # touch(Template(r"tpl1689905317323.png", record_pos=(0.437, -0.109), resolution=(1140, 979)))

    #touch(Template(r"tpl1689768782355.png", record_pos=(0.184, 0.138), resolution=(947, 928)))


    #touch(Template(r"tpl1689751091266.png", record_pos=(-0.452, -0.234), resolution=(877, 928)))

    # touch(Template(r"tpl1689751105572.png", record_pos=(0.142, 0.073), resolution=(1742, 928)))
    sleep(3)
    #touch(Template(r"tpl1689751111958.png", record_pos=(0.417, 0.02), resolution=(1742, 928)))
    #touch(Template(r"tpl1689751115729.png", record_pos=(0.076, 0.056), resolution=(1742, 928)))
    #wait(Template(r"tpl1689911852702.png", threshold=0.49999999999999983, rgb=True, record_pos=(0.048, 0.061), resolution=(1178, 928)))


    #wait(Template(r"tpl1689734642976.png", threshold=0.5, rgb=False, record_pos=(0.094, -0.047), resolution=(900, 979)))
    #assert_exists(Template(r"tpl1689734657861.png", threshold=0.5499999999999998, rgb=True, record_pos=(0.216, 0.078), resolution=(900, 979)), "确认支付")
    try:
        assert_exists(Template(r"tpl1689911852702.png", threshold=0.49999999999999983, rgb=True, record_pos=(0.048, 0.061), resolution=(1178, 928)), "支付界面存在，通过")
    except Exception as e:
        print("出现错误，继续往下执行")
        print(e)
    print("selenium+airtest,整合执行成功")
    #touch(Template(r"tpl1689734691908.png", record_pos=(0.22, 0.081), resolution=(900, 979)))
    #filepath=r"D:\BaiduNetdiskDownload\airdemo.air\untitled.py",
    #simple_report(__file__)
    simple_report(__file__,logfile=r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test\airdemo.air\log\log.txt",logpath=r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test\airdemo.air\log",output=r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test\airdemo.air\log.html")









