#!/usr/bin/python3
""" Doc for BASE CLASS """


import json
import os


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init id """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON of Dict """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON string to rep of listobj to file """

        if list_objs is None or len(list_objs) == 0:
            listo = []
        else:
            listo = []
            for item in list_objs:
                listo.append(item.to_dictionary())
        jstr = Base.to_json_string(listo)
        
        with open("{}.json".format(cls.__name__), mode="w")\
                as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON str rep """

        if json_string is None or not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with attr set """

        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            dummy = cls(7, 7)
        if cls == Square:
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return list of instances """

        filename = "{}.json".format(cls.__name__)

        if os.path.isfile(filename):
            insta_l = []
            with open(filename) as f:
                insta_o = cls.from_json_string(f.read())
                for dic in insta_o:
                    insta_l.append(cls.create(**dic))
            return insta_l

        return []







