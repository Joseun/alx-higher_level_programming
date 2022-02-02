-- Lists number of records of the table with same scores
-- in a database on the MySQL server.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
