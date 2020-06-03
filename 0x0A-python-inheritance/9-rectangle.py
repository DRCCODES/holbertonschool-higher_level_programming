#!/usr/bin/python3
""" Doc for Rectangle Class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Init of Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns Area Of Rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ for use in print() and str() """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
