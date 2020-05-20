#!/usr/bin/python3
"""class Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """class Square.position"""
        self.position = position
        self.size = size

    def area(self):
        """class Square.area"""
        return self.__size * self.__size

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

    @property
    def position(self):
        """class position"""
        return self.__position

    @position.setter
    def position(self, value):
        """class position.value"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """class position.my_print"""
        if (self.__size == 0):
            print("")
            return
        else:
            for x in range(self.__position[1]):
                print("")
            for y in range(self.size):
                for i in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
