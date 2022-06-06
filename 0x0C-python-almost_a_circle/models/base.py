#!/usr/bin/python3
import json
from multiprocessing import dummy
"""
base
"""


class Base:
    """def class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """def init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """def method to_json_String"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """def method save_to_file"""
        name_file  = f"{cls.__name__}.json"
        new_list = []

        if list_objs is not None:
            for obj in list_objs:
                new_list += [obj.to_dictionary()]
        
        list_to_string = Base.to_json_string(new_list)

        with open(name_file, "w",encoding="UTF-8") as file:
            file.write(list_to_string)

    def from_json_string(json_string):
        """def method from_json_string"""
        if json_string is None or len(json_string):
            lista = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        It creates an instance of the class `cls` and sets the attributes of the instance to the values
        in the dictionary
        
        :param cls: The class that is being created
        """
        class_name = cls.__name__

        if class_name == "Square":
            new_class = cls(1)
        elif class_name == "Rectangle":
            new_class = cls(1,1)

        new_class.update(**dictionary)

        return new_class

    @classmethod
    def load_from_file(cls):
        """def method lead_from_file"""
        name_file = f"{cls.__name__}.json"
        new_list = []
        try:
            with open(name_file,'r') as file:
                r = file.read()
            lista_obj = cls.from_json_string(r)
            for obj in lista_obj:
                new_list.append(cls.create(**obj))
        except:
            pass

        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This function saves a list of objects to a csv file.
        
        :param cls: The class of the object that we're saving
        :param list_objs: a list of objects
        """
        name_file = f"{cls.__name__}.csv"
        new_list = []
        aux = ""

        if cls.__name__ == "Square":
            if list_objs is not None:
                for obj in list_objs:
                    new_list += [{'id': obj.id, 'size': obj.size, 'x': obj.x, 'y': obj.y}]

        if cls.__name__ == "Rectangle":
            if list_objs is not None:
                for obj in list_objs:
                    new_list += [{'id': obj.id, 'width': obj.width, 'height': obj.height, 'x': obj.x, 'y': obj.y}]

        list_to_string = Base.to_json_string(new_list)

        with open(name_file, "w",encoding="UTF-8") as file:
            file.write(list_to_string)

    @classmethod
    def load_from_file_csv(cls):
        """
        It takes a class as an argument and returns a list of instances of that class
        
        :param cls: the class that we're loading from
        """
        name_file = f"{cls.__name__}.csv"
        new_list = []
        try:
            with open(name_file,'r') as file:
                r = file.read()
            lista_obj = cls.from_json_string(r)
            for obj in lista_obj:
                new_list.append(cls.create(**obj))
        except:
            pass

        return new_list
