from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginTests:

    def test_valid_login(self):
        baseURL = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        login_link = driver.find_element(By.XPATH, "//a[normalize-space()='Sign In']")
        login_link.click()

        time.sleep(3)  # use also if see CAPTCHA

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("test@email.com")

        time.sleep(3)

        password_field = driver.find_element(By.ID, "login-password")
        password_field.send_keys("abcabc")

        time.sleep(3)

        login_button = driver.find_element(By.ID, "login")
        login_button.click()

        user_icon = driver.find_element(By.XPATH, "//img[@class='zl-navbar-rhs-img ']")
        if user_icon is not None:
            print("Login successful ")
        else:
            print("Login Failed")


ch = LoginTests()
ch.test_valid_login()
