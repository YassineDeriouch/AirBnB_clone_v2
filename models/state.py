#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

class State(Base, BaseModel):
    """ State class """
    """
        __tablename__   :  defines MySQL table to store States.
        name            :  defines the name of the State.
        cities          :  desines the State-City relationship.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    @property
    def cities(self):
	""" cities funtion to returns the list of cities having state.id == thecurrent State_id"""
        from models import storage
        citiesList = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                citiesList.append(city)
        return citiesList
