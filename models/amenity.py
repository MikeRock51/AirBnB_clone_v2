#!/usr/bin/python3
"""Amenity model"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
#from models.place import Place



class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
