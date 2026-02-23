-- Creates the table second_table in the databases hbtn_0c_0 and adds multiple rows.
-- if the table already exists, the script does not fail.
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
