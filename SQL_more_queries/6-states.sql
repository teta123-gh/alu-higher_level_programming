-- A  script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- Query to  creates the database hbtn_0d_usa and the table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states ( -- Query to create states table with 2 constraints
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL);
