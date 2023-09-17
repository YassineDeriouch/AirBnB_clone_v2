#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel, Base):
    """
    This class defines a Place for MySQL DB.

        __tablename__    : The table name for the database table.
        city_id          : The City ID associated with the Place.
        user_id          : The User ID associated with the Place.
        name             : The name of the Place.
        description      : The description of the Place.
        number_rooms     : The number of rooms in the Place.
        number_bathrooms : The number of bathrooms in the Place.
        max_guest        : The maximum number of guests the Place can accommodate.
        price_by_night   : The price per night for the Place.
        latitude         : The latitude coordinate of the Place.
        longitude        : The longitude coordinate of the Place.
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
    latitude = Column(Float)
    longitude = Column(Float)
