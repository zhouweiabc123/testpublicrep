from time import sleep
from test221010.test.pages.ocr import identifyImg
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from test221010.test.basepage.BasePage import BasePage


class GameLoginPage(BasePage):
    url="https://h5-dev.hhygames.com/dfs/h5SDK/?gameId=32#/register"
    login_url="https://h5-dev.hhygames.com/dfs/h5SDK/?gameId=32#/accountLogin"
    quick_login_url="https://h5-dev.hhygames.com/dfs/h5SDK/?gameId=32#/login"
    username=''
    password=''
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
        print("你好，封装的登录页")
        # 继续打开新标签页，正常登录页面
        self.driver.switch_to.new_window()
        self.driver.get(self.login_url)
        #定位账号框和密码框
        user_input=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[1]/div/div/div/input'))
        password_input = self.el_find(
            ("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[2]/div/div/div/input'))
        print(self.username+"----"+self.password)
        print(user_input)
        # 输入事先保存的账号和密码
        self.el_sendkeys(user_input, self.username)
        sleep(1)
        password_input.send_keys(self.password)
        sleep(1)
        print("输入账号密码成功！")
        #第一次进来用账号密码正常登录，处理验证码用ocr识别
        login_check_img = "./check.png"
        check_img_element = self.el_find(("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[3]/div/div/div/div/img'))
        check_img_element.screenshot(login_check_img)
        sleep(1)
        check_code=identifyImg(login_check_img)
        #定位验证码输入框，输入图片验证码
        check_input=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[3]/div/div/div/input'))
        check_input.send_keys(check_code)
        print("输入图片验证码成功")
        sleep(2)
        #勾选协议和隐私政策
        check_box=self.driver.find_element("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[4]/div/div/label')
        #check_box.click()
        #点击登录
        login_bt=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[5]/div/div/button'))
        self.el_click(login_bt)
        sleep(1)
        print("登录页面的一些操作")
        #回到快速登录页
        self.driver.get(self.quick_login_url)
        sleep(1)
        print("现在在快速登录页，准备快速登录")
        #定位快速登录按钮，点击快速登录进去游戏里
        quick_login_bt=self.driver.find_element("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[3]/button')
        self.el_click(quick_login_bt)
        sleep(1)
        print("进入了游戏选服页面")
        #定位SDK功能浮标，点击显示功能入口弹窗
        icon_img_bt=self.el_find(("xpath",'//*[@id="app"]/div[3]'))
        icon_img_bt.click()
        print("点击！")
        sleep(1)
        #定位修改密码，然后点击
        update_password_icon=self.el_find(("xpath",'//*[@id="app"]/div[4]/div/div/section/div/div/div[2]/div[1]/i[1]'))
        self.el_click(update_password_icon)
        sleep(1)
        self.driver.refresh()
        # ac=ActionChains(self.driver)
        # ac.move_to_element(return_span).click().perform()
        # ac.click(return_span)
        # ac.perform()
    def register(self):
        '''
        这里是注册页面
        :return:
        '''
        print("你好，封装的注册页")
        cancellation_bt = self.el_find(("xpath", '//*[@id="app"]/div[10]/div/div[3]/span/button[1]'))
        print("找到了拒绝按钮，准备点击")
        self.el_click(cancellation_bt)
        sleep(2)
        print("定位返回元素中...元素不可交互，可用JS解决")
        # self.driver.switch_to.active_element
        # 元素不可交互，解决办法，用JS或JQuery点击
        # js="$('#app > div:nth-child(11) > div > div.el-dialog__body > div > span').click"

        print("使用js点击元素")
        # return_span=self.el_find(("xpath",'//*[@id="app"]/div[11]/div/div[2]/div/span'))
        js = "document.querySelector('#app > div:nth-child(11) > div > div.el-dialog__body > div > span').click();"
        self.driver.execute_script(js)
        print("找到了确定按钮，准备点击确定：")
        sleep(2)
        ##app > div:nth-child(11) > div > div.el-dialog__body > div > span
        #回到一开始打开的页面，点击确定
        define_bt=self.el_find(("xpath",'//*[@id="app"]/div[10]/div/div[3]/span/button[2]'))
        self.el_click(define_bt)
        print("进入登录注册页了")
        print("定位到协议勾选框")
        check_box=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[4]/div/div[1]/label'))
        print("是否勾选：", check_box.is_selected())
        sleep(1)
        check_box.click()
        #获取元素的一些属性，以此来判断
        class_value=check_box.get_attribute("class")
        print(class_value)
        print(type(class_value))
        print("点击勾选同意协议后的check_box：",check_box.is_selected())
        sleep(1)
        print("注册游客账号，先定位到 游客登录 按钮，这里用显示等待，元素出现才点击")
        #显示等待
        tourister_bt=WebDriverWait(self.driver,5,0.5).until(lambda x:self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[6]/div/div/button')))
        self.el_click(tourister_bt)
        print("游客注册成功")
        sleep(1)
        # 正常登录
        # user_input = self.el_find(
        #     ("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[1]/div/div/div/input'))
        # password_input = self.el_find(
        #     ("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[2]/div/div/div/input'))
        #快速登录
        # user_input = self.el_find(("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/input'))
        # password_input = self.el_find(("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/input'))
        # 为了方便登录，获取到账号密码保存下来，返回
        # 第一步，定位到账号输入框，密码输入框,在快速登录
        user_input=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[1]/div/input'))
        password_input=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/input'))
        self.username=user_input.get_attribute('value')
        self.password=password_input.get_attribute('value')
        print(self.username)
        print(self.username)
        # 图片验证码处理
        # imgcheck_input=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[3]/div/div/div/input'))
        # img_check=self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[3]/div/div/div/div/img'))
        # print("图片验证码类型：",type(img_check))
        # 第二步，获取账号密码保存起来
        # 第三步，跳转到登录页面输入账号密码登录进游戏里面
        # 快速登录，去到正确的页面，直接操作快速登录即可
        print("去登录游客账号")
        print("先找到 复制账号并登录按钮，使用显示等待，元素出现才点击")
        copy_login_bt=WebDriverWait(self.driver,5,0.5).until(lambda x: self.el_find(("xpath",'//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[1]/div[3]/button')))
        print("已定位到元素：",copy_login_bt)
        sleep(1)
        self.el_click(copy_login_bt)
        print("点击登录游戏，进入成功！游客注册操作完成！")
        sleep(3)
        #为了方便登录，获取到账号密码保存下来，返回
        #self.el_click(check_box)
        try:
            pass
            # return_span.click()
        except Exception as e:
            print(e)
        self.driver.switch_to.new_window()
        sleep(1)
        #self.driver.get("https://h5-dev.hhygames.com/dfs/h5SDK/?gameId=32#/login")#快速登录
        self.driver.get(self.login_url)#正常登录
        sleep(2)
        #找到验证码图片元素
        img_check = self.el_find(
            ("xpath", '//*[@id="app"]/div[2]/div/div[2]/div/div/div/div/form/div[3]/div/div/div/div/img'))
        print("图片验证码类型：", type(img_check))
        print(img_check.get_attribute("src"))
        #self.driver.get(img_check.get_attribute("src"))
        sleep(2)
        #check_img=self.driver.get_screenshot_as_base64()
        #保存验证码截图
        el_check_img=img_check.screenshot("./el.png")
        print("保存验证码截图成功！")
        sleep(1)
        print("识别保存的图片验证码")
        for i in range(2):
            #多次识别，确保正确
            identifyImg("el.png")
            # 如果识别后输入的验证码不对，点击更换换验证码，继续识别，一张验证码识别3次，
            # 直到识别出来可以登录成功为止，或者限制验证码更换次数去识别，最后识别不出来就跳过换到快速登录

        #save_img=self.driver.save_screenshot("./el.png")#保存整个浏览器截图
        #print(check_img)
        print("返回")
        handlers=self.driver.window_handles
        sleep(3)
        #self.driver.close()
        #继续打开新标签页，正常登录页面
        # self.driver.switch_to.new_window()
        # self.driver.get(self.login_url)

        #跳转回第一个标签页
        #self.driver.switch_to.window(handlers[0])
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
    gl.register()
    gl.login()
    gl.look()

