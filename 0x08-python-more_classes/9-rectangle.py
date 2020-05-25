#!/usr/bin/python3
"""  Simple rectangle """


class Rectangle:
    """ empty rectangle class """
    number_of_instances = 0

    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                rec.append(str(self.print_symbol))
            if h is not self.__height - 1:
                rec.append("\n")
        return "".join(rec)

    def __repr__(self):
        """ str created that works with eval() """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ prints message when instance is deleted """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """ compares rectangles by area """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.height * rect_1.width
        area2 = rect_2.height * rect_2.height

        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ redefines values to make square """

        return cls(size, size)
