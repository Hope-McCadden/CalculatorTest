from Calculator import Calculator
from unittest import TestCase

class CalculatorTest(TestCase):
    def testAdd(self):
        c = Calculator()
        actual = c.add(2,2)
        expected = 4
        self.assertEqual(expected, actual)

    def testSub(self):
        c = Calculator()
        actual = c.sub(2,2)
        expected = 0
        self.assertEqual(expected,actual)

    def testMult(self):
        c = Calculator()
        actual = c.mult(2,2)
        expected = 4
        self.assertEqual(expected,actual)

    def testDiv(self):
        c = Calculator()
        actual = c.div(2, 2)
        expected = 1
        self.assertEqual(expected, actual)