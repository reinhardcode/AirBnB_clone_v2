#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

st = getenv("HBNB_TYPE_STORAGE")

if st == "db":
    class State(BaseModel, Base):
        """ State class """

        __tablename__ = "states"

        name = Column(String(128), nullable=False)

        cities = relationship("City", cascade="all,delete, delete-orphan, merge, save-update", back_populates="state")
else:
    class State(BaseModel):
        name = ""
        @property
        def cities(self):
            """getter method for the filestorage"""

            from models import storage
            all_cities = storage.all(City)
            cities =[]

            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
