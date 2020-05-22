#!/usr/bin/python3
"""[0-add_integer]
"""


def add_integer(a, b=98):
    """[add_integer(a, b)]

    Arguments:
        a {[int - float]} -- [a number is interget or float]

    Keyword Arguments:
        b {[int - float]} -- [a number is interget or float] (default: {98})

    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]

    Returns:
        [int] -- [add the a and b]
    """
    if type(a) is not int and type(a) is not float or None:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
