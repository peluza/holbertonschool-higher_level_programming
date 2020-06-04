#!/usr/bin/python3
"""pascal_triangle
    """


def pascal_triangle(n):
    """pascal_triangle(n)

    Arguments:
        n {int} -- the number at row

    Returns:
        list -- the pascal triangle
    """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_n = [1]
        result = pascal_triangle(n-1)
        last_n = result[-1]
        for i in range(len(last_n)-1):
            new_n.append(last_n[i] + last_n[i+1])
        new_n += [1]
        result.append(new_n)
    return result
