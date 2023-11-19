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

    city_query = session.query(State).order_by(State.id)
    for state in city_query:
        print("{state.id}: {state.name}")
        for city in state.cities:
            print("    {city.id}: {city.name}")
