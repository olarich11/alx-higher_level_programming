-- Display all cities within the hbtn_0d_usa database
-- Retrieve all rows from a specific column in a database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
