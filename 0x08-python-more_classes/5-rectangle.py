#!/usr/bin/python3
"""  Simple rectangle """


class Rectangle:
    """ empty rectangle class """

    def __init__(self, width=0, height=0):
        """ creats instance of rectangle """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """ returns Width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width to value """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height to value """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns are of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ prints rectangle using str() """

        if self.__width == 0 or self.__height == 0:
            return ""
        rec = []
        for h in range(self.__height):
            for w in range(self.__width):
                rec.append('#')
            if h is not self.__height - 1:
                rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        """ str created that works with eval() """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints message when instance is deleted """

        print("Bye rectangle...")
