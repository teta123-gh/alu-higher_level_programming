-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Query to display the average temperature by city
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
