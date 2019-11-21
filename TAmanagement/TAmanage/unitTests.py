from django.test import TestCase
from .models import Course, User


class CourseTestCase(TestCase):
    # Simon: Course Test Cases
    def setUp(self):
        Course.objects.create(name="CS361", isCourseFull=False, dates="TR", startTime='11:00', endTime='11:50')
        Course.objects.create(name="CS395", isCourseFull=True, dates="MW", startTime='1:00', endTime='2:00')
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
        end = course.getEndTime()
        course.setEndTime('14:00')
        self.assertEqual(course.getEndTime(), end)

    # test invalid dates for course
    def test_course_invalid_dates(self):
        course = Course.objects.get(name='CS361')
        dates = course.getDates()
        course.setDates('XZ')
        self.assertEqual(course.getDates(), dates)


class UserTestCase(TestCase):
    # Arif: User Unit Tests
    def test_user1(self):
        user11 = User()
        user11.userEmail = "hossain8@uwm.edu"
        self.assertEqual(user11.getUsername(), "hossain8@uwm.edu")
        self.assertNotEqual(user11.getUsername(), "pqr@uwm.edu")

    def test_user2(self):
        user31 = User()
        user31.userEmail = None
        self.assertRaises(Exception, user31.getUsername())
        user31.userEmail = "hossain8"
        self.assertEqual(user31.getUsername(), "hossain8@uwm.edu", 'Not valid username')
        user31.userEmail = 5
        self.assertRaises(Exception, user31.getUsername())

    def test_userType(self):
        user21 = User()
        user21.user_type = 'MA'
        self.assertEqual(user21.USER_TYPES.__contains__(user21.userType()), False)
        user21.user_type = ('TA', 'TA / Grader')
        self.assertTrue(user21.USER_TYPES.__contains__(user21.userType()))

    def test_userType2(self):
        user41 = User()
        user41.user_type = ('TA', 'TA / Grader')
        self.assertFalse(user41.USER_TYPES.__contains__(('MA', 'ma')))
        self.assertFalse(user41.USER_TYPES.__contains__(('ta', 'TA')))
        self.assertNotEqual(user41.userType(), ('ADMIN', 'Admin'))

    def test_userType3(self):
        user51 = User()
        user51.user_type = None
        self.assertRaises(Exception, user51.getUsername())
        user51.user_type = 5
        self.assertRaises(TypeError, user51.getUsername())

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

    # Alec: Login Test Case
    def test_login_1(self):
        test_user = User.objects.get(userEmail="email")
        test_user_1 = User.objects.get(userEmail="test@test.com")
        test_user.setLoginState(True)
        test_user_1.setLoginState(True)
        self.assertFalse(test_user.loggedIn)

    # Saad: no more than one user can be logged in

    def test_login_2(self):
        user1 = User.objects.create(userEmail="user1@uwm.edu", userPassword="124test")
        user2 = User.objects.create(userEmail="user2@uwm.edu", userPassword="user2124")
        user1.setLoginState(True)
        user2.setLoginState(True)
        self.assertFalse(user2.loggedIn)
        user1.setLoginState(False)
        self.assertTrue(user2.loggedIn)

    # test admin login & logout
    def test_admin_login(self):
        admin = User.objects.create(user_type="admin", userPassword="admin123", userEmail="admin@uwm.edu")
        admin.setLoginState(True)
        self.assertTrue(admin.loggedIn)
        admin.setLoginState(False)
        self.assertFalse(admin.loggedIn)
        admin1 = User.objects.create(user_type="ADMIN", userPassword="ADMIN123", userEmail="ADMIN@uwm.edu")
        admin1.setLoginState(True)
        self.assertTrue(admin.loggedIn)
        admin1.setLoginState(False)
        self.assertFalse(admin1.loggedIn)

    # test TA login & logout

    def test_TA_login(self):
        TA = User.objects.create(user_type="TA", userPassword="TA123", userEmail="TA@uwm.edu")
        TA.setLoginState(True)
        self.assertTrue(TA.loggedIn)
        TA.setLoginState(False)
        self.assertFalse(TA.loggedIn)