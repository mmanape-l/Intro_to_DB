import mysql.connector
from mysql.connector import Error

def create_database():
    """Creates a database named 'alx_book_store' if it does not already exist."""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',        # Change this if your MySQL server is on a different host
            user='root',             # Replace with your MySQL username
            password='password'      # Replace with your MySQL password
        )
        
        if connection.is_connected():
            print("Connected to MySQL Server")

            # Create a cursor object using the connection
            cursor = connection.cursor()

            # SQL query to create database
            create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store;"

            # Execute the SQL query
            cursor.execute(create_database_query)

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        # Print error message if something goes wrong
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals() and cursor.is_connected():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

