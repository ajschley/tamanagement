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


if __name__ == '__main__':
    unittest.main()
