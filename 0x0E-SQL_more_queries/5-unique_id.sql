-- Generate the unique_id table on your MySQL server
-- Establish a table
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
