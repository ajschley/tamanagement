from django.test import TestCase
from .models import Course, User


class CourseTestCase(TestCase):
    # Simon: Course Test Cases
    def setUp(self):
        Course.objects.create(name="CS361", isCourseFull=False, dates="TR")
        Course.objects.create(name="CS395", isCourseFull=True, dates="MW")
        Course.objects.create(name="CS482", isCourseFull=False, dates="Online")

    def test_course_return(self):
        course361 = Course.objects.get(name="CS361")
        self.assertEqual(course361.courseName(), 'CS361')

    def test_course_not_full(self):
        course361 = Course.objects.get(name="CS361")
        self.assertFalse(course361.isFull())

    def test_course_full(self):
        course395 = Course.objects.get(name="CS395")
        self.assertTrue(course395.isFull())

    def test_course_online(self):
        course482 = Course.objects.get(name="CS482")
        self.assertTrue(course482.isOnline())

    def test_course_not_online(self):
        course395 = Course.objects.get(name="CS395")
        self.assertFalse(course395.isOnline())

    def test_course_dates(self):
        course361 = Course.objects.get(name="CS361")
        self.assertEqual(course361.getDates(), 'TR')


class UserTestCase(TestCase):
    # Arif: User Unit Tests
    def test_user(self):
        user11 = User()
        user11.userEmail = "hossain8@uwm.edu"
        self.assertEqual(user11.username(), "hossain8@uwm.edu")
        self.assertNotEqual(user11.username(), "pqr@uwm.edu")

    def test_userType(self):
        user21 = User()
        user21.user_type = 'MA'
        self.assertEqual(user21.USER_TYPES.__contains__(user21.userType()), False)
        user21.user_type = ('TA', 'TA / Grader')
        self.assertTrue(user21.USER_TYPES.__contains__(user21.userType()))
        self.assertFalse(user21.USER_TYPES.__contains__(('MA', 'ma')))
        self.assertFalse(user21.USER_TYPES.__contains__(('ta', 'TA')))
        self.assertNotEqual(user21.userType(), ('ADMIN', 'Admin'))

    def test_loggedIn(self):
        user31 = User()
        self.assertFalse(user31.loggedIn)
        user31.loggedIn = True
        self.assertTrue(user31.loggedIn)

    # Saad: more user Unit test

    # test for setting a password for a new user
    def test_password(self):
        user41 = User()
        user41.userPassword = "Stc123"
        self.assertEqual(user41.resetPassword(), "Stc123")
        self.assertNotEqual(user41.resetPassword(), "Stc124")
        user41.userPassword = None
        self.assertFalse(user41.resetPassword(), "error: enter a password")

    # test user email only valid uwm email

    def tes_userEmail(self):
        user51 = User()
        user51.userEmail = "saad_q95@gamil.com"
        self.assertFalse(user51.username(), "use a valid uwm email")
        user51.userEmail = "alqaht78@uwm.edu"
        self.assertEqual(user51.username(), "alqaht78@uwm.edu")
        user51.userEmail = None
        self.assertRaises(user51.username(), TypeError)
        self.assertFalse(user51.username(), "error: enter a valid email")



