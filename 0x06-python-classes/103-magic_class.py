#!/usr/bin/python3
""" Magic Calcultor """
import math


class MagicClass:
    """ class with radius gets Area and Circumference """
    def __init__(self, radius):
        """get radius"""
        self.radius = 0
        if type(radius) is not float and is not int:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """ Get area! """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ Get Circumference """
        return (2 * math.pi * self.__radius)
