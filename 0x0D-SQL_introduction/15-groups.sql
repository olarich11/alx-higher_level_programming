-- Display the count of records with identical score in the second_table table in my MySQL server.
-- Records are arranged in descending order based on the count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
