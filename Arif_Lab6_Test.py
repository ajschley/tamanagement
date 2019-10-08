import unittest
from unittest import TestCase
import ApplicationFramework

class TestApplicationFramework(TestCase):

    def test_create_user1(self):
        ApplicationFramework.createUser(self, 'user@uwm.edu')  # user with a valid uwm email account.
        self.assertEquals(str, "User added")

    def test_create_user2(self):
        ApplicationFramework.createUser(self, 'user2@uwm.edu')  # user already exists in the system
        self.assertEquals(str, "User Already Exists")


if __name__ == '__main__':
    unittest.main()
