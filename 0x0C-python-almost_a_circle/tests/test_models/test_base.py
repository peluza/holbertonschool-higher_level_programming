#!/usr/bin/python3
"""test_base
"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_id_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_positive(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_negative(self):
        b5 = Base(-2)
        self.assertEqual(b5.id, -2)
        b6 = Base(-4)
        self.assertEqual(b6.id, -4)

    def test_id_str(self):
        b7 = Base("Holberton")
        self.assertEqual(b7.id, "Holberton")
        b8 = Base("School")
        self.assertEqual(b8.id, "School")

    def test_id_bool(self):
        b9 = Base(True)
        self.assertEqual(b9.id, True)
        b10 = Base(False)
        self.assertEqual(b10.id, False)

    def test_id_tuple(self):
        b11 = Base((1, 2))
        self.assertEqual(b11.id, (1, 2))
        b12 = Base((4, 5))
        self.assertEqual(b12.id, (4, 5))

    def test_id_list(self):
        b13 = Base([1, 2, 3, 4])
        self.assertEqual(b13.id, [1, 2, 3, 4])
        b14 = Base([2, 2432, 34, 42])
        self.assertEqual(b14.id, [2, 2432, 34, 42])

    def test_id_dic(self):
        b13 = Base({1: 2, 3: 4})
        self.assertEqual(b13.id, {1: 2, 3: 4})
        b14 = Base({2: 2432, 34: 42})
        self.assertEqual(b14.id, {2: 2432, 34: 42})

    def test_id_float(self):
        b15 = Base(1.3)
        self.assertEqual(b15.id, 1.3)
        b16 = Base(567.24)
        self.assertEqual(b16.id, 567.24)
