#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage

class State(BaseModel, Base):
    """ State class """
    """
        __tablename__   :  defines MySQL table to store States.
        name            :  defines the name of the State.
        cities          :  desines the State-City relationship.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="all")

    @property
    def cities(self):
        citiesList = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                citiesList.append(city)
        return citiesList
