from django.test import TestCase
from datetime import datetime

from TAmanage.commands import CommandWorker
from .models import Course, User


class CourseTestCase(TestCase):
    # Simon: Course Test Cases
    def setUp(self):
        Course.objects.create(name="CS361", isCourseFull=False, section="001", dates="TR", startTime='11:00:00', endTime='11:55:00')
        Course.objects.create(name="CS395", isCourseFull=True, section="001", dates="MW", startTime='1:00', endTime='2:00')
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

    # test invalid start time for course
    def test_course_start_invalid(self):
        course = Course.objects.get(name='CS395')
        start = course.getStartTime()
        course.setStartTime('25:00')
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
    def test_user_email(self):
        user11 = User()
        user11.email = "hossain8@uwm.edu"
        self.assertEqual(user11.email, "hossain8@uwm.edu")
        self.assertNotEqual(user11.email, "pqr@uwm.edu")

    def test_user_type(self):
        user21 = User()
        user21.role = 'MA'
        self.assertEqual(False, user21.user_type.__contains__(user21.role))
        user21.role = 'TA'
        self.assertTrue(user21.USER_TYPES.__contains__(user21.role))
        self.assertFalse(user21.USER_TYPES.__contains__('MA'))
        self.assertFalse(user21.USER_TYPES.__contains__('X'))
        self.assertNotEqual('Admin', user21.role)

    def test_loggedIn(self):
        user31 = User()
        self.assertFalse(user31.loggedIn)
        user31.loggedIn = True
        self.assertTrue(user31.loggedIn)

    # Saad: more user Unit test

    # test for setting a password for a new user
    def test_reset_password(self):
        user41 = User()
        user41.password = "Stc123"
        self.assertEqual("Stc123", user41.resetPassword())
        self.assertNotEqual("Stc124", user41.resetPassword())
        user41.userPassword = None
        self.assertFalse(user41.resetPassword(), "error: enter a password")

    # test user email only valid uwm email

    def test_user_email_2(self):
        user51 = User()
        user51.userEmail = "saad_q95@gamil.com"
        self.assertFalse(user51.getUsername(), "use a valid uwm email")
        user51.userEmail = "alqaht78@uwm.edu"
        self.assertEqual(user51.getUsername(), "alqaht78@uwm.edu")
        user51.userEmail = None
        self.assertRaises(user51.getUsername(), TypeError)
        self.assertFalse(user51.getUsername(), "error: enter a valid email")


# class LoginTestCase(TestCase):
#     # Chris: Login Test Cases
#     def setUp(self):
#         User.objects.create(email="test@test.com", password="test")
#         User.objects.create(email="email", password="password")
#
#     def test_login(self):
#         user = User.objects.get(email="test@test.com")
#         self.assertFalse(user.loggedIn)
#         user.setLoginState(True)
#         self.assertTrue(user.loggedIn)
#         user.setLoginState(False)
#         self.assertFalse(user.loggedIn)


# Alec - Edit Course tests
class EditCourseTestCase(TestCase):

    def setUp(self):
        Course.objects.create(name="CS361", section="001", location="Roof", dates="TR", startTime='11:00:00', endTime='11:55:00')
        Course.objects.create(name="CS361", section="002", location="Basement", dates="MW", startTime='1:00:00', endTime='2:00:00')
        Course.objects.create(name="CS482", section="001", dates="Online")

    def test_edit_course_section(self):
        course = Course.objects.get(name="CS361", section='001')
        course.section = "002"
        self.assertEqual("002", course.section)

    def test_edit_course_section_already_exists(self):
        course = Course.objects.get(name="CS361", section='002')
        course.section = "001"
        self.assertEqual("Course section already exists", course.section)

    def test_edit_course_location(self):
        course = Course.objects.get(name="CS361", section='001')
        course.location = "Basement"
        self.assertEqual("Basement", course.location)

    def test_edit_course_dates(self):
        course = Course.objects.get(name="CS361", section='001')
        course.dates = "MW"
        self.assertEqual("MW", course.dates)

    def test_edit_course_start_time(self):
        course = Course.objects.get(name="CS361", section='001')
        course.startTime = "11:30:00"
        self.assertEqual("11:30:00", course.startTime)

    def test_edit_course_end_time(self):
        course = Course.objects.get(name="CS361", section='001')
        course.endTime = "12:00:00"
        self.assertEqual("12:00:00", course.endTime)

