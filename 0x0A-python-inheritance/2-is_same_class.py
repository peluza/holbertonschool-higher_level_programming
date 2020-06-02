#!/usr/bin/python3

def is_same_class(obj, a_class):
    """is_same_class

    Arguments:
        obj -- the obj at analyze the type
        a_class -- the type at anlayze of the obj

    Returns:
        type -- the instanse fo the class
    """
    return type(obj) == a_class
