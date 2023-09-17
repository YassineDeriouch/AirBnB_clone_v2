-- SQL script to prepares MySQL server for the project

-- create database if it not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user if it not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant SELECT statement privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- flush privileges to apply theses changes above
FLUSH PRIVILEGES;
