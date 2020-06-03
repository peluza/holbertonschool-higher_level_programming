#!/usr/bin/python3
"""add_item
    """
import sys
import os

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"

if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
    my_list += sys.argv[1:]
    save_to_json_file(list(my_list), filename)
else:
    save_to_json_file(list(sys.argv[1:]), filename)
