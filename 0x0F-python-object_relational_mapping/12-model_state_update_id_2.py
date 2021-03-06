#!/usr/bin/python3
""" Script that changes the name of a State object
    from the database hbtn_0e_6_usa """


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
    state_id_2 = session.query(State).filter_by(id=2).first()
    state_id_2.name = 'New Mexico'
    session.commit()
    session.close()
