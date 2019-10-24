import unittest
from unittest import TestCase
from CourseTime import CourseTime


class TestCourseTime(TestCase):      ##TA: unittest.Test case to inherit

    def test_init_valid(self):
        CourseTime.__init__("12:00 14:00 S")
        assert(self.__str__() == "12:00 14:00 S")

    def test_init_sunday(self):
        try:
            CourseTime.__init__("12:00 14:00 SS")
            assert False
        except (ValueError):
            assert True, "Exception thrown."

    def test_init_int(self):
        try:
            CourseTime.__init__(1)
            assert False
        except (TypeError):
            assert True, "Exception thrown."

    def test_init_invalid(self):
        try:
            CourseTime.__init__("25:00 27:00 R")
            assert False
        except (ValueError):
            assert True, "Exception thrown."

    def test_init_invalid2(self):
        try:
            CourseTime.__init__("13:00 16:00 7") ##TA :  why are you using 7 here???
            assert False
        except (ValueError):
            assert True, "Exception thrown."

    def test_str_same(self):
        CourseTime.__init__("11:00 12:50 T")
        self.assertEquals("11:00 12:50 T", CourseTime.__str__())

    def test_str_online(self):
        CourseTime.__init__("online")
        self.assertEquals("online", CourseTime.__str__())

    def test_start_same(self):
        CourseTime.__init__("11:00 12:50 T")
        self.assertEquals("11:00", CourseTime.__start__())

    def test_start_online(self):
        CourseTime.__init__("online")
        self.assertEquals("00:00", CourseTime.__start__())

    def test_end_same(self):
        CourseTime.__init__("11:00 12:50 T")
        self.assertEquals("12:50", CourseTime.__end__())

    def test_end_online(self):
        CourseTime.__init__("online")
        self.assertEquals("00:00", CourseTime.__end__())

    def test_isOnline_false(self):
        CourseTime.__init__("11:00 12:50 T")
        self.assertFalse(CourseTime.__isOnline__())

    def test_isOnline_true(self):
        CourseTime.__init__("online")
        self.assertTrue(CourseTime.__isOnline__())

    def test_isOverlap_false(self):
        time1 = CourseTime.__init__("11:00 12:50 T")
        time2 = CourseTime.__init__("10:00 10:50 T")
        self.assertFalse(time1.__isOverlap__(time2))

    def test_isOverlap_true(self):
        time1 = CourseTime.__init__("11:00 12:50 T")
        time2 = CourseTime.__init__("10:00 11:50 T")
        self.assertTrue(time1.__isOverlap__(time2))

    if __name__ == '__main__':
        unittest.main()

###TA: Try to write test suite and Texttest runner. Come up with even more test cases.