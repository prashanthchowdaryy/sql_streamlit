import streamlit as st
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PK12345678",
    database="chatbot_demo"
)

cursor = conn.cursor()

st.title("Demo Chatbot Login")

menu = st.sidebar.selectbox("Menu", ["Register", "Login", "Chatbot"])

# REGISTER
if menu == "Register":

    st.subheader("Student Registration")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    address = st.text_input("Address")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        query = """
        INSERT INTO students (name, phone, address, password)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(query, (name, phone, address, password))
        conn.commit()

        st.success("Registration Successful")

# LOGIN
elif menu == "Login":

    st.subheader("Student Login")

    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        query = """
        SELECT * FROM students
        WHERE phone=%s AND password=%s
        """

        cursor.execute(query, (phone, password))
        result = cursor.fetchone()

        if result:
            st.success("Login Successful")
        else:
            st.error("Invalid Credentials")

# CHATBOT DEMO
elif menu == "Chatbot":

    st.subheader("Mini Demo Chatbot")

    user_input = st.text_input("Ask something")

    if user_input:

        if "hello" in user_input.lower():
            st.write("Bot: Hello student,prashanth this side 👋")

        elif "course" in user_input.lower():
            st.write("Bot: We offer Data Science and AI")

        else:
            st.write("Bot: intreating let my master sleep on it for a while. 🤖")