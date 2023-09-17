#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    This class defines a City.
        __tablename__ (str): The table name for the database table.
        name (str): The name of the City.
        state_id (str): The State ID associated with the City.
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", passive_deletes=True, backref="cities")
