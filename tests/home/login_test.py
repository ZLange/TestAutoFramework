from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
# import time
import unittest

class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        baseURL = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")


        user_icon = driver.find_element(By.XPATH, "//img[@class='zl-navbar-rhs-img ']")
        if user_icon is not None:
            print("Login successful ")
        else:
            print("Login Failed")


