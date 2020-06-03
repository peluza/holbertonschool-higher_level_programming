#!/usr/bin/python3
"""read_lines
    """


def read_lines(filename="", nb_lines=0):
    """read_lines

    Keyword Arguments:
        filename {str} -- file name (default: {""})
        nb_lines {int} -- number the lines at read (default: {0})
    """
    with open(filename, encoding="utf-8") as my_file:
        count = 0
        if nb_lines <= 0:
            print(my_file.read())
        while count in range(nb_lines):
            line = my_file.readline()
            if not line:
                break
            count += 1
            print("{}".format(line), end='')
        return
