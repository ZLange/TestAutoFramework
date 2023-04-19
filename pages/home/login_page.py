from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
# import time
class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)  # added driver instance, won't run without it !!!!!
        self.driver = driver

    # locators
    _login_link = "//a[normalize-space()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

    # replaced with methods created in selenium_driver, so that code is cleaner!!
    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailDield(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPassswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    # action methods for page elements
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterUsername(self, username):  # email
        self.sendKeys(username, self._email_field,)  # by default already used id, if xpath or something else use locatorType

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, username, password):  # functionality, what needs to be done
        self.clickLoginLink()
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLoginButton()

