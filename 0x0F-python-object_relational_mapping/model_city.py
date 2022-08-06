#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)
    """def init"""
    def __init__(self, name, state_id):
        self.name = name
        self.state_id

    def __str__(self):
        return f"{self.id}: {self.name}"
        # legible para el humano ,simple string
