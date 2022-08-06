from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False, unique=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id',Integer, ForeignKey('states.id'), nullable=False)
    """def init"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.id}: {self.name}"
        # legible para el humano ,simple string
