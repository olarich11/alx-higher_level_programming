-- Retrieve all records from second_table table in my MySQL server where the score >= 10.
-- Records are sorted in descending order based on the score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
