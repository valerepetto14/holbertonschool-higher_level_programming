#!/usr/bin/python3
import json
from xxlimited import new
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

