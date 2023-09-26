#!/usr/bin/python3
# This script is meant to filter states where names match the argument
# Imports module MySQLdb

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Replace 'username', 'password', and 'database_name' with your MySQL credentials
    engine = create_engine('mysql://username:password@localhost:3306/database_name')

    # Create the 'states' table in the database
    Base.metadata.create_all(engine)
