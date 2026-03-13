CREATE DATABASE chatbot_demo;

USE chatbot_demo;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    password VARCHAR(100)
);
SELECT * FROM students;