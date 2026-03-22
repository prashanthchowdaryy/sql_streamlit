# Streamlit + MySQL Student Login System

This project is a simple web application built with Streamlit and MySQL.
It stores and validates student login details using a database.

---

## Features

* Student registration form
* Stores data in MySQL
* Login authentication
* Simple chatbot demo
* Backend connectivity testing

---

## Tech Stack

* Python
* Streamlit
* MySQL
* mysql-connector-python

---

## Project Structure

* app.py
* README.md

---

## Database Setup

Run the following in MySQL:

CREATE DATABASE chatbot_demo;

USE chatbot_demo;

CREATE TABLE students (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
phone VARCHAR(15),
address VARCHAR(255),
password VARCHAR(100)
);

---

## Installation

Install dependencies:

pip install streamlit mysql-connector-python

---

## Run

streamlit run app.py

Open in browser:

http://localhost:8501

---

## Testing

1. Register a student using the app
2. Open MySQL and run:

SELECT * FROM students;

3. Check if data is stored

---

## Use Case

* Learning database integration
* Backend testing
* Basic authentication system
