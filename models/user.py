#!/usr/bin/python3
"""module user that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user that inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
