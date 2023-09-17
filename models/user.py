#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
     """
        This class defines a user

        email      : user's email
        password   : user's password
        first_name : user's first name
        last_name  : user's last name

    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
