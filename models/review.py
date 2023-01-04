#!/usr/bin/python3
"""Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review Class
    Attributes:
        place_id(str): The place id
        user_id(str): The user id
        text(str)"""
    place_id = ""
    user_id = ""
    text = ""
