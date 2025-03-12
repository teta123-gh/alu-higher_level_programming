-- A script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Query to display the average temperature of a city
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
