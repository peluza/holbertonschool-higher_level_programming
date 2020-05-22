#!/usr/bin/python3
"""3-say_my_name
    """


def say_my_name(first_name, last_name=""):
    """say_my_name

    Arguments:
        first_name {str} -- the value is the first_name

    Keyword Arguments:
        last_name {str} -- the value is the las_name (default: {""})

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    Returns:
        str -- My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    result = print("My name is {} {}".format(first_name, last_name))
    return result
