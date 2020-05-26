#!/usr/bin/python3
""" Documentation for Rectangle class. """


class Rectangle:
    """ defines the rectangle. """
    def __init__(self, width=0, height=0):
        """ sets up rectangle instance. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width of rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width of rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height of rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
