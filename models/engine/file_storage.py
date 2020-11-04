#!/usr/bin/python3
"""module file_storage.py"""
import json
from models.user import User
from ..base_model import BaseModel
to_dict = BaseModel.to_dict


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
        key_object = '{}.{}'.format(type(obj).__name__, obj.id)
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
                c_k = key.split('.')
                self.__objects[key] = eval(
                    "{}(**{})".format(c_k[0], value)
                )
        except:
            pass
