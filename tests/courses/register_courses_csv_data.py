from pages.courses.register_for_course import RegisterForCourses
from utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
import time
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterForCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterForCourses(self.driver)
        self.ts = TestStatus(self.driver)

    def setUp(self):
        self.driver.find_element_by_link_text("All Courses").click()   # to get all courses

    @pytest.mark.run(order=1)
    @data(*getCSVData("fill with csv file path"))  # can provide only file name if file is in project folder
    @unpack
    def test_invalidEnrollment(self, cName, cNum, cExp, cCVV):
        # self.courses.allCourses()
        self.courses.enterCourseName(courseName=cName)
        time.sleep(1)
        self.courses.selectCourseToEnroll()
        time.sleep(1)
        self.courses.enterCardNum(cardNum=cNum)
        time.sleep(1)
        self.courses.enterCardExp(cardExp=cExp)
        time.sleep(1)
        self.courses.enterCardCVV(cardcvv=cCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        # # click all courses
        # self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
