from django.test import TestCase
from .models import Course
from .models import User
from .commands import CommandWorker


class WorkerTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.worker.currentUser = self.admin

    def test_worker(self):
        msg = self.worker.executeCommand("adsfasdfsdf")
        self.assertEqual(msg, "Not a valid command")


class InvalidCommandTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()

    def test_invalid_command(self):
        msg = self.worker.executeCommand("asdfdsf")
        self.assertEqual(msg, "Not a valid command")


class CreateCourseTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.ta = User.objects.create(email='ta@uwm.com', role=1)
        self.prof = User.objects.create(email='prof@test.com', role=2)
        self.worker.currentUser = self.admin

    def test_create_a_course(self):
        course = Course.objects.filter(name='CS999')
        self.assertEqual(course.count(), 0)
        msg = self.worker.executeCommand("create course CS999")
        self.assertEqual(msg, 'Course added')
        self.assertEqual(course.count(), 1)

    def test_create_a_course_1(self):
        course = Course.objects.filter(name='CS999')
        self.assertEquals(course.count(), 0)
        msg = self.worker.executeCommand("create course CS999 asdf")
        self.assertEqual(msg, 'Invalid number of parameters')
        self.assertEqual(course.count(), 0)

    def test_create_a_course_2(self):
        course = Course.objects.filter(name='CS999')
        self.assertEqual(course.count(), 0)
        msg = self.worker.executeCommand("create course")
        self.assertEqual(msg, 'Invalid number of parameters')
        self.assertEqual(course.count(), 0)

    def test_create_a_course_3(self):
        course = Course.objects.filter(name='CS999')
        self.assertEquals(course.count(), 0)
        msg = self.worker.executeCommand("create course CS999")
        self.assertEqual(msg, 'Course added')
        self.assertEqual(course.count(), 1)
        msg = self.worker.executeCommand("create course CS999")
        self.assertEqual(msg, 'Course already exists')
        self.assertEqual(course.count(), 1)

    def test_create_a_course_4(self):
        self.worker.currentUser = self.ta
        msg = self.worker.executeCommand("create course CS999")
        self.assertEqual(msg, "Only an Administrator can create a course")

    def test_create_a_course_5(self):
        self.worker.currentUser = self.prof
        msg = self.worker.executeCommand("create course CS999")
        self.assertEqual(msg, "Only an Administrator can create a course")


class LoginTest(TestCase):
    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', password='so_very_simple', role=3)
        self.ta = User.objects.create(email='ta@uwm.com', password='password', role=1)
        self.worker.currentUser = self.admin

    def test_login(self):
        msg = self.worker.executeCommand("login admin@example.com so_very_simple")
        self.assertEqual("Given email does not belong to an existing user", msg)

    def test_login_1(self):
        msg = self.worker.executeCommand("login admin@test.com so_very_simple")
        self.assertEqual("Logged in as admin@test.com", msg)

    def test_login_2(self):
        msg = self.worker.executeCommand("login admin@test.com so_very_simple")
        self.assertEqual("Logged in as admin@test.com", msg)
        msg = self.worker.executeCommand("logout")
        self.assertEqual("Logged out", msg)

    def test_login_3(self):
        msg = self.worker.executeCommand("login admin@test.com so_very_simple")
        self.assertEqual("Logged in as admin@test.com", msg)
        msg = self.worker.executeCommand("logout")
        self.assertEqual("Logged out", msg)
        msg = self.worker.executeCommand("login ta@uwm.com password")
        self.assertEqual("Logged in as ta@uwm.com", msg)


class CreateUserTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.worker.currentUser = self.admin
        self.ta = User.objects.create(email='ta@uwm.com', role=1)
        self.prof = User.objects.create(email='prof@test.com', role=2)

    def test_create_a_user(self):
        u = User.objects.filter(email="user@uwm.edu")
        self.assertEqual(u.count(), 0)
        msg = self.worker.executeCommand("create user user@uwm.edu pickles4breakfast")
        self.assertEqual(msg, 'User added')
        self.assertEqual(u.count(), 1)

    def test_create_a_user_1(self):
        self.worker.currentUser = self.ta
        u = User.objects.filter(email="user2@uwm.edu")
        self.assertEqual(u.count(), 0)
        msg = self.worker.executeCommand("create user user2@uwm.edu pickles4breakfast")
        self.assertEqual(msg, 'Only an Administrator can create a user')
        self.assertEqual(u.count(), 0)

    def test_create_a_user_2(self):
        self.worker.currentUser = self.prof
        u = User.objects.filter(email="user3@uwm.edu")
        self.assertEqual(u.count(), 0)
        msg = self.worker.executeCommand("create user user3@uwm.edu pickles4breakfast")
        self.assertEqual(msg, 'Only an Administrator can create a user')
        self.assertEqual(u.count(), 0)

    def test_create_a_user_3(self):
        #u = User.objects.filter(email="user@uwm.edu")
        msg = self.worker.executeCommand("create user")
        self.assertEqual(msg, "Invalid number of parameters")

    def test_create_a_user_4(self):
        u = User.objects.filter(email="user@uwm.edu")
        msg = self.worker.executeCommand("create user alec@uwm.edu")
        self.assertEqual(msg, "Invalid number of parameters")

    def test_create_a_user_5(self):
        u = User.objects.filter(email="user@uwm.edu")
        msg = self.worker.executeCommand("create user alec@uwm.edu banana banana")
        self.assertEqual(msg, "Invalid number of parameters")

    def test_create_a_user_5(self):
        u = User.objects.filter(email="user@uwm.edu")
        msg = self.worker.executeCommand("create user ta@uwm.com shiloop")
        self.assertEqual(msg, "User already exists")


class EditCourseTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.worker.currentUser = self.admin
        self.prof = User.objects.create(email='prof@uwm.edu', role=2)
        self.ta = User.objects.create(email='ta@uwm.com', role=1)
        self.course1 = Course.objects.create(name="CS999")

    def test_edit_course(self):
        msg = self.worker.executeCommand("edit course CS999 EMS180")
        self.assertEqual(msg, "Course already up to date")


