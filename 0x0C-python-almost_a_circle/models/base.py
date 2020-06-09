#!/usr/bin/python3
"""base
    """
import json
import os
import csv


class Base:
    """Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__(self, id)

        Args:
            id (optional): autoasigned. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if type(list_dictionaries) is list:
            if list_dictionaries is None:
                list_dictionaries = []
                return list_dictionaries
            else:
                return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None and json_string != []:
            new_list = []
            return new_list
        else:
            return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
            obj.update(**dictionary)
            return obj
        elif cls.__name__ == "Square":
            obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []
        else:
            with open(
                    filename, mode="r", encoding="utf-8") as f:
                new_read = f.read()
                new_list = []
                new_json = cls.from_json_string(new_read)
                for i in new_json:
                    new_list.append(cls.create(**i))
                return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        new = []
        for obj in list_objs:
            new.append(obj.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            csv_write = csv.writer(f)
            c = 0
            for dic in new:
                if c == 0:
                    header = dic.keys()
                    h = list(header)
                    csv_write.writerow(h)
                    c += 1
                val = list(dic.values())
                csv_write.writerow(val)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        new_dict = {}
        new_list = []
        my_list = []
        if os.path.isfile(filename) is False:
            return []
        else:
            with open(filename, mode="r", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader)
                for row in reader:
                    c = 0
                    for value in row:
                        new_dict[header[c]] = int(value)
                        c += 1
                    new_list.append(new_dict)
                    new_dict = {}
                for dic in new_list:
                    my_list.append(cls.create(**dic))
                return my_list
