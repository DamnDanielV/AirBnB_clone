#!/usr/bin/python3
"""module user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user that inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
