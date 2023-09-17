#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """
    This class defines a Review.

    Attributes:
        __tablename__ (str): The table name for the database table.
        text (str): The text of the review (maximum 1024 characters).
        place_id (str): The ID of the associated Place.
        user_id (str): The ID of the associated User.
    """

    __tablename__ = 'reviews'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    text = Column(String(1024), nullable=False)
