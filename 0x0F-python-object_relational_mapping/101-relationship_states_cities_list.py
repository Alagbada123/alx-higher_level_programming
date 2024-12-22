#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects from the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine and bind to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Establish session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query States and their related Cities, ordered by State.id and City.id
    states = session.query(State).order_by(State.id, City.id).all()

    # Iterate and print results in the required format
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

