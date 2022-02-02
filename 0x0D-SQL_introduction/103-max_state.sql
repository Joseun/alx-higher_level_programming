-- Displays the maximum temperatures in a table in hbtn_0c_0 on my SQL server
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
