#!/usr/bin/python3
import json
import csv
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
        name_file = f"{cls.__name__}.json"
        new_list = []

        if list_objs is not None:
            for obj in list_objs:
                new_list += [obj.to_dictionary()]

        list_to_string = Base.to_json_string(new_list)

        with open(name_file, "w", encoding="UTF-8") as file:
            file.write(list_to_string)

    def from_json_string(json_string):
        """def method from_json_string"""
        if json_string is None or len(json_string):
            lista = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """def method create"""
        class_name = cls.__name__

        if class_name == "Square":
            new_class = cls(1)
        elif class_name == "Rectangle":
            new_class = cls(1, 1)

        new_class.update(**dictionary)

        return new_class

    @classmethod
    def load_from_file(cls):
        """def method lead_from_file"""
        name_file = f"{cls.__name__}.json"
        new_list = []
        try:
            with open(name_file, 'r') as file:
                r = file.read()
            lista_obj = cls.from_json_string(r)
            for obj in lista_obj:
                new_list.append(cls.create(**obj))
        except Exception:
            pass
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """def method save_to file csv"""
        name_file = f"{cls.__name__}.csv"

        if cls.__name__ == "Square":
            if list_objs is not None:
                with open(name_file, 'w', newline='') as student_file:
                    writer = csv.writer(student_file)
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

        if cls.__name__ == "Rectangle":
            if list_objs is not None:
                with open(name_file, 'w', newline='') as student_file:
                    writer = csv.writer(student_file)
                    for obj in list_objs:
                        lista = [obj.id, obj.width, obj.height, obj.x, obj.y]
                        writer.writerow(lista)

    @classmethod
    def load_from_file_csv(cls):
        """def method load_from_file_csv"""
        name_class = cls.__name__
        name_file = f"{cls.__name__}.csv"
        new_list = []

        with open(name_file, 'r') as file:
            fileread = csv.reader(file)
            for obj in fileread:
                if name_class == 'Square':
                    dic_obj = {"id": int(obj[0]), "size": int(obj[1]),
                               "x": int(obj[2]), "y": int(obj[3])}

                if name_class == 'Rectangle':
                    dic_obj = {"id": int(obj[0]), "width": int(obj[1]),
                               "height": int(obj[2]), "x": int(obj[3]),
                               "y": int(obj[4])}

                new_list.append(cls.create(**dic_obj))

        return new_list
