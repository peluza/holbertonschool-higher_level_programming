#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_result_positve(self):
        """test_max_result_positve
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5, 5]), 5)
        self.assertAlmostEqual(max_integer([0]), 0)

    def test_none(self):
        """test_none
        """
        self.assertIsNone(max_integer([None]), None)
        self.assertIsNone(max_integer([]), None)

    def test_max_result_negative(self):
        """test_max_result_negative
        """
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4, -3]), -1)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4, -3]), -1)

    def test_max_result_negative_and_postive(self):
        """test_max_result_negative_and_postive
        """
        self.assertAlmostEqual(max_integer([-1, 2, 3, -4, -3]), 3)
        self.assertAlmostEqual(max_integer([-1, 2, -3, 4, 3]), 4)

    def test_max_result_positive_float(self):
        """test_max_result_positive_float
        """
        self.assertAlmostEqual(max_integer([1.2, 2.3, 3.4, 4.5, 3.6]), 4.5)
        self.assertAlmostEqual(max_integer([1.2, 2.3, 5.4, 4.5, 3.6]), 5.4)

    def test_max_result_positive_and_negative_float(self):
        """test_max_result_positive_and_negative_float
        """
        self.assertAlmostEqual(max_integer(
            [-1.2, 2.3, -3.4, -4.5, -3.6]), 2.3)
        self.assertAlmostEqual(max_integer([1.2, -2.3, -5.4, -4.5, -3.6]), 1.2)

    def test_max_result_negative_float(self):
        """test_max_result_negative_float
        """
        self.assertAlmostEqual(max_integer(
            [-1.2, -2.3, -3.4, -4.5, -3.6]), -1.2)
        self.assertAlmostEqual(max_integer(
            [-1.2, -2.3, -5.4, -4.5, -3.6]), -1.2)

    def test_max_result_raise(self):
        """_max_result_raise
        """
        with self.assertRaises(TypeError):
            max_integer(1, 2)
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer(3.8)
