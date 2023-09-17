#!/usr/bin/python3
""" Place """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv

class Place(BaseModel, Base):
    """
    This class defines a Place.

    Attributes:
        __tablename__ (str): The table name for the database table.
        city_id (str): The ID of the associated City.
        user_id (str): The ID of the owner User.
        name (str): The name of the Place.
        description (str): The description of the Place.
        number_rooms (int): The number of rooms in the Place.
        number_bathrooms (int): The number of bathrooms in the Place.
        max_guest (int): The maximum number of guests the Place can accommodate.
        price_by_night (int): The price per night to stay at the Place.
        latitude (float): The latitude coordinate of the Place.
        longitude (float): The longitude coordinate of the Place.
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances with
            place_id equals to the current Place.id"""
            review_list = []
            for review in list(models.storage.all("Review").values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

