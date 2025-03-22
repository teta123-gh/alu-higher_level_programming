#!/usr/bin/python3
"""
Base module
"""
import csv
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return dict representation of json_string
        """
        if (json_string is None or
                json_string == "[]" or
                json_string == ""):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create instance with attributes set from dictionary
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Load JSON from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save dict to CSV
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "w", newline="") as csvfile:
                if list_objs is None or list_objs == []:
                    csvfile.write("[]")
                else:
                    if cls.__name__ == "Rectangle":
                        fieldnames = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())
        except IOError:
            pass

    @classmethod
    def load_from_file_csv(cls):
        """
        Load CSV to dict
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
