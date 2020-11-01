#!/usr/bin/python3
import json

from models.user import User
from ..base_model import BaseModel
to_dict = BaseModel.to_dict

class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key_object = '{}.{}'.format(type(obj).__name__, obj.id)
        self.__objects[key_object] = obj

    def save(self):
        """serializes """
        file = self.__file_path
        d = self.__objects
        dict_obj = {}
        for key, value in d.items():
            dict_obj[key] = value.to_dict()
        with open(file, "w") as f:
            json.dump(dict_obj, f)

    def reload(self):
        """if file exists, deserializes"""
        file_name = self.__file_path
        try:
            with open(file_name, "r") as f:
                new_obj = json.load(f)
            for key, value in new_obj.items():
                if BaseModel.__name__ in key:
                    self.__objects[key] =  BaseModel(value)
        except:
            pass
