from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', backref='state',cascade='all, delete-orphan')

    """def init"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.id}: {self.name}"
        # legible para el humano ,simple string