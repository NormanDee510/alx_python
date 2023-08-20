#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Define the Base class
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table based on the class definition
    Base.metadata.create_all(engine)
