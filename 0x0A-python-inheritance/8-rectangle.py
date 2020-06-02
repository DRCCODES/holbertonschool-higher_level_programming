#!/usr/bin/python3
""" Doc for Base Geometry and Rectangle Class """


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ not implemented raises exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validates the value given """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class Rectangle inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Init of Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
