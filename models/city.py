#!/usr/bin/pyhon3
"""defines a city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city class
    Attributes:
        state_id(str): state id
        name(str): name of city"""
    state_id = ""
    name = ""
