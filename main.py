from selenium import webdriver
from config import SELENIUM_CONFIG
driver = webdriver.Chrome(SELENIUM_CONFIG['chrome_driver_path'])


driver.get('https://www.naver.com')
driver.implicitly_wait(3)
driver.find_element_by_class_name('lg_local_btn').click()
driver.find_element_by_name('id').send_keys('aaa')
driver.find_element_by_name('pw').send_keys('aaa')
driver.implicitly_wait(3)

# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.find_element_by_class_name('btn_global').click()
