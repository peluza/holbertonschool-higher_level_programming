-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_INCREMENT UNIQUE PRIMARY KEY, state_id INT, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id), name VARCHAR(256) NOT NULL);
