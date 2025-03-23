#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
Usage: ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State

if __name__ == "__main__":
    # Step 1: Create the engine to connect to MySQL database
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}', pool_pre_ping=True)
    
    # Step 2: Create a session factory
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Step 3: Query all City objects and access their related State using the relationship
    cities = session.query(City).order_by(City.id).all()
    
    # Step 4: Print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    
    # Step 5: Close the session
    session.close()

