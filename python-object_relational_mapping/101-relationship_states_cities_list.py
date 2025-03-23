#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database hbtn_0e_101_usa.
Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Step 1: Create the engine to connect to MySQL database
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}', pool_pre_ping=True)
    
    # Step 2: Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Step 3: Query all State objects, including their cities, sorted by state.id and city.id
    states = session.query(State).order_by(State.id).all()
    
    # Step 4: Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda c: c.id):
            print(f"\t{city.id}: {city.name}")
    
    # Step 5: Close the session
    session.close()

