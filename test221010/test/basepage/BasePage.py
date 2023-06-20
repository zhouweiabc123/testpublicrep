from time import sleep
from selenium import webdriver
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver=webdriver.Chrome()
        #self.driver=driver
        pass
    def el_find(self,element:tuple):
        '''
        封装定位
        :param element:第一个事元素定位方式，("id","#ks")
        :return: 返回元素
        '''
        el=self.driver.find_element(element[0],element[1])
        el.send_keys()

        print(el)
        return el
    def el_click(self,element):
        '''
        元素点击事件
        :param element: 定位到的元素
        :return:
        '''
        element.click()
    def el_sendkeys(self,element,eltext):
        '''
        给元素输入事件
        :param element: 定位到的元素
        :param eltext: 需要输入的内容
        :return:
        '''
        element.send_keys(eltext)
        #模拟按键
        #element.send_keys(Keys.ENTER)
    def el_clear(self,element):
        '''
        清楚元素的内容，如输入框
        :param element: 定位到的元素
        :return:
        '''
        element.clear()
    def get_handlers(self):
        ''':return: 返回窗口句柄，用于切换'''
        handles=self.driver.window_handles
        return handles
    def switch_to(self,*args):
        '''
        切换浏览器窗口或页面弹窗、等
        :param:可以是alert、frame、element...
        :return:
         element = driver.switch_to.active_element
                alert = driver.switch_to.alert
                driver.switch_to.default_content()
                driver.switch_to.frame('frame_name')
                driver.switch_to.frame(1)
                driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
                driver.switch_to.parent_frame()
                driver.switch_to.window('main')
        '''
        self.driver.switch_to.window(args)
    def refresh(self):
        '''
        刷新:return:
        '''
        self.driver.refresh()
    def close(self):
        '''
        关闭当前窗口:return:
        '''
        self.driver.close()
    def quit(self):
        '''
        退出驱动程序并关闭所有窗口 :return:
        '''
        self.driver.quit()
if __name__ == '__main__':
    print("这个是封装基本web操作的类")