#!/usr/bin/python3
"""100-my_int
    """


class MyInt(int):
    """MyInt(int)

    Arguments:
        int {int} -- the value is number
    """

    def __ne__(self, other):
        return True

    def __eq__(self, other):
        return False
