#!/usr/bin/python3
""" Script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for state in query.all():
        if state.name == argv[4]:
            print(state.id)
            break
    else:
        print('Not found')
    # if id:
    # print(id)
    # else:
    # print('Not found')
    session.close()
