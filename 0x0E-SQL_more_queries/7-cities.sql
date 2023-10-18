-- Establish the hbtn_0d_usa database and the cities table within it (in the database hbtn_0d_usa) on your MySQL server
-- Establish a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
