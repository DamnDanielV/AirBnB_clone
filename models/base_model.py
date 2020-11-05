#!/usr/bin/python3
"""base model project AirBnB"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """class base model"""
    def __init__(self):
        """initialize an instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string representation"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the current date time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing keys/values"""
        r_dict = self.__dict__.copy()
        for key in r_dict:
            if key == 'created_at':
                r_dict[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                r_dict[key] = self.updated_at.isoformat()
            elif key == 'id':
                r_dict[key] = self.id

        r_dict['__class__'] = self.__class__.__name__

        return r_dict
