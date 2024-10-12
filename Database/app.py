from flask import Flask, jsonify, request, render_template
import pyodbc
import os

app = Flask(__name__)

# SQL Server connection details (replace with your actual values or use environment variables)
server = os.getenv('DB_SERVER', '34.75.171.77,1433')  # IP of Cloud SQL instance with port
database = os.getenv('DB_NAME', 'mydatabase')  # Database name
username = os.getenv('DB_USER', 'sqlserver')  # SQL Server username
password = os.getenv('DB_PASSWORD', 'Prakash2148@')  # SQL Server password

# Connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def check_database_connection():
    """Checks the database connection."""
    try:
        conn = pyodbc.connect(conn_str)
        conn.close()
        return True
    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        return False

@app.route('/')
def home():
    """Home route that shows database connection status."""
    if check_database_connection():
        message = "Database connection successful, DB up and running."
    else:
        message = "Database connection failed. Please check the configuration."
    return jsonify(message=message)  # Return the message as JSON

@app.route('/validate', methods=['POST'])
def validate_login():
    """Validates the login credentials."""
    username = request.json.get('username')
    password = request.json.get('password')

    try:
        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Query to check if the username and password match
        cursor.execute("SELECT * FROM Login WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()

        # Close the connection
        cursor.close()
        conn.close()

        # Return True if the user exists, False otherwise
        return jsonify(valid=(result is not None))

    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return jsonify(error=str(e)), 500

@app.route('/connection')
def connection_status():
    """Checks and renders connection status."""
    if check_database_connection():
        message = "Connection successful"
    else:
        message = "Connection failed"

    return render_template('status.html', message=message)

if __name__ == '__main__':
    if check_database_connection():
        print("Database connection successful, DB up and running.")
    app.run(host='0.0.0.0', port=5001, debug=True)
