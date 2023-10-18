-- creates the hbtn_0d_2 database and the user user_0d_2
-- Establish a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a new user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Assign SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
