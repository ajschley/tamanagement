from unittest import TestCase
from Lab4 import Rational


class TestRational(TestCase):
    def setUp(self):
        self.rational = Rational(0, 1)


class TestInit(TestRational):
    def test_initial(self):
        self.rational.__init__(self, 1, 2)

    def test_zero(self):
        self.rational.__init__(self, 0, 0)


class TestAdd(TestRational):
    def test_zero(self):
        self.rational.__init__(2, 1)
        self.rational.__add__(0)
        self.assertTrue(self.rational.n == 2)

    def test_negative(self):
        self.rational.__init__(2, 1)
        self.rational.__add__(-1)
        self.assertTrue(self.rational.n == 1)

    def test_number(self):
        self.rational.__init__(5, 1)
        self.rational.__add__(5)
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
        self.rational.__div__(5)
        self.assertTrue(self.rational.n == 1)


class TestStr(TestRational):
    def testStrBase(self):
        self.assertEqual(self.rational.__str__(), "0/1")

    def testStrAGreaterThanB(self):
        self.rational.__init__(5, 1)
        self.assertEqual("5/1", self.rational.__str__())

    def testStrBGreaterThanA(self):
        self.rational.__init__(1, 5)
        self.assertEqual("1/5", self.rational.__str__())


class TestFloat(TestRational):
    def test_int(self):
        self.rational.__init__(10, 2)
        self.assertEqual(5.0, self.rational.__float__())

    def test_float_int(self):
        self.rational.__init__(10.0, 2)
        self.assertEqual(5.0, self.rational.__float__())

    def test_int_float(self):
        self.rational.__init__(10, 2.0)
        self.assertEqual(5.0, self.rational.__float__())

    def test_float_float(self):
        self.rational.__init__(10.0, 2.0)
        self.assertEqual(5.0, self.rational.__float__())
