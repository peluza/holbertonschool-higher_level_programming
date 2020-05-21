#!/usr/bin/python3
"""[add_integer]
"""


def add_integer(a, b=98):
    try:
        return int(a) + int(b)
    except TypeError:
        if a is not int or float:
            print("a must be an integer")
        if b is not int or float:
            print("b must be an integer")
    except Exception:
        pass