# Alec - Edit User tests
class EditUserTestCase(TestCase):

    def setUp(self):
        User.objects.create(email="admin@example.com", firstName='Bob', lastName='Bobble', phone='555-555-5555',
                            address='Roof', officeHours="2pm-3pm", officeHoursDates='MW', officeLocation='Jupiter')
        User.objects.create(email="instructor@example.com", firstName='Jim', lastName='Jimbles', phone='999-999-9999',
                            address='Basement', officeHours="4pm-5pm", officeHoursDates='TR',
                            officeLocation='Rain forest')
        User.objects.create(email="ta@example.com", firstName='Marky', lastName='Mark', phone='000-000-0000',
                            address='the void', officeHours="11am-12pm", officeHoursDates='F', officeLocation='Moon')

    def test_edit_user_first_name(self):
        user = User.objects.get(email="admin@example.com")
        user.firstName = "Rob"
        self.assertEqual("Rob", user.firstName)

    def test_edit_user_last_name(self):
        user = User.objects.get(email="admin@example.com")
        user.lastName = "Robble"
        self.assertEqual("Robble", user.lastName)

    def test_edit_user_phone(self):
        user = User.objects.get(email="admin@example.com")
        user.phone = "666-666-6666"
        self.assertEqual("666-666-6666", user.phone)

    def test_edit_user_address(self):
        user = User.objects.get(email="admin@example.com")
        user.address = "the void"
        self.assertEqual("the void", user.address)

    def test_edit_user_office_hours(self):
        user = User.objects.get(email="admin@example.com")
        user.officeHours = "6pm-7pm"
        self.assertEqual("6pm-7pm", user.officeHours)

    def test_edit_user_office_hours_dates(self):
        user = User.objects.get(email="admin@example.com")
        user.officeHoursDates = "T"
        self.assertEqual("T", user.officeHoursDates)

    def test_edit_user_office_location(self):
        user = User.objects.get(email="admin@example.com")
        user.officeHoursDates = "Mars"
        self.assertEqual("Mars", user.officeHoursDates)

    # Simon - more unit tests
    def test_profile1(self):
        user = User.objects.get(email="admin@example.com")
        user.resume = "a"
        self.assertEqual("a", user.resume)

    def test_profile2(self):
        user = User.objects.get(email="admin@example.com")
        user.preferences = "a"
        self.assertEqual("a", user.preferences)

    def test_profile3(self):
        user = User.objects.get(email="admin@example.com")
        user.schedule = "a"
        self.assertEqual("a", user.schedule)

    def test_profile4(self):
        user = User.objects.get(email="admin@example.com")
        user.resume = "a"
        self.assertNotEqual("b", user.resume)

    def test_profile5(self):
        user = User.objects.get(email="admin@example.com")
        user.schedule = "a"
        self.assertNotEqual("b", user.schedule)

    def test_profile6(self):
        user = User.objects.get(email="admin@example.com")
        user.preferences = "a"
        self.assertNotEqual("b", user.resume)



class assignTaTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="admin@example.com", firstName='Bob', lastName='Bobble', phone='555-555-5555',
                            address='Roof', officeHours="2pm-3pm", officeHoursDates='MW', officeLocation='Jupiter')
        User.objects.create(email="instructor@example.com", firstName='Jim', lastName='Jimbles', phone='999-999-9999',
                            address='Basement', officeHours="4pm-5pm", officeHoursDates='TR',
                            officeLocation='Rain forest')
        User.objects.create(email="ta@example.com", firstName='Marky', lastName='Mark', phone='000-000-0000',
                            address='the void', officeHours="11am-12pm", officeHoursDates='F', officeLocation='Moon')




    def testAssignTAPassing(self):
        user = User.objects.get(email="admin@example.com")
        worker = CommandWorker(currentUserEmail="admin@example.com")

        ta = user.clean()
        testCourse = Course
        worker.assign_ta(course=testCourse, tas=ta)
        self.assertEquals(user, Course.graderTAs.get(email="admin@example.com"))

    def testAssignTaBadCurrentUser(self):
        user = User.objects.get(email="admin@example.com")
        worker = CommandWorker()
        ta = user.clean()
        testCourse = Course

        worker.assign_ta(course=testCourse, tas=ta)