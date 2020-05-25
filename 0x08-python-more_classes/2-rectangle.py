#!/usr/bin/python3
"""2-rectangle
    """


class Rectangle:
    def __init__(self, width=0, height=0):
        """the Rectangle__init__

        Keyword Arguments:
            width {int} -- width the rectangle (default: {0})
            height {int} -- height the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    def area(self):
        """area

        Returns:
            self -- width * height
        """
        return self.width * self.height

    def perimeter(self):
        """perimeter

        Returns:
            self -- 2 * height + 2 * width
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * self.height + 2 * self.width

    @property
    def width(self):
        """width (self)

        Returns:
            self -- width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width (self,value)

        Arguments:
            value {int} -- value is at intenger positve

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """heigth(self)

        Returns:
            self -- height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """heigth(self, value)

        Arguments:
            value {int} -- value is the number interger positive

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
