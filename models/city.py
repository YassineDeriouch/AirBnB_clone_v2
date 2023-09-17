#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(Base, BaseModel):
    """ 
	The city class
	__tablename__ :  defines 'cities' table to store Cities
        name          :  defines the city name
        state_id      :  defines the state ID of a city (states.id fk)
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
