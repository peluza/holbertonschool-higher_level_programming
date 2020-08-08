#!/usr/bin/python3
"""prints the State object with the name passed as argument from the database
    """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name.like(sys.argv[4])):
        if instance.id is not None:
            print("{:d}".format(instance.id))
            break
    else:
        print("Not found")
