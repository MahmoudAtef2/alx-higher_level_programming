#!/usr/bin/python3
'''Module for Base class'''
from json import dumps, loads
import csv
import turtle


class Base:
    '''representation of Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the JSON serialization of a list of dicts.'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Write the JSON serialization of a list of objects in a file.'''
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Return the deserialization of a JSON string'''
        if json_string is None or json_string == []:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Return a class instantied from a dictionary of attributes'''
        if dictionary and not {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            else:
                new = None
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''Return a list of classes instantiated from a file of JSON strings'''
        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, "r") as f:
            list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write the CSV serialization of a list of objects to a file'''
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of classes instantiated from a CSV file'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''Draw Rectangles and Squares using the turtle module'''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
