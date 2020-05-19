#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int and type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 and position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
       if (self.__size != 0):
            print(('\n' * self.__position[1]), end="")
            for i in range(self.__size):
                print((" " * self.__position[0]), end='')
                print ("#" * self.__size)
            else:
                print("")

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int and type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def my_print(self):
       if (self.__size != 0):
            print(('\n' * self.__position[1]), end="")
            for i in range(self.__size):
                print((" " * self.__position[0]), end='')
                print ("#" * self.__size)
            else:
                print("")