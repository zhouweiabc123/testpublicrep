from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

#WebDriverWait
print('加载驱动打开浏览器')
drive = webdriver.Chrome()
drive.implicitly_wait(5)
drive.get('https://www.baidu.com/')
drive.maximize_window()
sleep(3)
print('定位到元素并输入关键字')
baidu_input = drive.find_element('id','kw')
baidu_input.send_keys('随地吐痰')
sleep(3)
print('点击')
bt = drive.find_element('id','su')
bt.click()
sleep(3)
windows1 = '//*[@id="hotsearch-content-wrapper"]/li[2]/a/span[2]'
drive.back()
sleep(2)
shouye = drive.find_element('xpath', '//*[@id="hotsearch-content-wrapper"]/li[2]/a/span[2]')
shouye.click()
sleep(3)
handles = drive.window_handles
print(handles)
sleep(3)
drive.switch_to.window(handles[-1])
sleep(2)
new_input = drive.find_element('xpath','//*[@id="kw"]')
new_input.clear()
sleep(2)
new_input.send_keys('成功切换窗口')
sleep(3)
drive.switch_to.window(handles[0])
sleep(2)
action_chain = ActionChains(drive)
search_el = drive.find_element('class','s-top-login-btn c-btn c-btn-primary c-btn-mini lb')
action_chain.move_to_element(search_el)
sleep(3)
hidden_btn = drive.find_element('xpath','//*[@id="s-user-setting-menu"]/div/a[2]/span')
action_chain.click(hidden_btn)
action_chain.perform()
sleep(3)
drive.quit()

