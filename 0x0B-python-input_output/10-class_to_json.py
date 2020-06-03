#!/usr/bin/python3
"""class_to_json
    """


def class_to_json(obj):
    """class_to_json(json)

    Arguments:
        obj {str} -- the value at the dictory

    Returns:
        dict -- returns the cointains obj at dictory
    """
    return obj.__dict__
