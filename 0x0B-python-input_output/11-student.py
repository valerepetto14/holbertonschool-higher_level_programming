#!/usr/bin/python3
"""
Write a class Student that defines a student by:
"""


class Student:
    """def class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """def to_json"""
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for atribute in attrs:
                if atribute in self.__dict__.keys():
                    dictionary[atribute] = self.__dict__[atribute]
            return dictionary

    def reload_from_json(self, json):
        """def reload from json"""
        for key, value in json.items():
            setattr(self, key, value)
