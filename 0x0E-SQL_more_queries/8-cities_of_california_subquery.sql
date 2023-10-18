-- Dispaly a lists aof all the cities of California found in the hbtn_0d_usa database
-- Retrieve all rows from a specific column in a database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
