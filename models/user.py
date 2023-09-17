#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
     """
        This class defines a user by various attributes

        email      : user's email
        password   : user's password
        first_name : user's first name
        last_name  : user's last name
        places     : User-Place relationship
        reviews    : User-Review relationship

    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", passive_deletes=True, backref="user")
    reviews = relationship("Review", passive_deletes=True, backref="user")
