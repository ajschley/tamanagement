from django.test import TestCase
from .views import Home


class CourseTestCase(TestCase):

    def test_createCourse1(self):
        Home.POST("createCourse CS361 11:00 11:50 TR")
        self.assertEqual(Home.response, 'CS361 was created.')

    def test_createCourseNoDates(self):
        Home.POST("createCourse CS361 11:00 11:50")
        self.assertEqual(Home.response, 'Error. Need All 4 Arguments.')

    def test_createCourseNoEndTime(self):
        Home.POST("createCourse CS361 11:00 TR")
        self.assertEqual(Home.response, 'Error. Need All 4 Arguments.')

    def test_createCourseNoName(self):
        Home.POST("createCourse")
        self.assertEqual(Home.response, 'Error. Need All 4 Arguments.')


class UserTestCase(TestCase):

    def test_createUser1(self):
        Home.POST("createUser example@uwm.edu password TA")
        self.assertEqual(Home.response, 'example@uwm.edu was created.')

    def test_createCourseNoType(self):
        Home.POST("createUser example@uwm.edu password")
        self.assertEqual(Home.response, 'Error. Need All 3 Arguments.')

    def test_createCourseNoPassword(self):
        Home.POST("createUser example@uwm.edu")
        self.assertEqual(Home.response, 'Error. Need All 3 Arguments.')

    def test_createCourseNoName(self):
        Home.POST("createUser")
        self.assertEqual(Home.response, 'Error. Need All 3 Arguments.')
