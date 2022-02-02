-- Displays the top 3 of city temperature during July and August in a table in hbtn_0c_0 on my SQL server
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
