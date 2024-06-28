import time
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
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
# time.sleep(5)
# # driver.swipe(100, 800, 100, 500)
# print(driver.find_element_by_id("com.ss.android.article.news:id/ayx").location)
# driver.swipe(300, 120, 100, 120)
# driver.find_element_by_xpath("//*[@content-desc='图片']").click()

srcL = driver.find_element(By.XPATH, "//*[@text='更多']")
endL = driver.find_element(By.XPATH, "//*[@text='建议']")

driver.scroll(srcL, endL)

driver.drag_and_drop(srcL, endL)
driver.quit()
