#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r49 = Rectangle(4, 6)
    print(r49)
    r50 = Rectangle(8, 4, 3)
    print(r50)
    r51 = Rectangle(3, 3, 3, 9)
    print(r51)
    r52 = Rectangle(4, 2, 3, 9, "Holberton")
    print(r52)
