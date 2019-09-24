from unittest import TestCase

from Lab4 import Rational

class TestRational(TestCase):
    def test_setup(self):
        self.rational = Rational()

class TestInit(TestRational):
    def test_initial(self):
        self.rational.__init__(self, 1, 2)

    def test_zero(self):
        self.rational.__init__(self, 0, 0)
