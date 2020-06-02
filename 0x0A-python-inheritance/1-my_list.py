#!/usr/bin/python3
"""1-my_list
    """


class MyList (list):
    """Mylist

    Arguments:
        list {list} -- the arguments is the list
    """

    def __init__(self):
        pass

    def print_sorted(self):
        """print_sorted

        Returns:
            [list] -- print the list
        """
        new_list = sorted(self)
        print(new_list)
        return new_list
