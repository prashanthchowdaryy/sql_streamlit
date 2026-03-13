Streamlit + MySQL Student Login System

A simple demo project that connects a Streamlit web application with a MySQL database to store and validate student login details.

This project was built to test backend connectivity before integrating more advanced systems like AI chatbots and RAG pipelines.

 Features

 Student Registration Form
 Stores data directly into MySQL
 Login Authentication using stored credentials
 Simple chatbot demo interface
 Backend connectivity testing

🛠 Tech Stack

Python

Streamlit

MySQL

mysql-connector-python

📂 Project Structure
streamlit-mysql-login
│
├── app.py
├── README.md
⚙️ Database Setup

Open MySQL Workbench and run:

CREATE DATABASE chatbot_demo;

USE chatbot_demo;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255),
    password VARCHAR(100)
);
 Install Dependencies
pip install streamlit mysql-connector-python
 Run the Application
streamlit run app.py

Then open:

http://localhost:8501
🧪 Testing the System

1️⃣ Register a new student from the Streamlit interface
2️⃣ Open MySQL Workbench
3️⃣ Run:

SELECT * FROM students;

If the data appears in the table, the Python → MySQL connection is working successfully.
