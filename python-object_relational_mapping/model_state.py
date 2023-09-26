#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine(
        'mysql://username:password@localhost:3306/database_name')
    # Create the 'states' table in the database
    Base.metadata.create_all(engine)
