import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys('python')
time.sleep(3)
driver.find_element_by_id("kw").clear()
time.sleep(3)
driver.find_element_by_id("kw").send_keys('测试')
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()