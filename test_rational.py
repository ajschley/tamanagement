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


#float cases by Arif
class TestFloat(TestRational):
    def test_int(self):
        self.assertEqual(self.__float__(10 / 2), 5.0)
        self.assertEqual(10 / 2, 5.0)
        self.assertEqual(10 / 3, 3.3)
        self.assertEqual(10 / 4, 2.5)
        self.assertEqual(10 / 5, 2.0)
        self.assertEqual(10 / 6, 1.7)
        self.assertEqual(10 / 7, 1.4)
        self.assertEqual(10 / 8, 1.3)
        self.assertEqual(10 / 9, 1.1)
        self.assertEqual(10 / 10, 1.0)

    def test_float_int(self):
        self.assertEqual(10.0 / 2, 5.0)
        self.assertEqual(10.0 / 3, 3.3)
        self.assertEqual(10.0 / 4, 2.5)
        self.assertEqual(10.0 / 5, 2.0)
        self.assertEqual(10.0 / 6, 1.7)
        self.assertEqual(10.0 / 7, 1.4)
        self.assertEqual(10.0 / 8, 1.3)
        self.assertEqual(10.0 / 9, 1.1)
        self.assertEqual(10.0 / 10, 1.0)

    def test_int_float(self):
        self.assertEqual(10 / 2.0, 5.0)
        self.assertEqual(10 / 3.0, 3.3)
        self.assertEqual(10 / 4.0, 2.5)
        self.assertEqual(10 / 5.0, 2.0)
        self.assertEqual(10 / 6.0, 1.7)
        self.assertEqual(10 / 7.0, 1.4)
        self.assertEqual(10 / 8.0, 1.3)
        self.assertEqual(10 / 9.0, 1.1)
        self.assertEqual(10 / 10.0, 1.0)

    def test_float_float(self):
        self.assertEqual(10.0 / 2.0, 5.0)
        self.assertEqual(10.0 / 3.0, 3.3)
        self.assertEqual(10.0 / 4.0, 2.5)
        self.assertEqual(10.0 / 5.0, 2.0)
        self.assertEqual(10.0 / 6.0, 1.6)
        self.assertEqual(10.0 / 7.0, 1.4)
        self.assertEqual(10.0 / 8.0, 1.3)
        self.assertEqual(10.0 / 9.0, 1.1)
        self.assertEqual(10.0 / 10.0, 1.0)

    def test_by_zero(self):
        self.assertTrue("Denom my not be zero" in self.exception)
