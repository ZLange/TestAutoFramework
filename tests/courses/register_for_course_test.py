from pages.courses.register_for_course import RegisterForCourses
from utilities.test_status import TestStatus
import unittest
import pytest

import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterForCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterForCourses(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.allCourses()
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll()
        self.courses.enrollCourse(num="5500 0000 0000 0004", exp="0525", cvv="444")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
