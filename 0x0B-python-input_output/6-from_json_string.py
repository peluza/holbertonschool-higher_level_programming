#!/usr/bin/python3
"""from_json_string
    """
import json


def from_json_string(my_str):
    """from_json_string(my_str)

    Arguments:
        my_str {str} -- the obj

    Returns:
        JSON -- JSON the format
    """
    return json.loads(my_str)
