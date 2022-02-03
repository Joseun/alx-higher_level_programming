-- Script that lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities ASC c
INNER JOIN states AS s
ON s.id = c.state_id
ORDER BY c.id ASC;