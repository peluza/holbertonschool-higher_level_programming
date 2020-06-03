#!/usr/bin/python3
"""8-rectangle
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
