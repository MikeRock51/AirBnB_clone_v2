#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models

class State(BaseModel, Base):
    """ State class """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete',
                            backref='states')
    else:
        name = ""
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("HAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHA")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """ Getter for cities attribute. """
            stored_cities = models.storage.all("City")
            return [city for city in stored_cities.values() if city.state_id == self.id]
