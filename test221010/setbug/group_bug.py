import os
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class LogPage:
    url_login = "http://10.10.10.21:8080/login.jsp?os_destination=%2Fissues%2F%3Fjql%3Dissuetype%2520%253D%2520BUG%25E7%25B1%25BB"
    url_create = ""
    #driver = webdriver.Chrome()
    def __init__(self,driver):
        driver.get(url=self.url_login)
        driver.implicitly_wait(5)
        driver.maximize_window()

    def el_find(self,path_el):
        el =driver.find_element(path_el[0],path_el[1])
        e1 = 1
        return el
    def quit(self):
        driver.quit()
    def group_txt(file_name="bug.txt"):
        with open("bug.txt","r",encoding="utf-8") as f :
            bugtxt = f.readlines()
            #print(bugtxt)

        return bugtxt
    def newbg(self):
        bugtxt = self.group_txt()
        bg = bugtxt
        new_bg = bg
        # for i in bg:
        #     i = i.strip()
        #     new_bg.append(i)
        return new_bg
   # print(new_bg)

def login(driver):
    # 创建对象方便调用封装的方法
    logpage = LogPage(driver)
    bg = logpage.newbg()
    #登录
    el = logpage.el_find(('xpath', '//*[@id="login-form-username"]'))
    el.send_keys("18598019760")
    sleep(1)
    el1 = logpage.el_find(('xpath', '//*[@id="login-form-password"]'))
    el1.send_keys("123456")
    sleep(1)
    el3 = logpage.el_find(('xpath', '//*[@id="login-form-submit"]'))
    el3.click()
    sleep(1)
    print("====================================================================================================")
    for i in range(0,len(bg)):#从2开始，len-2
        #print(i)
        el4 = logpage.el_find(('xpath', '//*[@id="create_link"]'))
        el4.click()
        sleep(1)
        # 建bug弹窗
        el5 = logpage.el_find(('xpath', '//*[@id="summary"]'))  # 概要
        el5.send_keys(bg[i])
        el0 = logpage.el_find(('xpath', '//*[@id="description-wiki-edit"]/nav/div/div/ul/li[2]/a'))  # 切换文本
        el0.click()
        el6 = logpage.el_find(('xpath', '//*[@id="description"]'))  # 描述
        el6.send_keys("1")
        el7 = logpage.el_find(('xpath', '//*[@id="customfield_10205"]/option[3]'))  # 需求分类
        el7.click()
        sleep(1)
        el8_1 = logpage.el_find(('xpath', '//*[@id="assign-to-me-trigger"]'))#分配给我
        el8_1.click()
        # el8 = logpage.el_find(('xpath', '//*[@id="assignee-field"]'))  # 经办人框
        # el8.click()
        # sleep(1)
        # el8.send_keys(Keys.BACKSPACE)#删除默认
        # # el8.clear()
        # sleep(1)
        # el8.send_keys("周伟")#经办人名精确搜索
        # sleep(1)
        # el8.send_keys(Keys.ENTER)#模拟enter键按下
        sleep(1)
        el_serverman = logpage.el_find(('xpath','//*[@id="customfield_10210"]'))#服务端
        el_serverman.send_keys("朱海军")
        sleep(1)
        el_serverman.send_keys(Keys.ENTER)
        el_sendman = logpage.el_find(('xpath','//*[@id="customfield_10206"]'))#抄送人
        el_sendman.send_keys('张子斌')
        sleep(1)
        el_sendman.send_keys(Keys.ENTER)
        sleep(1)
        el9 = logpage.el_find(('xpath', '//*[@id="create-issue-submit"]'))#新建
        el9.click()
        #logpage.quit()

    # el4 = logpage.el_find(('xpath','//*[@id="create_link"]'))
    # el4.click()
    # sleep(2)
    # #建bug弹窗
    # el5 = logpage.el_find(('xpath','//*[@id="summary"]')) #概要
    # el5.send_keys(bg[1])
    # el0 = logpage.el_find(('xpath','//*[@id="description-wiki-edit"]/nav/div/div/ul/li[2]/a'))#切换文本
    # el0.click()
    # el6 = logpage.el_find(('xpath', '//*[@id="description"]'))#描述
    # el6.send_keys("1")
    # el7 = logpage.el_find(('xpath','//*[@id="customfield_10205"]/option[3]'))#需求分类
    # el7.click()
    # sleep(2)
    # el8 = logpage.el_find(('xpath', '//*[@id="assignee-field"]'))#经办人框
    # el8.click()
    # sleep(2)
    # el8.send_keys(Keys.BACKSPACE)
    # #el8.clear()
    # sleep(2)
    # el8.send_keys("朱海军")
    # sleep(3)
    # el8.send_keys(Keys.ENTER)
    # sleep(2)
    # el9 = logpage.el_find(('xpath','//*[@id="create-issue-submit"]'))
    # el9.click()
    #print("登录成功")
    #logpage.quit()



if __name__ == '__main__':
     driver = webdriver.Chrome()
     #login(driver)
     logpage = LogPage(driver)
     b = logpage.newbg()
     print(b)
     print(len(b))
     for i in b:
        print(i)
    # el = logpage.el_find(('xpath','//*[@id="login-form-username"]'))
    # el.send_keys("18598019760")
    # sleep(1)
    # el1 = logpage.el_find(('xpath','//*[@id="login-form-password"]'))
    # el1.send_keys("123456")
    # sleep(1)
    # el3 = logpage.el_find(('xpath','//*[@id="login-form-submit"]'))
    # el3.click()
    # sleep(2)
    # logpage.quit()
     print("你好")
    # bugtxt = group_txt()
    # print(bugtxt)
    # bg = bugtxt.split("截图：")
    # print(bugtxt.split("截图："))
    # print(bg[0])
    # new_bg = []
    # for i in bg:
    #     i=i.strip()
    #     new_bg.append(i)
    # print(new_bg)
    # print("=="*30)
    # print(newbg())

