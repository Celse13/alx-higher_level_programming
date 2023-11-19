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

    state_one = State(name='California')
    state_two = City(name='San Francisco', state=state_one)
    session.add_all([state_one, state_two])
    session.commit()
    session.close()
