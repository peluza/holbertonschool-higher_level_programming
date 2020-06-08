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
        if type(list_dictionaries) is list:
            if list_dictionaries is None:
                list_dictionaries = []
                return list_dictionaries
            else:
                return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        if list_objs is None:
            with open(
                    cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
                f.write(new_list)
        else:
            for i in list_objs:
                new_list.append(i.to_dictionary())
            new_json = cls.to_json_string(new_list)
            with open(
                    cls.__name__ + ".json", mode="w", encoding="utf-8") as f:
                f.write(new_json)
