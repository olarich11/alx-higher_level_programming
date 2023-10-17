-- Show the average temperature by city ordered in decending order by temperature (in Fahrenheit)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
