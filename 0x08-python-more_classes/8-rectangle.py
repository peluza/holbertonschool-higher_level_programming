#!/usr/bin/python3
"""7-rectangle
    """


class Rectangle:
    """Rectangle

    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: height must be an integer
        ValueError: height must be >= 0

    Returns:
        self -- the configurations options at neceity for example
        area, perimeter, __str__, __repr__ and __del__
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_init(self,width,height)

        Keyword Arguments:
            width {int} -- width the rectangle (default: {0})
            height {int} -- height the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * self.height + 2 * self.width

    def __str__(self):
        result = ""
        if self.width == 0 or self.height == 0:
            return result
        else:
            for i in range(self.height):
                result += "\n"
                for j in range(self.width):
                    result += str(self.print_symbol)
            return result[1:]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
