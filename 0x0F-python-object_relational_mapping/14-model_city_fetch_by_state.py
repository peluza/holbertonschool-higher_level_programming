#!/usr/bin/python3
""" deletes all State objects with a name containing the letter
a from the database
    """
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State, City).join(City).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(instance.State.name,
                                         instance.City.id, instance.City.name))
