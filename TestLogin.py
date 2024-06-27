import unittest
import time
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def test_login_01(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.jianhua/a.754894437.1.5af92a89DhZ7Ow&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
        time.sleep(3)
        driver.find_element_by_id("fm-login-id").send_keys("jtq")
        driver.find_element_by_id("fm-login-password").send_keys("jtq222")
        driver.find_element_by_xpath("//button[@class='fm-button fm-submit password-login']").click()
        time.sleep(10)