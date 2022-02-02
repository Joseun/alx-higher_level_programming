-- Displays the average temperature in a table in hbtn_0c_0 on my SQL server
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
