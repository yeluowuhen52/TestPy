import time
from appium import webdriver

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

# driver.background_app("com.ss.android.article.news")

driver.find_element_by_id("com.ss.android.article.news:id/h6m").click()
time.sleep(5)
driver.find_element_by_id("com.ss.android.article.news:id/d0").send_keys("测试")
driver.find_element_by_id("com.ss.android.article.news:id/e2").click()

# time.sleep(5)
# driver.terminate_app("com.ss.android.article.news")

# print(driver.is_app_installed("com.ss.android.article.news"))

# driver.install_app("D:\头条搜索极速版.apk")

driver.quit()
