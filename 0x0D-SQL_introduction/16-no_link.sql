-- Lists all records of the table with in a database on the MySQL server.
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
