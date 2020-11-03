#!/usr/bin/python3
"""module review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review that inherites from BaseModel"""
    place_id = ""
    user_id =  ""
    text = ""
