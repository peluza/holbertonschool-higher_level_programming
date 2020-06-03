#!/usr/bin/python3
"""load_from_json_file
    """
import json


def load_from_json_file(filename):
    """load_from_json_file(filename)

    Arguments:
        filename {str} -- file name at read

    Returns:
        JSON -- the read at JSON
    """
    with open(filename, encoding="utf-8") as my_file:
        js = my_file.read()
        return json.loads(js)
