#!/usr/bin/python3

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """
    This class defines a City by its name.
        __tablename__ (str): The table name for the database table.
        name (str): The name of the City.
        state_id (str): The State ID associated with the City.
    """

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False
