from selenium import webdriver
from time import sleep
import group_bug
driver = webdriver.Chrome()
group_bug.login(driver)

# creat_bt = driver.find_element('xpath','//*[@id="create_link"]')
# creat_bt.click()
driver.quit()

