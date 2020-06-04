#!/usr/bin/python3
"""student
    """


class Student:
    """Student
    """

    def __init__(self, first_name, last_name, age):
        """__init__(self, first_name, last_name, age)

        Arguments:
            first_name {str} -- the first name of the students
            last_name {str} -- the last name of the students
            age {int} -- the age of the students
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if attrs is None:
            return self.__dict__
        else:
            copy_dic = self.__dict__
            for k, v in copy_dic.items():
                if k in attrs:
                    dic[k] = v
            return dic

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
