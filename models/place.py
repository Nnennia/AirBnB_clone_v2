#!/usr/bin/python3
"""Place Class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A Place Class
    Attributes:
        city_id(str): city id
        user_id(str): user id
        name(str)
        descripition(str)
        number_rooms(int)
        max_guest(int)
        price_by_night(int)
        latitude(float)
        longitude(float)
        amenity_ids: List of amenity.id(str)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
