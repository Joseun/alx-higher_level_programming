#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
	import MySQLdb
	from sys import argv

	conn = MySQLdb.connect(
		host="localhost",
		port=3306,
		user=argv[1],
		password=argv[2],
		database=argv[3],
	)
	cur = conn.cursor()
	cur.execute("SELECT * FROM states ORDER BY id ASC")
	query_rows = cur.fetchall()
	for rows in query_rows:
		print(row)
	cur.close()
	conn.close()
