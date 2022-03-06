#!/usr/bin/python3
""" Script that prints the first State object from the database hbtn_0e_6_usa """
if __name__ == "__main__":
	from sys import argv
	from model_state import Base, State
	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker


	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()

	query = session.query(State).order_by(State.id).limit(1) # .first() also works
	for state in query.all():
		if state == []:
			print('Nothing')
		else:
			print('{}: {}'.format(state.id, state.name))

	session.close()
