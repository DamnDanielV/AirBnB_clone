#!/usr/bin/python3
"""model place taht inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place that inherites from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    option = ""
    number_roms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
