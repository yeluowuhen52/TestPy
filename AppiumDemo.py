import time
from appium import webdriver

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = '127.0.0.1:7555'
#今日头条
desired_caps['appPackage'] = 'com.ss.android.article.news'
desired_caps['appActivity'] = 'com.ss.android.article.news.activity.MainActivity'

# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = 'com.android.settings.SubSettings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.quit()