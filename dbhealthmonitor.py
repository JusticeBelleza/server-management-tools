import mysql.connector
from mysql.connector import Error

def check_database_health(host, database, user, password):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password)
        if connection.is_connected():
            print("Database connection established.")
            cursor = connection.cursor()
            cursor.execute("SELECT VERSION();")
            db_version = cursor.fetchone()
            print("Database Version:", db_version[0])
            # Add more checks as needed
            cursor.close()
        else:
            print("Failed to connect to the database.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    DB_HOST = "your_host"
    DB_DATABASE = "your_database"
    DB_USER = "your_username"
    DB_PASSWORD = "your_password"
    check_database_health(DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)
