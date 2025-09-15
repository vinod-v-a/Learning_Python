"  database connection settings"
import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Create and return a database connection.
    Update the user, password, and host if needed.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",      # or 127.0.0.1
            user="root",           # change if your MySQL user is different
            password="root",  # replace with your MySQL password
            database="library_db"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None
