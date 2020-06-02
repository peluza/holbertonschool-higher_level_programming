#!/usr/bin/python3
"""10-square
    """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square(Rectangle)

    Arguments:
        Rectangle {int} -- call class Rectangle
    """

    def __init__(self, size):
        """__init__(self,size)

        Arguments:
            size {int} -- the number at size for square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
