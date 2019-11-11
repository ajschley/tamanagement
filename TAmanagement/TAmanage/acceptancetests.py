from django.test import TestCase
from .models import Course
from .models import User
from .commands import CommandWorker


class CreateCourseTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.worker.currentUser = self.admin

    def test_create_a_course(self):
        course = Course.objects.filter(name='CS999')
        self.assertEquals(course.count(), 0)
        msg = self.worker.executeCommand("create course CS999")
        self.assertEqual(msg, 'Course added')
        course = Course.objects.filter(name='CS999')
        self.assertEquals(course.count(), 1)

class LoginTest(TestCase):
    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', password='so_very_simple', role=3)
        self.worker.currentUser = self.admin

    def test_login(self):
        msg = self.worker.executeCommand("login 'admin@example.com' 'so_very_simple'")
        self.assertEqual("Logged in as admin@example.com", msg)


class CreateUserTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.worker.currentUser = self.admin
        self.ta = User.objects.create(email='ta@uwm.com', role=1)

    def test_create_a_user(self):
        u = User.objects.filter(email="user@uwm.edu")
        self.assertEquals(u.count(), 0)
        msg = self.worker.executeCommand("create user 'user@uwm.edu' 'pickles4breakfast'")
        self.assertEqual(msg, 'User added')
        u = User.objects.filter(email='user@uwm.edu')
        self.assertEquals(u.count(), 1)

    def test_create_a_user_as_ta(self):
        self.worker.currentUser = self.ta
        u = User.objects.filter(email="user2@uwm.edu")
        self.assertEquals(u.count(), 0)
        msg = self.worker.executeCommand("create user 'user2@uwm.edu' 'pickles4breakfast'")
        self.assertEqual(msg, 'Only an Administrator can create a user')
        u = User.objects.filter(email='user2@uwm.edu')
        self.assertEquals(u.count(), 0)

class ListUserTest(TestCase):

    def setUp(self):
        self.worker = CommandWorker()
        self.admin = User.objects.create(email='admin@test.com', role=3)
        self.worker.currentUser = self.admin
        self.prof = User.objects.create(email='prof@uwm.edu', role=2)
        self.ta = User.objects.create(email='ta@uwm.com', role=1)

    def test_list_users(self):
        u = User.objects.filter(email="ta@uwm.edu")
        User.delete(u)
        u = User.objects.all()
        self.assertEquals(u.count(), 2)
        msg = self.worker.executeCommand("list users")
        self.assertEquals(msg, "")

    def test_list_users_1(self):
        u = User.objects.all()
        self.assertEquals(u.count(), 3)
        msg = self.worker.executeCommand("list users")
        self.assertEqual(msg, "")
