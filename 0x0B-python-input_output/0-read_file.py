#!/usr/bin/python3
"""read_file
    """


def read_file(filename=""):
    """read_file(filename)

    Keyword Arguments:
        filename {str} -- name of the file (default: {""})
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end='')
