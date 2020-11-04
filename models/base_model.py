#!/usr/bin/python3
"""base model project AirBnB"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """class base model"""
    def __init__(self, *args, **kwargs):
        """initialize an instance"""
        if kwargs:
            self.__dict__ = kwargs
            try:
                self.__dict__['updated_at'] = datetime.strptime(
                    self.__dict__['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__['created_at'] = datetime.strptime(
                    self.__dict__['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            except Exception as e:
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """returns a string representation"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the current date time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing keys/values"""
        return {
                "id": self.id,
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "created_at": self.created_at.isoformat()
                }
