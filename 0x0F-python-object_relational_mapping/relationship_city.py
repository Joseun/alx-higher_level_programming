#!/usr/bin/python3
""" Script that lists cities must represent
    a relationship with the class City 
"""
if __name__ == "__main__":
	from sqlalchemy.orm import relationship


	state = relationship("State", back_populates="cities")
