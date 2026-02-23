## SQL Project Summary - Introduction

### This project covered the fundamentals of relational databases and SQL using MySQL. Below is a quick summary of the tasks completed:

# 🗄️ Database Operations
- Create a database: CREATE DATABASE IF NOT EXISTS database_name;

- Delete a database: DROP DATABASE IF EXISTS database_name;

- List databases: SHOW DATABASES; (used for testing only)

# 📋 Table Operations
- Create a table with columns and data types:
```bash
sql
CREATE TABLE IF NOT EXISTS table_name (
    id INT,
    name VARCHAR(256)
);
```
-List tables: SHOW TABLES;

- Show table structure: SHOW CREATE TABLE table_name; (alternative to DESCRIBE)

# 🔍 Querying Data:

- Retrieve all rows: SELECT * FROM table_name;

- Retrieve with condition: SELECT ... FROM ... WHERE condition;

- Sort results: ORDER BY column DESC/ASC;

- Limit results: LIMIT n;

# ✍️ Modifying Data:

- Insert a row:
```
sql
INSERT INTO table_name (columns) VALUES (values);
```
- Update data:
```
sql
UPDATE table_name SET column = value WHERE condition;
```
- Delete data:
```
sql
DELETE FROM table_name WHERE condition;
```
# 📊 Aggregate Functions

- Count: COUNT(*)

- Average: AVG(column)

- Sum: SUM(column)

- Max/Min: MAX(column), MIN(column)

# 🧮 Grouping and Sorting:

- Group by: GROUP BY column

- Filter groups: HAVING condition

- Order by: ORDER BY ...

# 🔤 Character Set Conversion (UTF8)
- Alter database:
```
sql
ALTER DATABASE db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
Alter table:
```
sql
ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
# 🌡️ Temperatures Project:

# Imported a dump file and ran analytical queries:

- Average temperature per city.

- Top 3 cities during July and August.

- Maximum temperature per state.

# ⚠️ Important Notes:

- Use uppercase for SQL keywords (SELECT, WHERE, ...).

- Add a comment describing the task before each query.

- Do not use SELECT or SHOW if prohibited.

- End each file with a new line.

# Author:
**Amaal Asiri** ,as a part of Holberton School curriculum.
