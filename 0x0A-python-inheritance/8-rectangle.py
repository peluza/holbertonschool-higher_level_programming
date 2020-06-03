#!/usr/bin/python3
"""5-base_geometry
    """


class BaseGeometry:
    """BaseGeometry
    """

    def area(self):
        """area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator

        Arguments:
            name {str} -- the varibel at name is str
            value {int} -- the variable at value is number interger >= 0

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle

    Arguments:
        BaseGeometry {class} -- the class is BAseGeometry
    """

    def __init__(self, width, height):
        """__init__

        Arguments:
            width {int} -- value is int
            height {int} -- value is int
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
