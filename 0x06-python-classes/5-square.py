#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """class Square.size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """class Square.area"""
        return self.__size * self.__size

    def my_print(self):
        """class size"""
        if self.size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """class size"""
        return self.__size

    @size.setter
    def size(self, value):
        """class size.value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
