#!/usr/bin/python3
"""
Module to get all states
"""
from sys import argv

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username, password, database = argv[1:4]
    search_name = argv[4]
    # default host is 'localhost' and default port is '3306'
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )
    session = Session(engine)
    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.name == search_name).first()
    if state is not None:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
