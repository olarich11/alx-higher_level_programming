-- Converts the entire hbtn_0c_0 to UTF8 database to UTF-8 encoding
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
