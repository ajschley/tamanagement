from unittest import TestCase

from Lab4 import Rational

class TestRational(TestCase):
    def setUp(self):
        self.rational = Rational(0, 1)

class TestMul(TestRational):
    def test_zero(self):
        self.rational.__init__(0, 1)
        self.assertEqual(Rational().__init__(0, 1), self.rational.__mul__(0))
    def test_zero2(self):
        self.rational.__init__(5, 1)
        self.assertEqual(Rational().__init__(0, 1), self.rational.__mul__(0))
    def test_twentyFive(self):
        self.rational.__init__(5, 1)
        self.assertEqual(Rational().__init__(25, 1), self.rational.__mul__(5))
    def test_negative(self):
        self.rational.__init__(5, 1)
        self.assertEqual(Rational().__init__(-25, 1), self.rational.__mul__(-5))
class TestDiv(TestRational):
    def test_five(self):
        self.rational.__init__(25, 1)
        self.assertEqual(Rational().__init__(5, 1), self.rational.__div__(5))
    def test_same(self):
        self.rational.__init__(25, 1)
        self.assertEqual(Rational().__init__(25, 1), self.rational.__div__(1))