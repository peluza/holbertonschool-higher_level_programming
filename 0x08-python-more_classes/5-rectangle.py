#!/usr/bin/python3
"""5-rectangle
    """


class Rectangle:
    """Rectangle
    """

    def __init__(self, width=0, height=0):
        """the Rectangle__init__

        Keyword Arguments:
            width {int} -- width the rectangle (default: {0})
            height {int} -- height the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * self.height + 2 * self.width

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for i in range(1, self.height):
                result = "#" * self.width
                print(result)
            return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
