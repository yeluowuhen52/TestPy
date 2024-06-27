import time
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = '127.0.0.1:7555'
# 今日头条
# desired_caps['appPackage'] = 'com.ss.android.article.news'
# desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'

# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = 'com.android.settings.SubSettings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 启动今日头条
print(driver.current_package + '---' + driver.current_activity)
driver.start_activity("com.ss.android.article.news", "com.ss.android.article.news.activity.MainActivity")
print(driver.current_package + '33333---' + driver.current_activity)

# titles = driver.find_elements_by_id("com.ss.android.article.news:id/hkx")
# print(len(titles))
#
#
# for title in titles:
#     txt = title.text[0:3]
#     print(title.text)
#
# path = "//*[contains(@text,'"+ txt+ "')]"
# print(path)
# titles2 = driver.find_elements_by_xpath(path)
# print(len(titles2))

driver.find_element(By.ID, "com.ss.android.article.news:id/h6m").click()
# driver.find_element_by_id("com.ss.android.article.news:id/h6m").click()

driver.quit()
