#!/usr/bin/python3
"""The state model"""


from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """The state class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """Returns all cities associated the state instnce"""
            from models.city import City

            stateCities = []
            allCities = storage.all(City)
            for instance in allCities.values():
                if instance.state_id == self.id:
                    stateCities.append(instance)
            return stateCities
