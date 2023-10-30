import unittest
from TestCases.my_adder_34 import my_adder


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        self.assertEqual(my_adder(5, 3), 8)
        # 函数调用也可以作为参数

    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5, 3), -2)
