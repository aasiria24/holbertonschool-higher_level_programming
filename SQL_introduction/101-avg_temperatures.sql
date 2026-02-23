-- Computes the average temperature (Fahrenheit) by city and displays results ordered descending.
SELECT city, AVG(temperature) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
