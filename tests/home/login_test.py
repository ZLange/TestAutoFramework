import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import time
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccess()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test@email.com", "abczzzzzzzabc")
        time.sleep(3)
        result = self.lp.verifyLoginFailed()
        assert result == True


