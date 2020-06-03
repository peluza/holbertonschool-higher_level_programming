#!/usr/bin/python3
"""4-inherints_from
    """


def inherits_from(obj, a_class):
    """inherits_from

    Arguments:
        obj  -- the obj at analyze the type and the class
        a_class -- the type at anlayze of the obj

    Returns:
        type -- eturns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
