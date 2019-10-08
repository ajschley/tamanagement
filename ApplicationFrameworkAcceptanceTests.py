import unittest
from unittest import TestCase
from ApplicationFramework import ApplicationFramework


class TestApplicationFramework(TestCase):
    def test__init__(self):
        self.fail()


class TestLogin(TestApplicationFramework) :
    def test_login(self):
        self.fail()

    # Fails if username is not a valid UWM email address
    def test_loginUWMPass(self):
        self.ApplicationFramework.__login__("test@gmail.com", "password")
        self.assertEquals(str, "Login Failed.")

    # Passes if username is a valid UWM email address
    def test_loginUWMFail(self):
        self.ApplicationFramework.__login__("test@uwm.edu", "password")
        self.assertEquals(str, "Login is Successful.")


if __name__ == '__main__':
    unittest.main()
