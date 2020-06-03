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

    def to_json(self):
        return self.__dict__
