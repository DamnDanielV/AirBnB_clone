#!/usr/bin/python3
""" Module file storage to handled objects """

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obje with key and id"""
        key_object = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key_object] = obj

    def save(self):
        """serializes objects to the json file"""
        file = self.__file_path
        d = self.__objects
        dict_obj = {}
        for key, value in d.items():
            dict_obj[key] = value.to_dict()
        with open(file, "w") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """if file exists, deserializes JSON file"""
        file_name = self.__file_path
        try:
            with open(file_name, "r") as f:
                new_obj = json.load(f)
            for key, value in new_obj.items():
                self.__objects[key] = eval(
                    value['__class__'] + '(**value)'
                )
        except:
            pass
