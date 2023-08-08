import time

import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class RegisterForCourses(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    #_all_courses = "course-listing-title"
    _search_box = "search"
    _search_course_icon = "//i[@class='fa fa-search']"
    _course = "//a[@href='/courses/javascript-for-beginners']"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _card_num = "//input[@placeholder='Card Number']"
    _card_exp = "//input[@placeholder='MM / YY']"
    _card_cvv = "//input[@placeholder='Security Code']"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']/parent::div"

    # after login go to all courses
    def allCourses(self):
        self.getElement(locator=self._all_courses, locatorType='xpath' )
        self.elementClick(locator=self._all_courses)

    def enterCourseName(self, courseName):
        self.sendKeys(courseName, locator=self._search_box, locatorType='id')
        self.elementClick(locator=self._search_course_icon)

    def selectCourseToEnroll(self):
        self.elementClick(locator=self._course)

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, cardNum):
        # self.switchToFrame(name="__privateStripeFrame4")
        self.sendKeys(cardNum, locator=self._card_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, cardExp):
        # self.switchToFrame(name="__privateStripeFrame5")
        self.sendKeys(cardExp, locator=self._card_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cardcvv):
        # self.switchToFrame(name="__privateStripeFrame6")
        self.sendKeys(cardcvv, locator=self._card_cvv, locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self):
        # self.switchToFrame(name="__privateStripeFrame7")
        self.sendKeys(zip, locatorType="name")
        self.switchToDefaultContent()

    def clickAgreeToTermsCheckbox(self):
        self.elementClick(locator=self._agree_to_terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickAgreeToTermsCheckbox()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result

