#!/usr/bin/python3
"""
Start link class to table in database
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """def state"""
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    def __init__(self, name):
        """def init"""
        self.name = name

    def __str__(self):
        """def str"""
        return f"{self.id}: {self.name}"
        # legible para el humano ,simple string
