import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# driver.find_element_by_id("kw").send_keys('python')
# driver.find_element_by_class_name("s_ipt").send_keys('python')
# driver.find_element_by_name("wd").send_keys('python')
# driver.find_element_by_tag_name("input").send_keys('python')
# driver.find_element_by_link_text("hao123").click()
# driver.find_element_by_partial_link_text("hao123").click()

# XPath属性定位
# 路径定位
# /html/body/div/div[1]/div[5]/div/div/form/span/input
# //form/span/input
#属性定位
# //input[@id="kw"]
# //input[@class="s_ipt"]
# 结合
# //form[@id='form']/span/input
# driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys('python')

# css定位
# id选择器
# #kw
# class选择器 .s_ipt
# 属性选择器 [id=kw] [class=s_ipt]
# 层级选择器 #form>span>#kw 隔代：#form #kw #form [id="kw"]
driver.find_element_by_css_selector("#form [id='kw']").send_keys('python')

time.sleep(3)
driver.quit()