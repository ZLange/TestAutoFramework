from pages.courses.register_for_course import RegisterForCourses
from utilities.test_status import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterForCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterForCourses(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript", "5500 0000 0000 0004", "0525", "444"),("Learn Python 3 from scratch", "20", "1220", "20"))
    @unpack
    def test_invalidEnrollment(self, cName, cNum, cExp, cCVV):
        # self.courses.allCourses()
        self.courses.enterCourseName(courseName=cName)
        self.courses.selectCourseToEnroll()
        # self.courses.enrollCourse(cardNum = cNum, cardExp=cExp, cardcvv=cCVV)
        self.courses.enterCardNum(cardNum=cNum)
        self.courses.enterCardExp(cardExp=cExp)
        self.courses.enterCardCVV(cardcvv=cCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        # click all courses
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
