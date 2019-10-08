import unittest
from unittest import TestCase

import ApplicationFramework


class TestApplicationFramework(TestCase):
    # def test_createUser(self):
    #     self.assertSetEqual(TestApplicationFramework.createUser(self, 'Saad'), 'user created')
    #     self.assertSetEqual(TestApplicationFramework.createCourse(self, 'Simon'), 'user created')
    #     self.assertSetEqual(TestApplicationFramework.createCourse(self, 'Arif'), 'user created')
    #     #self.assertSetEqual(ApplicationFramework.createCourse(self, 'Arif'), 'user created')
    #    # self.fail()
    #     ApplicationFramework.createUser(self,'Saad')
    #     assert("user created")

    def test_createUser1(self):
        ApplicationFramework.createUser(self, 'Saad')
        self.assertEquals(str, "user created")

    def test_createUser2(self):
        ApplicationFramework.createUser(self, 'Arif')
        self.assertEquals(str, "user created")

    def test_createUser2(self):
        ApplicationFramework.createUser(self, 'Simon')
        self.assertEquals(str, "user created")

    def test_createUser3(self):
        ApplicationFramework.createUser(self, 'Alex')
        self.assertEquals(str, "user created")


if __name__ == '__main__':
    unittest.main()
