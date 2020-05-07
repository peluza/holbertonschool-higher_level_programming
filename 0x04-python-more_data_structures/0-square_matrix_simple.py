#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    f = []
    for i in matrix:
        f.append(list(map(lambda i: i*i, i)))
    return f
