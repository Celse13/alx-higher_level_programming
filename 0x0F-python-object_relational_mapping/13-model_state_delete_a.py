#!/usr/bin/python3
"""Retrieving the states from the database using ORM."""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=db_engine)
    Base.metadata.create_all(db_engine)
    session = Session()

    state_query = session.query(State).filter(State.name.like('%a%'))

    for state in state_query:
        session.delete(state)
    session.close()
