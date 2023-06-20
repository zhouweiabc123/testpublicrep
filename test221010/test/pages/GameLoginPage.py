from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from test221010.test.basepage.BasePage import BasePage
from selenium import webdriver

class GameLoginPage(BasePage):
    url="https://h5.hhygames.com/dfs/h5SDK/?gameId=32#/register"
    def __init__(self,driver):
        super().__init__(driver=driver)
        self.driver.get(url=self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def login(self):
        '''
        登录页面
        :return:
        '''
        print("登录页面的一些操作")
        pass
        # ac=ActionChains(self.driver)
        # ac.move_to_element(return_span).click().perform()
        # ac.click(return_span)
        # ac.perform()
    def register(self):
        '''
        这里是注册页面
        :return:
        '''
        print("你好，封装的登录页")
        cancellation_bt = self.el_find(("xpath", '//*[@id="app"]/div[10]/div/div[3]/span/button[1]'))
        print("找到了拒绝按钮，准备点击")
        self.el_click(cancellation_bt)
        sleep(2)
        print("定位返回元素中...元素不可交互，可用JS解决")
        # self.driver.switch_to.active_element
        # 元素不可交互，解决办法，用JS或JQuery点击
        # js="$('#app > div:nth-child(11) > div > div.el-dialog__body > div > span').click"
        js = "document.querySelector('#app > div:nth-child(11) > div > div.el-dialog__body > div > span').click();"
        self.driver.execute_script(js)
        print("使用js点击元素")
        # return_span=self.el_find(("xpath",'//*[@id="app"]/div[11]/div/div[2]/div/span'))
        print("找到了返回 span 元素，准备点击返回：")
        ##app > div:nth-child(11) > div > div.el-dialog__body > div > span
        try:
            pass
            # return_span.click()
        except Exception as e:
            print(e)
        print("已返回协议确认页")
    def look(self):
        '''
        隐私协议
        :return:
        '''
        print("看协议的WEB操作")
        pass
if __name__ == '__main__':
    print("创建GameloginPage对象")
    driver=1
    gl=GameLoginPage(driver=driver)
    gl.login()
    gl.look()
    gl.register()
