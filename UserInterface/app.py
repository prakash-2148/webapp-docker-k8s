from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import pyodbc
import os

app = Flask(__name__)
app.secret_key = 'account-file.json'  # Change this to a random secret key

# SQL Server connection details
server = os.getenv('DB_SERVER', '104.196.127.218,1433')  # IP of Cloud SQL instance with port
database = os.getenv('DB_NAME', 'mydatabase')  # Database name
username = os.getenv('DB_USER', 'sqlserver')  # SQL Server username
password = os.getenv('DB_PASSWORD', 'Prakash2148@')  # SQL Server password

# Connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
print("Connection String:", conn_str)


def get_all_logins():
    """Fetches all login entries from the database."""
    try:
        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("Cursor:", conn.cursor())
        # Query to fetch all login entries
        cursor.execute("SELECT * FROM Login")
        results = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        return results

    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return []


@app.route('/')
def index():
    return render_template('login.html')  # Render the login form


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        response = requests.post('http://35.196.64.207/validate', json={'username': username, 'password': password})
        print(f"Response from database service: {response.json()}")  # Print response from the database container

        if response.status_code == 200 and response.json().get('valid'):
            flash('Login successful!', 'success')
            return redirect(url_for('welcome'))  # Redirect to a welcome page after successful login
        else:
            flash('Invalid credentials, please try again.', 'danger')
            return redirect(url_for('index'))  # Reload the login page with an error
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('index'))  # Handle any exceptions


@app.route('/welcome')
def welcome():
    return "Welcome to your dashboard!"  # This is a placeholder page for successful login


@app.route('/logins', methods=['GET'])
def display_logins():
    """Fetches and displays all login entries."""
    logins = get_all_logins()
    return render_template('logins.html', logins=logins)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # Run the UserInterface microservice on port 5000