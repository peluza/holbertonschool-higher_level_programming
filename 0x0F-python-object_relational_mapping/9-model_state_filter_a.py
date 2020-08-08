#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database
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
    for instance in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        if instance is not None:
            print("{:d}: {:s}".format(instance.id, instance.name))
        else:
            print("Nothing")
