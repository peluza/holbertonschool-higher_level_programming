#!/usr/bin/python3
"""0-lookup
    """


def lookup(obj):
    """lookup

    Arguments:
        obj {obj} --  the list of available attributes and methods of an object

    Returns:
        [list] -- the list of available attributes and methods of an object
    """
    return (dir(obj))
