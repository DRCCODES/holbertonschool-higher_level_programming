#!/usr/bin/python3
"""  Simple rectangle """


class Rectangle:
    """ empty rectangle class """

    def __init__(self, width=0, height=0)
        """ creats instance of rectangle """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width > 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif width > 0:
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
        elif width > 0:
            raise ValueError("value must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets width to value """

        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif width > 0:
            raise ValueError("value must be >= 0")
        else:
            self.__height = value

    def area(self):
       """returns are of rectangle"""

       return self.__width * self.__width

   def perimeter(self):
       """ returns perimeter of rectangle """

       if width == 0 or height == 0:
           return 0

       return 2*(height + width)
