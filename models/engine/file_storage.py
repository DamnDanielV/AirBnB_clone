#!/usr/bin/python3
import json


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
        d = FileStorage.__objects
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
                self.__objects = json.load(f)
                f.close()
        except:
            pass
