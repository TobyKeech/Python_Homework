 DROP TABLE IF EXISTS books;
 DROP TABLE IF EXISTS libraries;
 

 CREATE TABLE libraries(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
 );

 CREATE TABLE books(
    id SERIAL PRIMARY KEY, 
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255), 
    library_id INT REFERENCES libraries(id) ON DELETE CASCADE
 );

 INSERT INTO libraries(name)
 VALUES ('Big Reading');

 INSERT INTO libraries (name)
 VALUES ('A B and maybe even Cs');

 INSERT INTO books(title,author,genre,library_id)
 VALUES ('The mysterious history of Lewis', 'Toby', 'non-fiction', 1);

 INSERT INTO books(title,author,genre,library_id)
 VALUES ('Roger: A man or a spaceship?', 'Roger','fiction', 2);