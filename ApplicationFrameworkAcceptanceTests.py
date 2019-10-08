from unittest import TestCase
from ApplicationFramework import ApplicationFramework


class TestApplicationFramework(TestCase):
    def test__init__(self):
        self.fail()


class TestLogin(TestApplicationFramework) :
    def test_login(self):
        self.fail()

class TestCreateCourse(TestApplicationFramework) :

   #passes if valid course name, assume course name is CS361 which is a valid course
    def test_create_course(self):
        self.ApplicationFramework.createCourse(self, "CS361")
        self.assertEquals(str, "Course created")

   #fails if pass in more than one class
    def test_create_course2(self):
        self.ApplicationFramework.createCourse(self, "CS361", "CS337")
        self.assertEquals(str, "Too many courses")

   # fails if no class is passed in
    def test_create_course3(self):
        self.ApplicationFramework.createCourse(self)
        self.assertEquals(str, "No course to create")

