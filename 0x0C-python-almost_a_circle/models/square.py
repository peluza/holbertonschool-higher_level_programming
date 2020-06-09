#!/usr/bin/python3
"""square
    """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square(Rectangle)

    Args:
        Rectangle (int): the value is inter, id optional
    """

    def __init__(self, size, x=0, y=0, id=None):
        """__init__(self,size,x,y,id)

        Args:
            size (int): the size is the intenger
            x (int): the x is intenger >= 0. Defaults to 0.
            y (int): the y is intenger >= 0. Defaults to 0.
            id (optional): the id id type opcional. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return str("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        new_list = ["id", "size", "x", "y"]
        if args is not None and args != ():
            for i in range(len(new_list)):
                if i < len(args):
                    setattr(self, new_list[i], args[i])
        elif kwargs is not None and kwargs != {}:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        new_dict = {}
        new_list = ["id", "size", "x", "y"]
        for i in range(len(new_list)):
            new_dict[new_list[i]] = getattr(self, new_list[i])
        return new_dict

    @ property
    def size(self):
        return self.width

    @ size.setter
    def size(self, value):
        self.width = value
        self.height = value
