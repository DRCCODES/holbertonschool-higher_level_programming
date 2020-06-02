#!/usr/bin/python3
""" Doc for Base Geometry """


class BaseGeometry:
    """ Base Geometry Class """

    def area(self):
        """ doc for BaseGeometry area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """" function that validates the value given """

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
