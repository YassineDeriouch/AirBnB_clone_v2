#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
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
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
