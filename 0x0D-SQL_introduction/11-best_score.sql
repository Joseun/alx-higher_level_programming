-- Lists all records of the table with score >= 10
--- in a database on the MySQL server.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
