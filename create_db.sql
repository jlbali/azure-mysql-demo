DROP DATABASE IF EXISTS todos_db;
CREATE DATABASE IF NOT EXISTS todos_db;
USE todos_db;

CREATE TABLE Todos (
    id int NOT NULL AUTO_INCREMENT,
    texto varchar(255) NOT NULL,
    PRIMARY KEY (id)
);


INSERT INTO Todos(texto)
VALUES('Recordatorio 1');

INSERT INTO Todos(texto)
VALUES('Recordatorio 2');
