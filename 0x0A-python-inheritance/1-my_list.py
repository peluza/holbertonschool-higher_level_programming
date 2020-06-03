#!/usr/bin/python3
"""1-my_list
    """


class MyList (list):
    """Mylist

    Arguments:
        list {list} -- the arguments is the list
    """

    def print_sorted(self):
        """print_sorted

        Returns:
            [list] -- print the list
        """
        print(sorted(self))
