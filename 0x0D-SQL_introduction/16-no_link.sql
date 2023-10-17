-- Display all records from the second_table table taht have a name value in my MySQL server.
-- Records are arranged in descending order based on the score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
