# SQL 

- Relation or Table
- Turple or Row
- Attribute also Collumn or Field

- [x] **Key**:
  - Primary Key
    - `id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE`
  - Logical Key
  - Foreign Key
    - `album_id INTEGER`
    - `genre_id INTEGER`

## Syntax

**CRUD** (create, read, update, delete)

- `CREATE TABLE ___ ( )`
- `INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')`
- `DELETE FROM Users WHERE email = 'csev@umich.edu'`
- `UPADATE Users SET name = 'Charles' WHERE email = 'csev@umich.edu'`
- `SELECT * FROM Users`
- `SELECT * FROM Users WHERE email = 'csev@umich.edu'`
- `SELECT * FROM Users ORDER BY emails`


- `select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id`
