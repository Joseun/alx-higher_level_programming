#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
	import MySQLdb
	from sys import argv

	db = MySQLdb.connect(
		host = "localhost",
		port = 3306,
		user = argv[1],
		password = argv[2],
		database = argv[3]
	)
	cur = db.cursor()
	cur.execute("SELECT * FROM states ORDER BY id ASC")
	states = cur.fetchall()
	for state in states:
		print(state)
	cur.close()
	db.close()
