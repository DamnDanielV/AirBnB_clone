#!/usr/bin/python3
"""
module city that inherits from base model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that unherits from BaseModel"""
    state_id = ""
    name = ""
