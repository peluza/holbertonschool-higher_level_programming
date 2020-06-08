#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    print(s1.area())
    s1.size = 10
    print(s1)
    print(s1.area())
    print(s1.__dict__)
