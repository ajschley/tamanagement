from django.test import TestCase
from datetime import datetime
from .models import Course, User


class CourseTestCase(TestCase):
    # Simon: Course Test Cases
    def setUp(self):
        Course.objects.create(name="CS361", section="001", dates="TR", startTime='11:00:00', endTime='11:55:00')
        Course.objects.create(name="CS395", section="001", dates="MW", startTime='1:00', endTime='2:00')
        Course.objects.create(name="CS482", section="001", dates="Online")

    def test_course_1(self):
        course361 = Course.objects.get(name="CS361")
        self.assertEqual(course361.courseName(), 'CS361')

    def test_course_2(self):
        course361 = Course.objects.get(name="CS395")
        self.assertEqual(course361.courseName(), 'CS395')

    def test_course_3(self):
        course361 = Course.objects.get(name="CS482")
        self.assertEqual(course361.courseName(), 'CS482')

    def test_course_4(self):
        course361 = Course.objects.get(name="CS361")
        self.assertNotEqual(course361.courseName(), 'CS362')

    def test_course_5(self):
        course361 = Course.objects.get(name="CS395")
        self.assertNotEqual(course361.courseName(), 'CS396')

    def test_course_6(self):
        course361 = Course.objects.get(name="CS482")
        self.assertNotEqual(course361.courseName(), 'CS483')

    def test_course_7(self):
        course361 = Course.objects.get(name="CS361")
        self.assertEqual(course361.section, '001')

    def test_course_8(self):
        course361 = Course.objects.get(name="CS395")
        self.assertEqual(course361.section, '001')

    def test_course_9(self):
        course361 = Course.objects.get(name="CS482")
        self.assertEqual(course361.section, '001')

    def test_course_10(self):
        course361 = Course.objects.get(name="CS361")
        self.assertNotEqual(course361.section, 'CS362')

    def test_course_11(self):
        course361 = Course.objects.get(name="CS395")
        self.assertNotEqual(course361.section, 'CS396')

    def test_course_12(self):
        course361 = Course.objects.get(name="CS482")
        self.assertNotEqual(course361.section, 'CS483')

    def test_course_13(self):
        course361 = Course.objects.get(name="CS361")
        self.assertEqual(course361.startTime.strftime('%H:%M:%S'), '11:00:00')



    def test_course_not_full(self):
        course361 = Course.objects.get(name="CS361")
        self.assertFalse(course361.isFull())

    def test_course_full(self):
        course395 = Course.objects.get(name="CS395")
        self.assertTrue(course395.isFull())

    # Ben: Course Test Cases
    def test_course_online(self):
        course482 = Course.objects.get(name="CS482")
        self.assertTrue(course482.isOnline())

    def test_course_not_online(self):
        course395 = Course.objects.get(name="CS395")
        self.assertFalse(course395.isOnline())

    def test_course_dates(self):
        course361 = Course.objects.get(name="CS361")
        self.assertEqual(course361.getDates(), 'TR')

    # Alec: Course Test Cases
    # test start time for a course

    def test_course_start(self):
        course361 = Course()
        course361.startTime = "11:00"
        self.assertEqual(course361.getStartTime(), "11:00")
        self.assertNotEqual(course361.getStartTime(), "11:50")

    # test end time for a course
    def test_course_end(self):
        course361 = Course()
        course361.endTime = "11:50"
        self.assertEqual(course361.getEndTime(), "11:50")
        self.assertNotEqual(course361.getEndTime(), "11:00")

    # test the online class doesn't have start or end time
    def test_course_online_time(self):
        course482 = Course()
        course482.dates = "Online"
        self.assertEqual(course482.getStartTime(), None)
        self.assertEqual(course482.getEndTime(), None)

    # test the online class doesn't have dates
    def test_course_online_dates(self):
        course = Course.objects.get(name='CS361')
        dates = course.getDates()
        self.assertEqual(dates, None)

    # test invalid start time for course
    def test_course_start_invalid(self):
        course = Course.objects.get(name='CS395')
        start = course.getStartTime()
        course.setStartTime('13:00')
        self.assertEqual(course.getStartTime(), start)

    # test invalid end time for course
    def test_course_end_invalid(self):
        course = Course.objects.get(name='CS395')
        end = course.endTime
        course.endTime = '25:00'
        self.assertNotEqual(course.endTime, end)

    # test invalid dates for course
    def test_course_invalid_dates(self):
        course = Course.objects.get(name='CS361')
        dates = course.getDates()
        course.setDates('XZ')
        self.assertEqual(course.getDates(), dates)


class UserTestCase(TestCase):
    # Arif: User Unit Tests
    def test_user(self):
        user11 = User()
        user11.userEmail = "hossain8@uwm.edu"
        self.assertEqual(user11.getUsername(), "hossain8@uwm.edu")
        self.assertNotEqual(user11.getUsername(), "pqr@uwm.edu")

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

    def test_userEmail(self):
        user51 = User()
        user51.userEmail = "saad_q95@gamil.com"
        self.assertFalse(user51.getUsername(), "use a valid uwm email")
        user51.userEmail = "alqaht78@uwm.edu"
        self.assertEqual(user51.getUsername(), "alqaht78@uwm.edu")
        user51.userEmail = None
        self.assertRaises(user51.getUsername(), TypeError)
        self.assertFalse(user51.getUsername(), "error: enter a valid email")


class LoginTestCase(TestCase):
    # Chris: Login Test Cases
    def setUp(self):
        User.objects.create(userEmail="test@test.com", userPassword="test")
        User.objects.create(userEmail="email", userPassword="password")

    def test_login(self):
        testUser = User.objects.get(userEmail="test@test.com")
        self.assertFalse(testUser.loggedIn)
        testUser.setLoginState(True)
        self.assertTrue(testUser.loggedIn)
        testUser.setLoginState(False)
        self.assertFalse(testUser.loggedIn)


class EditCourseTestCase(TestCase):

    def setUp(self):
        Course.objects.create(name="CS361", section="001", dates="TR", startTime='11:00:00', endTime='11:55:00')
        Course.objects.create(name="CS395", section="001", dates="MW", startTime='1:00', endTime='2:00')
        Course.objects.create(name="CS482", section="001", dates="Online")

    def test_edit_course_section(self):
        course = Course.objects.get(name="CS361")
        course.section = "002"
        course.save()
        self.assertEqual("002", course.section)

    def test_edit_course_dates(self):
        course = Course.objects.get(name="CS361")
        course.dates = "MW"
        course.save()
        self.assertEqual("MW", course.dates)

    def test_edit_course_start_time(self):
        course = Course.objects.get(name="CS361")
        course.startTime = "11:30:00"
