#!/usr/bin/python3
"""9-rectangle
    """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area

        Returns:
            int -- number intergert
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__

        Returns:
            str -- the result in str format
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
