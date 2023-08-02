import time

import utilities.custom_logger as cl
import logging
from base.base_page import BasePage


class RgisterForCourses(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search_box = "//input[@id='search']"
    _click_search = "//i[@class='fa fa-search']"
    _course = "//a[@href='/courses/javascript-for-beginners']"
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num = "//input[@placeholder='Card Number']"
    _cc_exp = "//input[@placeholder='MM / YY']"
    _cc_cvv = "//input[@placeholder='Security Code']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']" # need to do better
    _enroll_error_msg = "//div[@role='alert']//p[@class='dynamic-text']"

    def allCourses(self, coursesAll):
        self.elementClick(coursesAll, self._all_courses)

    def enterCourseName(self, courseName):
        self.sendKeys(courseName, self._search_box)

    def selectCourse(self, selectCourse):
        self.elementClick(selectCourse, self._course)

    def
