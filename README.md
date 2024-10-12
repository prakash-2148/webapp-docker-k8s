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

project structure
/User-Login-Microservices
|-- /frontend                 # Frontend Microservice
|   |-- app.py                # Main Flask application for the frontend
|   |-- templates/            # HTML templates for rendering
|   |-- static/               # Static files (CSS, JavaScript)
|   |-- requirements.txt       # Python dependencies for frontend
|
|-- /backend                  # Backend Microservice
|   |-- app.py                # Main Flask API application for backend
|   |-- requirements.txt       # Python dependencies for backend
|
|-- Dockerfile                 # Dockerfile for building the images
|-- docker-compose.yml         # Docker Compose configuration
|-- README.md                  # Project documentation


Testing with Postman

{
    "username": "your_username",
    "password": "your_password"
}

Build the Docker Images

docker build -t frontend:latest ./frontend
docker build -t backend:latest ./backend


Pushing to a Docker Registry

docker tag frontend:latest yourusername/frontend:latest
docker tag backend:latest yourusername/backend:latest

docker push yourusername/frontend:latest
docker push yourusername/backend:latest

Deploying with Kubernetes
kubectl apply -f frontend-deployment.yaml
kubectl apply -f backend-deployment.yaml

