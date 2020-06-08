#!/usr/bin/python3
"""base
    """
import json


class Base:
    """Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__(self,id)

        Args:
            id (int, optional): the asifned at id  . Defaults to None.
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list(list_dictionaries))
