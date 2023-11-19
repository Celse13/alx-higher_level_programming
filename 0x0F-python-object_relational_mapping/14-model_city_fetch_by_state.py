#!/usr/bin/python3
"""Retrieving the states from the database using ORM."""


from model_state import Base, State
from sys import argv
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()
    Base.metadata.create_all(db_engine)

    state_query = session.query(State, City).join(City).order_by(City.id)

    for column_state, city in state_query:
        print("{}: ({}) {}".format(column_state.name, city.id, city.name))

    session.close()
