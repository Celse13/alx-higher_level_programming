#!/usr/bin/python3
"""Retrieving the states from the database using ORM."""


from sqlalchemy import create_engine
from sys import argv
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()
    Base.metadata.create_all(db_engine)

    ist = session.query(City).outerjoin(State).all()
    if ist:
        for city in ist:
            print(f"{city.id}: {city.name} -> {city.state.name}")
