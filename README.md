User Login Microservices


This project consists of two microservices:
Frontend Microservice: A Flask application that provides a user interface for logging in and displaying login results.
Backend Microservice: A Flask API that handles authentication requests and connects to a SQL Server database for login validation.

Table of Contents
Overview
Technologies
Prerequisites
Project Structure
Setup and Run Instructions
Endpoints
Testing with Postman
Docker Deployment
Contributing

Overview

The project demonstrates a simple user login system with two microservices:
Frontend: Users submit login credentials through an HTML form.
Backend: The API validates the credentials using SQL Server and returns the result.

Technologies
Python 3.9
Flask for both frontend and backend microservices
SQL Server for database management
Docker for containerization
Postman for testing
Prerequisites

The followings are installed:

Python 3.9 or higher
Docker
Postman (for testing the APIs)
Flask (pip install flask)
SQL Server ODBC Driver (pyodbc for Python)
