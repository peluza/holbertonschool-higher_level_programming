#!/usr/bin/python3
"""rectangle
    """
from models.base import Base


class Rectangle(Base):
    """class Rectangle(Base)

    Args:
        Base (int): asigned at ID
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__(width,height,x,y,id)

        Args:
            width (int): the width is the intenger
            height (int): the height is the intenger
            x (int): the x is intenger >= 0. Defaults to 0.
            y (int): the y is intenger >= 0. Defaults to 0.
            id (optional): the id id type opcional. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        return self.__width * self.__height

    def display(self):
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        new_list = ["id", "width", "height", "x", "y"]
        if args is not None and args != ():
            for i in range(len(new_list)):
                if i < len(args):
                    setattr(self, new_list[i], args[i])
        elif kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        new_dict = {}
        new_list = ["id", "width", "height", "x", "y"]
        for i in range(len(new_list)):
            new_dict[new_list[i]] = getattr(self, new_list[i])
        return new_dict

    @ property
    def width(self):
        return self.__width

    @ width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @ property
    def height(self):
        return self.__height

    @ height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @ property
    def x(self):
        return self.__x

    @ x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @ property
    def y(self):
        return self.__y

    @ y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value
