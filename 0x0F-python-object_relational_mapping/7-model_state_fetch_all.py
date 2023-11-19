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
    session = Session()
    Base.metadata.create_all(db_engine)

    s_tate = session.query(State).order_by(State.id).all()
    for item in s_tate:
        print("{}: {}".format(item.id, item.name))

    session.close()
