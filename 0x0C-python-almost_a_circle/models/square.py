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
                                                 self.width)

    @property
    def size(self):
        """ sets size of square """

        return self.width

    @size.setter
    def size(self, value):
        """ sets sizes uses width  and height """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates square! """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                for key in kwargs.keys():
                    if key == "id":
                        self.id = kwargs["id"]
                    if key == "size":
                        self.width = kwargs["size"]
                        self.height = kwargs["size"]
                    if key == "x":
                        self.x = kwargs["x"]
                    if key == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """ creats dict of attributes """

        dic = {}

        dic["id"] = self.id
        dic["size"] = self.width
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
