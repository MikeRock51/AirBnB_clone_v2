#!/usr/bin/python3
"""The state model"""


from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
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
            stateCities = []
            for key, value in FileStorage.__objects.items():
                if value.to_dict().__class__ == 'City'\
                        and value.to_dict().state_id == self.id:
                    stateCities.append(value)
            return stateCities
