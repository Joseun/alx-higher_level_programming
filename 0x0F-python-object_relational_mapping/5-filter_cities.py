#!/usr/bin/python3
""" a script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC"
            )
    cities = cur.fetchall()
    filteredcities = []
    for city in cities:
        state = city[2]
        city = city[1]
        if state == argv[4]:
            filteredcities.append(city)
    print(", ".join(filteredcities))
    cur.close()
    db.close()
