#!/usr/bin/python3
"""Retrieving the states from the database using ORM."""


import sys
from my_model_module import MyModelBase, MyModelState
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    MyModelBase.metadata.create_all(db_engine)
    Session = sessionmaker(bind=db_engine)
    db_session = Session()

    for obj in db_session.query(MyModelState).order_by(MyModelState.id):
        print(obj.id, obj.name, sep=": ")
