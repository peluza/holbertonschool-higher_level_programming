#!/usr/bin/python3
"""test_Square
"""
import unittest
import pep8
from models.square import Square


class TestMaxInteger(unittest.TestCase):

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_square_str(self):
        s1 = Square(5)
        self.assertEqual(s1.__str__(), '[Square] ({}) 0/0 - 5'.format(s1.id))
        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), '[Square] ({}) 2/0 - 2'.format(s2.id))
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), '[Square] ({}) 1/3 - 3'.format(s3.id))
        s4 = Square(2, 5, 4, 89)
        self.assertEqual(s4.__str__(), '[Square] (89) 5/4 - 2')
        s5 = Square(234, 35436, 12, 1234156)
        self.assertEqual(s5.__str__(), '[Square] (1234156) 35436/12 - 234')

    def test_square_size_positive(self):
        s6 = Square(5)
        s6.size = 10
        self.assertEqual(s6.__str__(), '[Square] ({}) 0/0 - 10'.format(s6.id))
        s7 = Square(500)
        s7.size = 500
        self.assertEqual(s7.__str__(), '[Square] ({}) 0/0 - 500'.format(s7.id))

    def test_square_size_negative(self):
        s8 = Square(5)
        with self.assertRaises(ValueError):
            s8.size = -10
        s9 = Square(500)
        with self.assertRaises(ValueError):
            s9.size = -200

    def test_square_size_str(self):
        s10 = Square(5)
        with self.assertRaises(TypeError):
            s10.size = "10"
        s11 = Square(500)
        with self.assertRaises(TypeError):
            s11.size = "200"

    def test_square_size_dict(self):
        s12 = Square(5)
        with self.assertRaises(TypeError):
            s12.size = {10: 2}
        s13 = Square(500)
        with self.assertRaises(TypeError):
            s13.size = {200: "s"}

    def test_square_size_list(self):
        s14 = Square(5)
        with self.assertRaises(TypeError):
            s14.size = [10]
        s15 = Square(500)
        with self.assertRaises(TypeError):
            s15.size = [1, 4, 5]

    def test_square_size_tuple(self):
        s16 = Square(5)
        with self.assertRaises(TypeError):
            s16.size = (10, )
        s17 = Square(500)
        with self.assertRaises(TypeError):
            s17.size = (200, 334)

    def test_square_size_bool(self):
        s18 = Square(5)
        with self.assertRaises(TypeError):
            s18.size = True
        s19 = Square(500)
        with self.assertRaises(TypeError):
            s19.size = False

    def test_update_args(self):
        s20 = Square(4)
        s20.update(1234)
        self.assertEqual(s20.__str__(), '[Square] (1234) 0/0 - 4')
        s21 = Square(8, 4)
        s21.update(234, 3, 4)
        self.assertEqual(s21.__str__(), '[Square] (234) 4/0 - 3')
        s22 = Square(3, 3, 9)
        s22.update(91, 2, 2)
        self.assertEqual(s22.__str__(), '[Square] (91) 2/9 - 2')
        s23 = Square(4, 3, 9, "ISaza")
        s23.update(4522, 3, 5, 2)
        self.assertEqual(s23.__str__(), '[Square] (4522) 5/2 - 3')
        s24 = Square(4, 2, 3,)
        s24.update(93, 4, 3, 2)
        self.assertEqual(s24.__str__(), '[Square] (93) 3/2 - 4')
        s25 = Square(4, 2, 3)
        s25.update()
        self.assertEqual(
            s25.__str__(), '[Square] ({}) 2/3 - 4'.format(s25.id))

    def test_update_kwargs(self):
        s26 = Square(4)
        s26.update(id=93)
        self.assertEqual(s26.__str__(), '[Square] (93) 0/0 - 4')
        s27 = Square(8, 4)
        s27.update(id=90, size=4)
        self.assertEqual(s27.__str__(), '[Square] (90) 4/0 - 4')
        s28 = Square(3, 3, 9)
        s28.update(id=91, size=2, y=2)
        self.assertEqual(s28.__str__(), '[Square] (91) 3/2 - 2')
        s29 = Square(4, 3, 9, "School")
        s29.update(x=92, y=3, id=4, size=5)
        self.assertEqual(s29.__str__(), '[Square] (4) 92/3 - 5')
        s30 = Square(4, 2, 3,)
        s30.update(id=93, y=4, x=2, size=3)
        self.assertEqual(s30.__str__(), '[Square] (93) 2/4 - 3')

    def test_Square_dictionary(self):
        s31 = Square(10, 2, 9, 345)
        self.assertEqual(
            s31.to_dictionary(), {'id': 345, "size": 10, 'x': 2, 'y': 9})
        s32 = Square(10, 2, 1)
        self.assertEqual(
            s32.to_dictionary(), {'id': s32.id, 'size': 10, 'x': 2, 'y': 1})
        s33 = Square(10, 2, 1)
        self.assertEqual(
            s33.to_dictionary(), {'id': s33.id, 'size': 10, 'x': 2, 'y': 1})
        s34 = Square(10, 2)
        self.assertEqual(
            s34.to_dictionary(), {'id': s34.id, 'size': 10, 'x': 2, 'y': 0})
        s35 = Square(10)
        self.assertEqual(
            s35.to_dictionary(), {'id': s35.id, 'size': 10, 'x': 0, 'y': 0})
