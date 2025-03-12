-- A script that displays the max temperature of each state (ordered by State name).-- Query to display the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;
