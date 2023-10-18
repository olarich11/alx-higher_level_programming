-- Establishes the hbtn_0d_usa database and the states table (in the database hbtn_0d_usa) on your MySQL server
-- Establish a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select a database
USE hbtn_0d_usa;
-- Establish a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
