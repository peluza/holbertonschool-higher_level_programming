#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Arguments:
        obj  -- the obj at analyze the type and the class
        a_class  -- the type at anlayze of the obj

    Returns:
        type -- the instanse fo the class
    """
    return isinstance(obj, a_class)
