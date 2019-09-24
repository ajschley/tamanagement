from unittest import TestCase
from Lab4 import Rational


class TestRational(TestCase):
    def setUp(self):
        self.rational = Rational(0, 1)


class TestInit(TestRational):
    def test_initial(self):
        self.rational.__init__(1, 2)

    def test_zero(self):
        self.rational.__init__(0, 0)


class TestStr(TestRational):
    def testStrBase(self):
        self.assertEqual(self.rational.__str__(), "0/1")

    def testStrAGreaterThanB(self):
        self.rational.__init__(5, 1)
        self.assertEqual( "5/1", self.rational.__str__())

    def testStrBGreaterThanA(self):
        self.rational.__init__(1, 5)
        self.assertEqual("1/5", self.rational.__str__())

