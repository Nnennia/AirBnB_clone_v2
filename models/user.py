#!/usr/bin/python3
"""Defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A user class

    Attributes:
        email(str), password(str), first_name(str), last_name(str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
