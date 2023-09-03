#!/usr/bin/env python3
"""
Module that defines the State class and creates a database table.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class represents a database table 'states'.

    Attributes:
        id (int): An auto-generated, unique integer representing the primary key.
        name (str): A string representing the name of the state.

    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    print("Table 'states' created.")
