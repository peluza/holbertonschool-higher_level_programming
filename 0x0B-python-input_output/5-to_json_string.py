#!/usr/bin/python3
"""to_json_string
    """
import json


def to_json_string(my_obj):
    """to_json_string(my_obj)

    Arguments:
        my_obj {JSON} -- the at is the list

    Returns:
        JSON -- the content of the JSON
    """
    return json.dumps(my_obj)
