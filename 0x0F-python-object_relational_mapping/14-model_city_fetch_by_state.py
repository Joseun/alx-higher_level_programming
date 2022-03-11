#!/usr/bin/python3
""" Script that lists all all City objects
    from the database hbtn_0e_14_usa
"""


if __name__ == "__main__":
    from sys import argv
    from model_city import Base, City, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City)\
                   .filter(State.id == City.state_id)\
                   .order_by(City.id)
    for state, city in query.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
