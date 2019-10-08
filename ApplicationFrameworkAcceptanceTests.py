import unittest
from unittest import TestCase
from ApplicationFramework import ApplicationFramework


class TestApplicationFramework(TestCase):
    def setUp(self):
        self.ApplicationFramework = ApplicationFramework()


class TestLogin(TestApplicationFramework):
    """For this test, we assume that the user exists in the database,
        and hasn't already logged in before"""

    def test_normLogin(self):
        VALID_USER = "valid@uwm.edu"
        VALID_PASS = "12345"
        self.ApplicationFramework.__init__()

        """ADD user/pass to database, set state to already logged in"""

        result = self.ApplicationFramework.login(VALID_USER, VALID_PASS)
        self.assertEquals("Login Successful", result)

    """For this test, we assume that the user exists in the database,
        but hasn't logged in at all before"""

    def test_newLogin(self):
        VALID_USER = "invalid@gmail.com"
        VALID_PASS = "e"
        self.ApplicationFramework.__init__()

        """ADD user/pass to database, set state to not already logged"""

        result = self.ApplicationFramework.login(VALID_USER, VALID_PASS)
        self.assertEquals("New Login Successful", result)

    """For this test we assume that either the user name being used to 
        log in doesn't exist in the database, or the user has input the
        wrong accompanying password."""

    def test_badLogin(self):
        INVALID_USER = "invalid@gmail.com"
        INVALID_PASS = "e"
        self.ApplicationFramework.__init__()

        """Don't add anything to database"""

        result = self.ApplicationFramework.login(INVALID_USER, INVALID_PASS)
        self.assertEquals("Login Not Successful", result)

        """Add user to database"""
        """Use wrong password"""
        result = self.ApplicationFramework.login(INVALID_USER, INVALID_PASS)
        self.assertEquals("Login Not Successful", result)

    # Fails if the username is not a valid UWM email address
    def test_loginUWMPass(self):
        self.ApplicationFramework.login("test@gmail.com", "password")
        self.assertEquals(str, "Login Failed.")

    # Passes if the username is a valid UWM email address
    def test_loginUWMFail(self):
        self.ApplicationFramework.login("test@uwm.edu", "password")
        self.assertEquals(str, "Login is Successful.")


class TestCreateCourse(TestApplicationFramework):

    def test_empty(self):
        self.ApplicationFramework.createCourse("course1")  # Where there are no courses.
        assert "Course added."

    def test_proper(self):
        self.ApplicationFramework.createCourse("course2")  # Where there is one non-conflicting course.
        assert "Course added."

    def test_conflicting(self):
        self.ApplicationFramework.createCourse("course2")  # Where there is a conflicting course.
        assert "Conflicting course found, could not add."


class TestApplicationFramework(TestApplicationFramework):
    # def test_createUser(self):
    #     self.assertSetEqual(TestApplicationFramework.createUser(self, 'Saad'), 'user created')
    #     self.assertSetEqual(TestApplicationFramework.createCourse(self, 'Simon'), 'user created')
    #     self.assertSetEqual(TestApplicationFramework.createCourse(self, 'Arif'), 'user created')
    #     #self.assertSetEqual(ApplicationFramework.createCourse(self, 'Arif'), 'user created')
    #    # self.fail()
    #     ApplicationFramework.createUser(self,'Saad')
    #     assert("user created")

    def test_createUser1(self):
        self.ApplicationFramework.createUser('Saad')
        self.assertEquals(str, "user created")

    def test_createUser2(self):
        self.ApplicationFramework.createUser('Arif')
        self.assertEquals(str, "user created")

    def test_createUser3(self):
        self.ApplicationFramework.createUser('Simon')
        self.assertEquals(str, "user created")

    def test_createUser4(self):
        self.ApplicationFramework.createUser('Alec')
        self.assertEquals(str, "user created")


if __name__ == '__main__':
    unittest.main()
