#!/usr/bin/python3
"""
Script that file that contains the class definition of a State 
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """this is class which represents the states table in the database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name