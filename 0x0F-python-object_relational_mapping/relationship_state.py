#!/usr/bin/python3
""" Script that lists cities must represent
	a relationship with the class State 
"""
if __name__ == "__main__":
	from sqlalchemy.orm import relationship


	State.cities = relationship("City", order_by=City.id, back_populates="states")
