#!/usr/bin/python3
"""number of lines
    """


def number_of_lines(filename=""):
    """number_of_lines(filename)

    Keyword Arguments:
        filename {str} -- the file name (default: {""})

    Returns:
        int -- the number of the lines
    """
    with open(filename, encoding="utf-8") as my_file:
        count = 0
        while True:
            line = my_file.readline()
            if not line:
                break
            count += 1
        return count
