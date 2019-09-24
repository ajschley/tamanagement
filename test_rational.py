import unittest
from unittest import TestCase

from Lab4 import Rational


class TestRational(unittest.TestCase):
    def setUp(self):
        self.rational = Rational()


class TestAdd(TestRational):
    def test_zero(self):
        self.rational.__init__(2, 1)
        self.rational.__mul__(0)
        self.assertTrue(self.rational.n == 2)

    def test_negative(self):
        self.rational.__init__(2, 1)
        self.rational.__mul__(-1)
        self.assertTrue(self.rational.n == 1)

    def test_number(self):
        self.rational.__init__(5, 1)
        self.rational.__mul__(5)
        self.assertTrue(self.rational.n == 10)


class TestSub(TestRational):
    def test_zero(self):
        self.rational.__init__(2, 1)
        self.rational.__sub__(0)
        self.assertTrue(self.rational.n == 2)

    def test_negative(self):
        self.rational.__init__(2, 1)
        self.rational.__sub__(-1)
        self.assertTrue(self.rational.n == 3)

    def test_number(self):
        self.rational.__init__(5, 1)
        self.rational.__sub__(5)
        self.assertTrue(self.rational.n == 0)


class TestMul(TestRational):
    def test_zero(self):
        self.rational.__init__(2, 1)
        self.rational.__mul__(0)
        self.assertTrue(0 == self.rational.n)

    def test_negative(self):
        self.rational.__init__(2, 1)
        self.rational.__mul__(-1)
        self.assertTrue(self.rational.n > 0)

    def test_number(self):
        self.rational.__init__(5, 1)
        self.rational.__mul__(5)
        self.assertTrue(self.rational.n == 25)


class TestDiv(TestRational):
    def test_zero(self):
        self.rational.__init__(1, 1)
        self.rational.__div__(0)
        self.assertTrue(1 == self.rational.n)

    def test_negative(self):
        self.rational.__init__(2, 1)
        self.rational.__div__(-1)
        self.assertTrue(self.rational.n > 0)

    def test_number(self):
        self.rational.__init__(5, 1)
        self.rational.__mul__(5)
        self.assertTrue(self.rational.n == 1)
