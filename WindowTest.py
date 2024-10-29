import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.maximize_window()

print(driver.title)

time.sleep(3)

driver.find_element_by_xpath('//*[@id="kw"]').send_keys("蜡笔小新")

driver.find_element_by_xpath('//*[@id="kw"]').click()
# driver.quit()