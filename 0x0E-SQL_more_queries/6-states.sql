-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server --
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE state (id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL, name VARCHAR(256) NOT NULL);