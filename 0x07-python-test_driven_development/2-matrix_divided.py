#!/usr/bin/python3
"""[2-matrix_divided]
    """


def matrix_divided(matrix, div):
    """matrix_divided(matrix, div)

    Arguments:
        matrix {list} -- the value is the list
        div {int]} -- the value is the int

    Raises:
        TypeError: matrix must be a  matrix (list of list) of integers/floats
        TypeError: matrix must be a  matrix (list of list) of integers/floats
        TypeError: matrix must be a  matrix (list of list) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        list -- returns div of the value the betwen the lists
    """
    str1 = "matrix must be a  matrix (list of list) of integers/floats"
    str2 = "Each row of the matrix must have the same size"
    str3 = "div must be a number"
    str4 = "division by zero"
    if type(div) not in (int, float):
        raise TypeError(str3)
    if len(matrix) == 0 or len(matrix) == 1:
        raise TypeError(str2)
    if div == 0:
        raise ZeroDivisionError(str4)
    if type(matrix) is not list:
        raise TypeError(str1)
    len1 = len(matrix[0])
    for row in matrix:
        if len(row) != len1:
            raise TypeError(str2)
        if len(row) == 0:
            raise TypeError(str1)
        if type(row) != list:
            raise TypeError(str1)
        for column in row:
            if type(column) not in (int, float):
                raise TypeError(str1)
    return [[round(column / div, 2)for column in row]for row in matrix]
