#!/usr/bin/python3
""" Doc for Class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ The Square Class! """

    def __init__(self, size, x=0, y=0, id=None):
        """ inits for instance of square uses super() """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ over rides print for wanted format """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
