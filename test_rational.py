from unittest import TestCase

from Lab4 import Rational

class TestRational(TestCase):
    def test_setUp(self):
        self.rational = Rational(1, 2)

class TestAdd(TestRational):
    def test_zero(self):
        self.rational.__init__(0, 1)
        self.assertEqual(Rational().__init__(0, 1), self.rational.__add__(self, 0))
    def test_one(self):
        self.rational.__init__(1, 1)
        self.assertEqual(Rational().__init__(0, 1), self.rational.__add__(self, 0))
    def test_oneHalf(self):
        self.rational.__init__(1, 2)
        self.assertEqual(Rational().__init__(1, 2), self.rational.__add__(self, 0))
    def test_ten(self):
        self.rational.__init__(5, 1)
        self.assertEqual(Rational().__init__(5, 1), self.rational.__add__(self, 5))
    def test_negativeOne(self):
        self.rational.__init__(-1, 1)
        self.assertEqual(Rational().__init__(-1, 1), self.rational.__add__(self, 0))
    def test_oneHundred(self):
        self.rational.__init__(50, 2)
        self.assertEqual(Rational().__init__(100, 1), self.rational.__add__(self, 75))
