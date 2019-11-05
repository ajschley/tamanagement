from django.test import TestCase
from .models import Course, User, CourseCreation


class CourseTestCase(TestCase):
    def setUp(self):
        Course.objects.create(name="CS361", isCourseFull=False)
        Course.objects.create(name="CS395", isCourseFull=True)

    def test_course_return(self):
        course1 = Course.objects.get(name="CS361")
        self.assertEqual(course1.courseName(), 'CS361')

    def test_course_not_full(self):
        course1 = Course.objects.get(name="CS361")
        self.assertFalse(course1.isFull())

    def test_course_full(self):
        course2 = Course.objects.get(name="CS395")
        self.assertTrue(course2.isFull())

# user unittests
    def test_user(self):
        user11 = User()
        user11.userEmail = "hossain8"
        self.assertEqual(user11.username(), "hossain8")

    def test_userType(self):
        user11 = User()
        user11.user_type = 'MA'
        self.assertEqual(user11.USER_TYPES.__contains__(user11.userType()), False)
        user12 = User()
        user12.user_type = ('TA', 'TA / Grader')
        self.assertTrue(user12.USER_TYPES.__contains__(user12.userType()))
        self.assertFalse(user12.USER_TYPES.__contains__(('MA', 'ma')))
        self.assertFalse(user12.USER_TYPES.__contains__(('ta', 'TA')))

