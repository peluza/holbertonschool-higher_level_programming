#!/usr/bin/python3
"""save_to_json_file
    """
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file(my_obj, filename)

    Arguments:
        my_obj {JSON} -- objets at JSON
        filename {str} -- filename at crate

    Returns:
        JSON -- create at file the format JSON
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(json.dumps(my_obj))
