#!/usr/bin/python3
"""base model project AirBnB"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """class base model"""
    def __init__(self, *args, **kwargs):
        """initialize an instance"""
        self.updated_at = datetime.now(tz=None)
        if kwargs:
            accepted_args = ['created_at', 'id', 'my_number', 'updated_at']
            for key, value in kwargs.items():
                if key in accepted_args:
                    self.id = kwargs['id']
                    a_d_c = str(kwargs['created_at'])
                    ad_c_2 = datetime.strptime(a_d_c, '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = ad_c_2
                    a_d_u = str(kwargs['updated_at'])
                    ad_u_2 = datetime.strptime(a_d_u, '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = ad_u_2
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(tz=None)
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """returns a string representation"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the current date time"""
        self.updated_at = datetime.now(tz=None)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing keys/values"""
        return {
                "id": self.id,
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "created_at": self.created_at.isoformat()
                }
