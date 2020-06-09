#!/usr/bin/python3
"""test_rectangle
"""
import unittest
import pep8
from models.rectangle import Rectangle, Base


def print1(value):
    return value


class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_rectangle_positive(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(130, 2, 34)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(130, 2, 34, 2)
        self.assertEqual(r3.id, 3)

    def test_rectangle_negative(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, -2)
        with self.assertRaises(ValueError):
            r5 = Rectangle(-10, -2, -3)
        with self.assertRaises(ValueError):
            r6 = Rectangle(-10, -2, -3, -10)

    def test_rectangle_mix(self):
        with self.assertRaises(ValueError):
            r7 = Rectangle(10, -2)
        with self.assertRaises(ValueError):
            r8 = Rectangle(-10, 2, -3)
        with self.assertRaises(ValueError):
            r9 = Rectangle(10, -2, -3, 10)

    def test_rectangle_tuple(self):
        with self.assertRaises(TypeError):
            r10 = Rectangle(10, (-2, ))
        with self.assertRaises(TypeError):
            r11 = Rectangle((-10,), 2, -3)
        with self.assertRaises(TypeError):
            r12 = Rectangle((10, -2, -3, 10))
        with self.assertRaises(TypeError):
            r13 = Rectangle((10, -2, (-3, 10)))
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2, (-3, 10))

    def test_rectangle_list(self):
        with self.assertRaises(TypeError):
            r15 = Rectangle(10, [-2, ])
        with self.assertRaises(TypeError):
            r16 = Rectangle([-10, ], 2, -3)
        with self.assertRaises(TypeError):
            r17 = Rectangle([10, -2, -3, 10])
        with self.assertRaises(TypeError):
            r18 = Rectangle([10, -2, [-3, 10]])
        with self.assertRaises(TypeError):
            r19 = Rectangle(10, 2, [-3, 10])

    def test_rectangle_dict(self):
        with self.assertRaises(TypeError):
            r20 = Rectangle(10, {-2: "text"})
        with self.assertRaises(TypeError):
            r21 = Rectangle({-10: 3}, 2, -3)
        with self.assertRaises(TypeError):
            r22 = Rectangle({10: -2, -3: 10})
        with self.assertRaises(TypeError):
            r23 = Rectangle([10, -2, {-3: 10}])
        with self.assertRaises(TypeError):
            r24 = Rectangle(10, 2, [-3, 10])

    def test_rectangle_str(self):
        with self.assertRaises(TypeError):
            r25 = Rectangle(10, "text")
        with self.assertRaises(TypeError):
            r26 = Rectangle("Holberton", 2, -3)
        with self.assertRaises(TypeError):
            r27 = Rectangle("Holberton", "School")
        with self.assertRaises(TypeError):
            r28 = Rectangle(10, 2, "School")

    def test_rectangle_bool(self):
        with self.assertRaises(TypeError):
            r29 = Rectangle(10, True)
        with self.assertRaises(TypeError):
            r30 = Rectangle(False, 2, -3)
        with self.assertRaises(TypeError):
            r31 = Rectangle(True, False)
        with self.assertRaises(TypeError):
            r32 = Rectangle(10, 2, True)

    def test_rectangle_float(self):
        with self.assertRaises(TypeError):
            r33 = Rectangle(10, 2.5)
        with self.assertRaises(TypeError):
            r34 = Rectangle(4.6, 2, 2.5)
        with self.assertRaises(TypeError):
            r35 = Rectangle(20.56, 2.7)
        with self.assertRaises(TypeError):
            r36 = Rectangle(10, 2, 436.23)

    def test_area_positive(self):
        r37 = Rectangle(3, 2)
        self.assertEqual(r37.area(), 6)
        r38 = Rectangle(2, 10)
        self.assertEqual(r38.area(), 20)
        r39 = Rectangle(2, 10, 3)
        self.assertEqual(r39.area(), 20)
        r40 = Rectangle(8, 7, 3, 5, "Edison")
        self.assertEqual(r40.area(), 56)

    def test_display(self):
        r41 = Rectangle(4, 6)
        self.assertEqual(r41.display(), None)
        r42 = Rectangle(8, 4, 3)
        self.assertEqual(r42.display(), None)
        r43 = Rectangle(3, 3, 3, 9)
        self.assertEqual(r43.display(), None)
        r44 = Rectangle(4, 2, 3, 9, "Holberton")
        self.assertEqual(r44.display(), None)

    def test_str(self):
        r45 = Rectangle(4, 6)
        self.assertEqual(
            r45.__str__(), '[Rectangle] ({}) 0/0 - 4/6'.format(r45.id))
        r46 = Rectangle(8, 4, 3)
        self.assertEqual(
            r46.__str__(), '[Rectangle] ({}) 3/0 - 8/4'.format(r46.id))
        r47 = Rectangle(3, 3, 3, 9)
        self.assertEqual(
            r47.__str__(), '[Rectangle] ({}) 3/9 - 3/3'.format(r47.id))
        r48 = Rectangle(4, 2, 3, 9, "Esteban")
        self.assertEqual(r48.__str__(), '[Rectangle] (Esteban) 3/9 - 4/2')
        r49 = Rectangle(4, 6)
        self.assertAlmostEqual(print(r49), None)
        r50 = Rectangle(8, 4, 3)
        self.assertEqual(print(r50), None)
        r51 = Rectangle(3, 3, 3, 9)
        self.assertEqual(print(r51), None)
        r52 = Rectangle(4, 2, 3, 9, "Isaza")
        self.assertEqual(print(r52), None)

    def test_update_args(self):
        r53 = Rectangle(4, 6)
        r53.update(89)
        self.assertEqual(r53.__str__(), '[Rectangle] (89) 0/0 - 4/6')
        r54 = Rectangle(8, 4, 3)
        r54.update(90, 3, 4)
        self.assertEqual(r54.__str__(), '[Rectangle] (90) 3/0 - 3/4')
        r55 = Rectangle(3, 3, 3, 9)
        r55.update(91, 2, 2, 2)
        self.assertEqual(r55.__str__(), '[Rectangle] (91) 2/9 - 2/2')
        r56 = Rectangle(4, 2, 3, 9, "Holberton")
        r56.update(92, 3, 4, 5, 2)
        self.assertEqual(r56.__str__(), '[Rectangle] (92) 5/2 - 3/4')
        r57 = Rectangle(4, 2, 3,)
        r57.update(93, 4, 2, 3, 2)
        self.assertEqual(r57.__str__(), '[Rectangle] (93) 3/2 - 4/2')
        r58 = Rectangle(4, 2, 3)
        r58.update()
        self.assertEqual(
            r58.__str__(), '[Rectangle] ({}) 3/0 - 4/2'.format(r58.id))

    def test_update_kwargs(self):
        r59 = Rectangle(4, 6)
        r59.update(id=89)
        self.assertEqual(r59.__str__(), '[Rectangle] (89) 0/0 - 4/6')
        r60 = Rectangle(8, 4, 3)
        r60.update(id=90, width=3, height=4)
        self.assertEqual(r60.__str__(), '[Rectangle] (90) 3/0 - 3/4')
        r61 = Rectangle(3, 3, 3, 9)
        r61.update(id=91, height=2, width=2, y=2)
        self.assertEqual(r61.__str__(), '[Rectangle] (91) 3/2 - 2/2')
        r62 = Rectangle(4, 2, 3, 9, "School")
        r62.update(x=92, y=3, id=4, width=5, heigth=2)
        self.assertEqual(r62.__str__(), '[Rectangle] (4) 92/3 - 5/2')
        r63 = Rectangle(4, 2, 3,)
        r63.update(id=93, y=4, x=2, height=3, width=2)
        self.assertEqual(r63.__str__(), '[Rectangle] (93) 2/4 - 2/3')

    def test_rectangle_dictionary(self):
        r64 = Rectangle(10, 2, 1, 9, 345)
        self.assertEqual(
            r64.to_dictionary(), {'id': 345, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        r65 = Rectangle(10, 2, 1, 9)
        self.assertEqual(
            r65.to_dictionary(), {'id': r65.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        r66 = Rectangle(10, 2, 1)
        self.assertEqual(
            r66.to_dictionary(), {'id': r66.id, 'width': 10, 'height': 2, 'x': 1, 'y': 0})
        r67 = Rectangle(10, 2)
        self.assertEqual(
            r67.to_dictionary(), {'id': r67.id, 'width': 10, 'height': 2, 'x': 0, 'y': 0})

    def test_rectangle_json(self):
        r68 = Rectangle(10, 2, 1, 9, 345)
        r69 = r68.to_dictionary()
        self.assertEqual(
            Base.to_json_string([r69]), '[{"id": 345, "width": 10, "height": 2, "x": 1, "y": 9}]')
        r70 = Rectangle(10, 2, 1, 9)
        r71 = r70.to_dictionary()
        self.assertEqual(
            Base.to_json_string([r71]), '[{"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}]')
        r72 = Rectangle(10, 2, 1)
        r73 = r72.to_dictionary()
        self.assertEqual(
            Base.to_json_string([r73]), '[{"id": 2, "width": 10, "height": 2, "x": 1, "y": 0}]')
        r74 = Rectangle(10, 2)
        r75 = r74.to_dictionary()
        self.assertEqual(
            Base.to_json_string(r75), None)
        r76 = Rectangle(10, 2)
        self.assertEqual(
            Base.to_json_string([]), '[]')
