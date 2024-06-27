import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

test = driver.find_element_by_xpath("//div[@class='s_form s_form_nologin']/div/div[3]/ul/li/a/span[2]").text
print(test)
time.sleep(3)
driver.quit()